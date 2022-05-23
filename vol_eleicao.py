import yfinance as yf
import numpy as np
import datetime as dt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
pio.renderers.default ='browser'

ibov = '^BVSP'

start1 = dt.datetime(1998,1,1)
end1 = dt.datetime(1998,12,31)

start2 = dt.datetime(2002,1,1)
end2 = dt.datetime(2002,12,31)

start3 = dt.datetime(2006,1,1)
end3 = dt.datetime(2006,12,31)

start4 = dt.datetime(2010,1,1)
end4 = dt.datetime(2010,12,31)

start5 = dt.datetime(2014,1,1)
end5 = dt.datetime(2014,12,31)

start6 = dt.datetime(2018,1,1)
end6 = dt.datetime(2018,12,31)

start7 = dt.datetime(2022,1,1)
end7 = dt.datetime.today()

ibov_1998 = yf.download(ibov, start1, end1)['Adj Close']
ibov_1998_returns = ibov_1998.pct_change()
ibov_1998_returns = ibov_1998_returns.fillna(0)
ibov_1998_volatility = np.std(ibov_1998_returns)
ibov_1998_volatility_annual = ibov_1998_volatility * np.sqrt(252)

vol_1998 = str(round(ibov_1998_volatility_annual, 3) * 100)

ibov_2002 = yf.download(ibov, start2, end2)['Adj Close']
ibov_2002_returns = ibov_2002.pct_change()
ibov_2002_returns = ibov_2002_returns.fillna(0)
ibov_2002_volatility = np.std(ibov_2002_returns)
ibov_2002_volatility_annual = ibov_2002_volatility * np.sqrt(252)

vol_2002 = str(round(ibov_2002_volatility_annual, 3) * 100)

ibov_2006 = yf.download(ibov, start3, end3)['Adj Close']
ibov_2006_returns = ibov_2006.pct_change()
ibov_2006_returns = ibov_2006_returns.fillna(0)
ibov_2006_volatility = np.std(ibov_2006_returns)
ibov_2006_volatility_annual = ibov_2006_volatility * np.sqrt(252)

vol_2006 = str(round(ibov_2006_volatility_annual, 3) * 100)

ibov_2010 = yf.download(ibov, start4, end4)['Adj Close']
ibov_2010_returns = ibov_2010.pct_change()
ibov_2010_returns = ibov_2010_returns.fillna(0)
ibov_2010_volatility = np.std(ibov_2010_returns)
ibov_2010_volatility_annual = ibov_2010_volatility * np.sqrt(252)

vol_2010 = str(round(ibov_2010_volatility_annual, 2) * 100)

ibov_2014 = yf.download(ibov, start5, end5)['Adj Close']
ibov_2014_returns = ibov_2014.pct_change()
ibov_2014_returns = ibov_2014_returns.fillna(0)
ibov_2014_volatility = np.std(ibov_2014_returns)
ibov_2014_volatility_annual = ibov_2014_volatility * np.sqrt(252)

vol_2014 = str(round(ibov_2014_volatility_annual, 3) * 100)

ibov_2018 = yf.download(ibov, start6, end6)['Adj Close']
ibov_2018_returns = ibov_2018.pct_change()
ibov_2018_returns = ibov_2018_returns.fillna(0)
ibov_2018_volatility = np.std(ibov_2018_returns)
ibov_2018_volatility_annual = ibov_2018_volatility * np.sqrt(252)

vol_2018 = str(round(ibov_2018_volatility_annual, 3) * 100)

ibov_2022 = yf.download(ibov, start7, end7)['Adj Close']
ibov_2022_returns = ibov_2022.pct_change()
ibov_2022_returns = ibov_2022_returns.fillna(0)
ibov_2022_volatility = np.std(ibov_2022_returns)
ibov_2022_volatility_annual = ibov_2022_volatility * np.sqrt(252)

vol_2022 = str(round(ibov_2022_volatility_annual, 3) * 100)

fig = make_subplots(rows = 2, cols = 4)
trace0 = go.Histogram(x = ibov_1998_returns, name = 'Ibov-1998')
trace1 = go.Histogram(x = ibov_2002_returns, name = 'Ibov-2002')
trace2 = go.Histogram(x = ibov_2006_returns, name = 'Ibov-2006')
trace3 = go.Histogram(x = ibov_2010_returns, name = 'Ibov-2010')
trace4 = go.Histogram(x = ibov_2014_returns, name = 'Ibov-2014')
trace5 = go.Histogram(x = ibov_2018_returns, name = 'Ibov-2018')
trace6 = go.Histogram(x = ibov_2022_returns, name = 'Ibov-2022')

fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 2)
fig.append_trace(trace2, 1, 3)
fig.append_trace(trace3, 1, 4)
fig.append_trace(trace4, 2, 1)
fig.append_trace(trace5, 2, 2)
fig.append_trace(trace6, 2, 3)

fig.update_layout(title = 'Frequency of Returns - Election Years', xaxis = dict(title = 'Ibov 1998 Annualized Vol: ' 
                                                               + str(vol_1998 + '%')), 
                  xaxis2 = dict(title = 'Ibov 2002 Annualized Vol: ' + str(vol_2002 + '%')),
                  xaxis3 = dict(title = 'Ibov 2006 Annualized Vol: ' + str(vol_2006) + '%'), 
                  xaxis4 = dict(title = 'Ibov 2010 Annualized Vol: ' + str(vol_2010 + '%')),
                  xaxis5 = dict(title = 'Ibov 2014 Annualized Vol: ' + str(vol_2014) + '%'),
                  xaxis6 = dict(title = 'Ibov 2018 Annualized Vol: ' + str(vol_2018 + '%')),
                  xaxis7 = dict(title = 'Ibov 2022 Annualized Vol: ' + str(vol_2022 + '%')))

fig.show()

