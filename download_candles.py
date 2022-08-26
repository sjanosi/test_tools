import datetime as dt
import os
import urllib.request
import zipfile


now = dt.datetime.now()

for i in range(365):
	day_date = now - dt.timedelta(days=365-i)
	file_name = day_date.strftime("ETHUSDC-1m-%Y-%m-%d.zip")

	file_full_path = "/home/ubuntu/temp/" + file_name

	url = "https://data.binance.vision/data/spot/daily/klines/ETHUSDC/1m/" + file_name
	urllib.request.urlretrieve(url, file_full_path)

	with zipfile.ZipFile(file_name, 'r') as zip_ref:
		zip.ref.extractall('./1m_candles')

	os.remove(file_full_path)
