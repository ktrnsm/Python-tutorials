import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

bitcoin = yf.download('BTC-USD', start='2010-01-01')['Close']

# Tarihleri gün olarak değiştirme
days = mdates.DayLocator()
years = mdates.YearLocator()
years_fmt = mdates.DateFormatter('%Y')
start_date = bitcoin.index[0]
dates = np.array([(date - start_date).days for date in bitcoin.index])

# Logaritmik dönüşüm
log_bitcoin = np.log(bitcoin)

# Grafik çizimi
fig, ax = plt.subplots()
ax.plot(dates, log_bitcoin)
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(days)
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
ax.set_xlabel('Tarih (günler)')
ax.set_ylabel('Bitcoin Fiyatı (Logaritmik)')
ax.set_title('Bitcoin Fiyatları (Logaritmik Ölçek)')
plt.show()
