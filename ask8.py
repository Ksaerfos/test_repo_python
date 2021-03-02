import urllib.request
import json
from time import sleep
def get_coin(coin):
    url="https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC&tsyms=EUR&e=CCCAGG"
    r=urllib.request.urlopen(url)
    html=r.read()
    html = html.decode()
    d = json.load(html)
    return d[coin]["EUR"]

for i in range(10) :
    print(get_coin("BTC"))
    sleep(5)

