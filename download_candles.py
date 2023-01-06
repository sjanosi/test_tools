from datetime import date, timedelta
import os
import requests
import zipfile
import io


# the symbol pairs to download candles for
symbols = ['ETHBUSD']
# the timeframes to download candles for
timeframes = ['1m', '5m', '15m', '1h']
# binance URL
binance_url = "https://data.binance.vision/data/spot/daily/klines"
# the home directory
# home_dir = "/Users/sorinjanosi/klines"
home_dir = "/home/ubuntu/klines"
# get the current day
today = date.today()
yesterday = today - timedelta(1)
# get the first day to start downloading candles
first_day = today - timedelta(365)

# download candles files for each symbol and timeframe
for symbol in symbols:
	# create symbol directory if it does not exist
	symbol_dir = f"{home_dir}/{symbol}"
	if not os.path.exists(symbol_dir):
		os.makedirs(symbol_dir)
	# get candles files for each timeframe
	for timeframe in timeframes:
		# create timeframe directory if it does not exist
		timeframe_dir = f"{symbol_dir}/{timeframe}"
		if not os.path.exists(timeframe_dir):
			os.makedirs(timeframe_dir)

		# download all daily files
		current_day = first_day
		while current_day != today:
			# the file to download
			filename = current_day.strftime(f"{symbol}-{timeframe}-%Y-%m-%d")
			# check if file exist already
			if not os.path.exists(f"{timeframe_dir}/{filename}.csv"):
				# download the file
				zip_file_url = f"{binance_url}/{symbol}/{timeframe}/{filename}.zip"
				local_zipfile = f"{timeframe_dir}/{filename}.zip"
				# download the zip file
				r = requests.get(zip_file_url, stream=True)
				z = zipfile.ZipFile(io.BytesIO(r.content))
				z.extractall(timeframe_dir)
				z.close()
				# delete the zip archive
				# os.remove(local_zipfile)
			# increment the current day
			current_day += timedelta(1)
