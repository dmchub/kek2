import requests
from time import sleep
import base64

a = b'NTYyNDA1ODEzOkFBRVdVSW1qekR3YTRGOXV3dzg4UUdJMDZuUUl3Ti1ZZmNJ'
b = base64.b64decode(a).decode("utf-8", "ignore")
url = "https://api.telegram.org/bot{}/".format(b)

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


def get_member_name(update):
	member = update["message"]['new_chat_member']['first_name']
	return member


def send_mess(chat, text):  
	params = {'chat_id': chat, 'text': text}
	response = requests.post(url + 'sendMessage', data=params)
	return response

	
def main():
	update_id = last_update(get_updates_json(url))['update_id']
	new_member = 'new_chat_member'
	while True:
		if update_id == last_update(get_updates_json(url))['update_id']:
			message = last_update(get_updates_json(url))['message']
			keys = message.keys()
			if new_member in keys:
				name = get_member_name(last_update(get_updates_json(url)))
				send_mess(get_chat_id(last_update(get_updates_json(url))), 'Приветствую, {}! \n\nЭто группа Нассима Талеба.\nЗдесь собираются охотники за счастливыми лебедями, жертвы ассиметрии, жадные читатели и просто антихрупкие люди. \n\n Наш канал \n https://t.me/nntaleb \n\n Канал в контакте \n https://vk.com/nntaleb \n\n Причитать новую книгу Skin in the Game на английском \n https://t.me/nntaleb_group/714 \n\n Прочитать старую книгу Dynamic Hedging на английском \n https://t.me/nntaleb_group/690 \n\n Получить прокси для Телеграмма \n https://t.me/nntaleb_group/747 \n\n Как настроить доступ к Телеграмму через Tor \n https://t.me/nntaleb_group/770  \n\n Скачать книги Нассима Талеба Вы можете здесь \n https://rutracker.org/forum/tracker.php?nm=%D0%BD%D0%B0%D1%81%D1%81%D0%B8%D0%BC%20%D1%82%D0%B0%D0%BB%D0%B5%D0%B1 \n\n'.format(name))
			else:
				send_mess(get_chat_id(last_update(get_updates_json(url))), 'Саудовская Аравия должна быть разрушена!!! Kapish???')
			update_id += 1
		sleep(1)       


if __name__ == '__main__':  
	main()