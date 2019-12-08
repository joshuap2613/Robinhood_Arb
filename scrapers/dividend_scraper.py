import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

fields = ['exOrEffDate', 'type', 'amount', 'declarationDate', 'recordDate', 'paymentDate']

TICKER_PATH = "fixtures/tickers.txt"
OUTPUT_PATH = "fixtures/dividends.csv"
f = open(OUTPUT_PATH, "w")
f.write("ticker,")
for field in fields:
    f.write(field)
    f.write(',')
f.write('\n')

tickers = [word for word in open(TICKER_PATH,"r")]


for t in tickers:
    t = t.strip()
    url = 'http://api.nasdaq.com/api/quote/' + t + '/dividends?assetclass=stocks'
    print(t)
    try:
        response = requests.get(url, timeout=5)
        json_data = json.loads(response.text)
    except:
        continue
    #print(json_data)
    if json_data['data'] != None and json_data['data']['dividends']['rows'] != None:
        rows = json_data['data']['dividends']['rows']
        for row in rows:
            print(row)
            f.write(t)
            f.write(",")
            for field in fields:
                f.write(row[field])
                f.write(',')
            f.write('\n')
f.close()
prev_data = pd.read_csv("prev_div.csv")
cur_data = pd.read_csv("fixtures/dividends.csv")
pd.concat([prev_data,cur_data]).drop_duplicates().reset_index(drop=True)
pd.to_csv("fixtures/dividends.csv")
print('done')
