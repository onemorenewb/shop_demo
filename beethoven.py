import requests
import json
from time import sleep

def get_btc():
    url = 'https://api.cryptonator.com/api/ticker/btc-usd'
    result = requests.get(url)
    decoded = result.json()
    #print(json.dumps(result.json(), indent=4, ensure_ascii=False))
    #print(decoded['ticker']['price'])
    price = decoded['ticker']['price']
    sleep(1)
    return price


#print(get_btc())
