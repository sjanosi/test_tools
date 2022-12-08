from datetime import date, timedelta
import os
import urllib.request
import zipfile

# the symbol pairs to download candles for
symbols = ['ETHBUSD']

# the timeframes to download candles for
timeframes = ['1m', '5m', '15m', '1h']

# binance URL
binance_url = "https://data.binance.vision/?prefix=data/spot/daily/klines"

# the home directory
home_dir = "/home/ubuntu/klines"

# get the current day
today = date.today()
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
				url = f"{binance_url}/{symbol}/{timeframe}/{filename}.zip"
				local_zipfile = f"{timeframe_dir}/{filename}.zip"
				urllib.request.urlretrieve(url, local_zipfile)
				# extract the zip archive
				with zipfile.ZipFile(local_zipfile, 'r') as zip_ref:
					zip_ref.extractall(timeframe_dir)
				# delete the zip archive
				os.remove(local_zipfile)
			# increment the current day
			current_day += timedelta(1)
