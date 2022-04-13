import numpy as np
import yfinance as yf
import pandas as pd
import requests
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import random

sns.set()

warnings.filterwarnings('ignore')

url = 'https://www.fundamentus.com.br/resultado.php'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
r = requests.get(url, headers=headers)

df = pd.read_html(r.text, decimal=',', thousands='.')[0][['Papel', 'Liq.2meses']]
df.sort_values('Liq.2meses', ascending = False, inplace = True)
sorted_per_liquidity = df['Papel'].copy()[:50]
tickers = [ticker + '.SA' for ticker in sorted_per_liquidity.to_list()]

data = yf.download(tickers, period = '1y')['Adj Close']
data.dropna(how = 'all', inplace = True)
data.dropna(axis = 1, inplace = True, thresh = 200)

ibov = yf.download('^BVSP', period = '1y')['Adj Close']
ibov = ibov / ibov.iloc[0]

retorno = data.pct_change()
retorno_acumulado = (1 + retorno).cumprod()
retorno_acumulado.iloc[0] = 1 
n = 1000

saldos_finais= []

for i in range(n):
    carteira = random.sample(list(data.columns) , k= 5)
    carteira = 10000 * retorno_acumulado.loc[: , carteira]
    carteira['saldo'] = carteira.sum(axis=1)
    carteira['saldo'].plot(figsize=(18,8))
    saldos_finais.append(carteira['saldo'].iloc[-1])

(ibov*50000).plot(linewidth=4, color='black', label='IBOV')

supera_ibov = 0
saldo_final_ibov = ibov.iloc[-1]*50000
for saldo in saldos_finais:
  if (saldo > saldo_final_ibov):
    supera_ibov += 1

supera_ibov_porcento = round((supera_ibov / n)*100, 2)
plt.title(f'{supera_ibov} de {n} carteiras ({supera_ibov_porcento}%) bateram o IBOV no período', fontsize = 25)

