import numpy as np
import pandas_datareader as web
import datetime as dt
import pandas as pd
import requests
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

end = dt.datetime.now()
start = dt.date(end.year - 5, end.month, end.day)

url = 'https://www.fundamentus.com.br/resultado.php'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
r = requests.get(url, headers=headers)

df = pd.read_html(r.text, decimal=',', thousands='.')[0][['Papel', 'Liq.2meses']]
df.sort_values('Liq.2meses', ascending = False, inplace = True)
sorted_per_liquidity = df['Papel'].copy()[:9]
tickers = [ticker + '.SA' for ticker in sorted_per_liquidity.to_list()]
tickers.append('^BVSP')
data = web.get_data_yahoo(tickers, start, end, interval = 'm')['Adj Close']

log_returns = np.log(data/data.shift())
log_returns = log_returns.dropna()

cov_matrix = log_returns.cov()
var = log_returns['^BVSP'].var()

log_returns.boxplot(figsize = (12,10), grid = False)
plt.title('Stocks monthly returns')

beta,alpha = dict(), dict()

fig, axes = plt.subplots(3,3, dpi=100, figsize=(40,40))
axes = axes.flatten()

for idx, ticker in enumerate(log_returns.columns):
    if ticker != 'Date' and ticker != '^BVSP':
        
        log_returns.plot(kind = 'scatter', x = '^BVSP', y = ticker, ax=axes[idx-1])
 
       
        b_, a_ = np.polyfit(log_returns[ticker], log_returns['^BVSP'], 1)
 
        regression_line = b_ * log_returns['^BVSP'] + a_
        axes[idx-1].plot(log_returns['^BVSP'], regression_line, '-', color = 'r')
        
        beta[ticker] = b_
        alpha[ticker] = a_
plt.suptitle('Beta estimation: regression between IBOV and individual stock monthly performance', size=15)

ER = dict()
rf = 10
rm = log_returns['^BVSP'].mean() * 252

keys = list(beta.keys())

for k in keys:
    ER[k] = rf + beta[k] * (rm-rf)

for k in keys:
    print('Expected return based on CAPM model for {} is {}%'.format(k, round(ER[k],2)))
    
for k in keys:
    print('Return based on historical data for {} is {}%'.format(k,round(log_returns[k].mean() * 252,2)))





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    