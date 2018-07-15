import requests
from config import *
from beethoven import *
import json
from time import sleep

URL = 'https://api.telegram.org/bot' + token + '/'


def get_bot_updates(limit, offset):
    url = URL + 'getUpdates'
    par = {'limit': limit, 'offset': offset}
    result = requests.get(url, params=par)
    decoded = result.json()
    return decoded ['result']

def send_bot_message(chat_id, text):
    url = URL + 'sendMessage'
    par = {'chat_id': chat_id, 'text': text}
    result = requests.get(url, params=par)
    decoded = result.json()
    return decoded

new_offset=0
update_id=0
result=get_bot_updates(5, new_offset)  

for item in result:
    text = item['message']['text']
    chat_id = item['message']['chat']['id']
    update_id = item['update_id']
    sleep(1)
    if (text == '/btc'):
        send_bot_message(chat_id, get_btc() + ' usd')
    new_offset = update_id + 1
    get_bot_updates(5, new_offset)
    
