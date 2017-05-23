#!/usr/bin/python3
 
import datetime
from urllib.request import urlopen
import json
import math
import time
 
# Whalepool Shitcoin Index (WSI)
# Index of top 10 shitcoins by marketcap
# 1000 pts = standardized to 1 Billion USD
# Uses CoinMarketCap to determine rank and marketcap (by USD)
# Written by swapman @ https://www.whalepool.io
 
 
#Manually set coins that are disqualified from being in the index
nonrankcoins=['PIVX', 'USDT']
 
#scrape from coinmarketcap
url = "https://api.coinmarketcap.com/v1/ticker/?limit=15"
 
#grab url
page = urlopen(url)
 
#read data
data=page.read()
 
#load json to grab coin parms
wsi=json.loads(data.decode())
marketcaptotal=0
menrank=0
#sum the marketcaps
for x in range(1,11):
    if wsi[x]['symbol'] in nonrankcoins:
        continue
    menrank=menrank+1;
    if menrank>10:
        break
    print(float(wsi[x]['market_cap_usd']))
    marketcaptotal=float(marketcaptotal)+float(wsi[x]['market_cap_usd'])
   
#Total marketcaps in US dollars
marketcaptotal=round(marketcaptotal,0)
 
#WSI is just marketcap standardized to 1 billion to 1000 pts
wsivalue=(marketcaptotal/1000000000)*1000
 
f = open('wsidata.txt', 'a', encoding='utf-8')
f.write(str(round(time.time())) + "," + str(round(wsivalue,2)))
f.write("\n")
f.close()
 
#grab poloniex ticker for BTC 24Hr pct change
 
url2= "https://poloniex.com/public?command=returnTicker"
#grab url
page2 = urlopen(url2)
 
#read data
data2=page2.read()
 
#load json to grab coin parms
poloticker=json.loads(data2.decode())
 
weightedpct=0
minrank=0
for x in range(1,15):
    if wsi[x]['symbol'] in nonrankcoins:
        continue
    minrank=minrank+1;
    if minrank>10:
        break
    weightedpct=weightedpct+(float(wsi[x]['percent_change_24h'])*(float(wsi[x]['market_cap_usd'])/marketcaptotal))
 
 
#24-hour BTC-value pct change (most active pairs are BTC)
#print(weightedpct)
