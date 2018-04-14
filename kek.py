import requests
from time import sleep
import base64

a = b'NTYyNDA1ODEzOkFBRVdVSW1qekR3YTRGOXV3dzg4UUdJMDZuUUl3Ti1ZZmNJ'
b = base64.b64decode(a).decode("utf-8", "ignore")
url = "https://api.telegram.org/bot{}/".format(b)

greetings = ('здравствуй', 'привет', 'ку', 'здорово')

def get_updates_json(request):  
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()


def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]
    
    
def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id


def get_chat_text(chat, text):
    chat_text = update['message']['text']
    return chat_text


def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def main():
    data = get_updates_json(url)
    results = data['result']
    index = len(results) - 1
    member = results[index]["message"]['new_chat_member']['first_name']
    chat_id = results[index]['message']['chat']['id']
    chat_name = results[index]['message']['chat']['title']
    """
    print(index)
    print('Привет {}'.format(member))
    print('Номер чатика: {}, название: {}'.format(chat_id, chat_name))

    
    if chat_text in greetings:
        send_mess(get_chat_id(last_update(get_updates_json(url))), 'чо бля')
    else:
        send_mess(get_chat_id(last_update(get_updates_json(url))), 'не понимать')
    
    
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        last_chat_text = last_update(get_updates_json(url))['text']
        if last_chat_text in greetings and update_id == last_update(get_updates_json(url))['update_id']:
           send_mess(get_chat_id(last_update(get_updates_json(url))), 'чо бля')
           update_id += 1
        elif update_id == last_update(get_updates_json(url))['update_id']:
           send_mess(get_chat_id(last_update(get_updates_json(url))), 'привет :)')
           update_id += 1
        sleep(1)       
    """

    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           # print('Привет {} \nДобро пожаловать в чат. \nПредставься, пожалуйста и расскажи немного о себе, если не сложно'.format(member))
           send_mess(get_chat_id(last_update(get_updates_json(url))), 'Привет {} \nДобро пожаловать в чат. \nПредставься, пожалуйста и расскажи немного о себе, если не сложно'.format(member))
           update_id += 1
        sleep(1)       
    

if __name__ == '__main__':  
    main()