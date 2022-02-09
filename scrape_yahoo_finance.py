import requests
from datetime import datetime
import time

def getDate(dt):
  d = datetime.strptime(dt, '%Y/%m/%d')
  return d

ticker = input("Enter the ticker symbol : \n")
from_date = input("ENTER START DATE IN YYYY/MM/DD format : \n")
to_date   = input("ENTER END DATE IN YYYY/MM/DD format : \n")

from_date = getDate(from_date)
to_date = getDate(to_date)

from_epoch = int(time.mktime(from_date.timetuple()))
to_epoch  = int(time.mktime(to_date.timetuple()))

url =f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

url_max = "https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=345427200&period2=1644451200&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}  

content = requests.get(url, headers=headers).content

with open('data.csv', 'wb') as file:
  file.write(content)