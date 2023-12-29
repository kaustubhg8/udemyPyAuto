import time

import requests
from datetime import datetime

ticker = input('Enter the ticker symbol: ')
from_date = input('Enter a start date in yyyy/mm/dd format: ')
to_date = input('Enter a end date in yyyy/mm/dd format: ')

from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date,'%Y/%m/%d')

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))


url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}.NS?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

# These are user agents
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

stock_data = requests.get(url, headers=headers).content
print(url)

with open(f'{ticker}.csv', 'wb') as file:
    file.write(stock_data)

