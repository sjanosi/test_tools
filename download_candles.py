import datetime as dt
import os
import shutil
import urllib.request
import zipfile


now = dt.datetime.now()

for i in range(365):
	day_date = now - dt.timedelta(days=365-i)

	temp_file_path = "/home/ubuntu/temp/"

	full_1m_path = '/home/ubuntu/candles_data/1m_candles/'
	full_5m_path = '/home/ubuntu/candles_data/5m_candles/'

	# download 1m candles
	filename_1m_csv = day_date.strftime("ETHUSDC-1m-%Y-%m-%d.csv")
	filename_1m_zip = day_date.strftime("ETHUSDC-1m-%Y-%m-%d.zip")


	if not os.path.exists(full_1m_path + filename_1m_csv):
		temp_zip_file = temp_file_path + filename_1m_zip

		url_1m = "https://data.binance.vision/data/spot/daily/klines/ETHUSDC/1m/" + filename_1m_zip
		urllib.request.urlretrieve(url_1m, temp_zip_file)

		with zipfile.ZipFile(temp_zip_file, 'r') as zip_ref:
			zip_ref.extractall(full_1m_path + filename_1m_csv)

		os.remove(temp_zip_file)

		shuitl.copyfile(full_1m_path + filename_1m_csv, "./candles_1m/" + filename_1m_csv)

	# download 5m candles
	filename_5m_csv = day_date.strftime("ETHUSDC-5m-%Y-%m-%d.csv")
	filename_5m_zip = day_date.strftime("ETHUSDC-5m-%Y-%m-%d.zip")


	if not os.path.exists(full_5m_path + filename_5m_csv):
		temp_zip_file = temp_file_path + filename_5m_zip

		url_5m = "https://data.binance.vision/data/spot/daily/klines/ETHUSDC/5m/" + filename_5m_zip
		urllib.request.urlretrieve(url_5m, temp_zip_file)

		with zipfile.ZipFile(temp_zip_file, 'r') as zip_ref:
			zip_ref.extractall(full_5m_path + filename_5m_csv)

		os.remove(temp_zip_file)

		shuitl.copyfile(full_5m_path + filename_5m_csv, "./candles_5m/" + filename_5m_csv)
