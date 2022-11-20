import json  
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import pandas_datareader as web
import functools
import warnings

plt.style.use('default')

warnings.filterwarnings('ignore')

start = (dt.datetime(2014,9,15)).strftime('%d-%m-%Y')
today = dt.datetime.today()
ts = pd.Timestamp(str(today))
offset = pd.tseries.offsets.BusinessDay(n = 1)
end = (today - offset).strftime('%d-%m-%Y')

df_volume = web.DataReader('BTC-USD', 'yahoo', start, end)['Volume']
df_volume = df_volume.to_frame()
df_volume = df_volume.reset_index()
df_volume['Date'] = df_volume['Date'].apply(lambda x: x.strftime('%d-%m-%Y'))

with open('bitcoin-number-of-active-addresses.json', 'r') as f:
    data = json.loads(f.read())

df_address = pd.json_normalize(data, record_path = ['Active Addresses'])

df_address['t'] = pd.to_datetime(df_address['t']).dt.tz_localize(None)
df_address['t'] = df_address['t'].apply(lambda x: x.strftime('%d-%m-%Y'))
df_address.rename(columns = {'t': 'Date', 'v': 'Address'}, inplace = True)

df_prices = pd.read_excel('BTC-USD.xlsx')
df_prices['Date'] = df_prices['Date'].apply(lambda x: x.strftime('%d-%m-%Y'))

df_final = df_prices.merge(df_address, how = 'left',on = 'Date')
df_final = df_final.set_index('Date')
df_final = df_final[::-1]

ax = df_final.plot(use_index = True, y = 'Price', legend = False, color = '#6A96C7')
ax2 = ax.twinx()
df_final.plot(use_index = True, y = 'Address', ax = ax2, legend = False, color = '#9FDBFF')
ax.figure.legend()
plt.title('BTC Price and Unique Addresses')
plt.show()

df_final2 = functools.reduce(lambda left,right: pd.merge(left,right,on='Date'), [df_volume, df_address, df_prices])
df_final2 = df_final2.set_index('Date')

sns.pairplot(df_final2)
plt.suptitle('Pairplot - Price x Volume x Address')
plt.show()

volume = df_final2['Volume']
price = df_final2['Price']
address = df_final2['Address']

corr = df_final2.corr()
sns.heatmap(corr, xticklabels = corr.columns.values, yticklabels = corr.columns.values, 
            annot = True, fmt = '.2f', cmap = 'Blues')

plt.title('Pearson Correlation')
plt.show()