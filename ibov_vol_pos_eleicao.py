import yfinance as yf
import numpy as np
import datetime as dt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
pio.renderers.default ='browser'

ibov = '^BVSP'

start1 = dt.datetime(1999,1,1)
end1 = dt.datetime(1999,12,31)

start2 = dt.datetime(2003,1,1)
end2 = dt.datetime(2003,12,31)

start3 = dt.datetime(2007,1,1)
end3 = dt.datetime(2007,12,31)

start4 = dt.datetime(2011,1,1)
end4 = dt.datetime(2011,12,31)

start5 = dt.datetime(2015,1,1)
end5 = dt.datetime(2015,12,31)

start6 = dt.datetime(2019,1,1)
end6 = dt.datetime(2019,12,31)

ibov_1999 = yf.download(ibov, start1, end1)['Adj Close']
ibov_1999_returns = ibov_1999.pct_change()
ibov_1999_returns = ibov_1999_returns.fillna(0)
ibov_1999_volatility = np.std(ibov_1999_returns)
ibov_1999_volatility_annual = ibov_1999_volatility * np.sqrt(252)

vol_1999 = str(round(ibov_1999_volatility_annual, 3) * 100)

ibov_2003 = yf.download(ibov, start2, end2)['Adj Close']
ibov_2003_returns = ibov_2003.pct_change()
ibov_2003_returns = ibov_2003_returns.fillna(0)
ibov_2003_volatility = np.std(ibov_2003_returns)
ibov_2003_volatility_annual = ibov_2003_volatility * np.sqrt(252)

vol_2003 = str(round(ibov_2003_volatility_annual, 3) * 100)

ibov_2007 = yf.download(ibov, start3, end3)['Adj Close']
ibov_2007_returns = ibov_2007.pct_change()
ibov_2007_returns = ibov_2007_returns.fillna(0)
ibov_2007_volatility = np.std(ibov_2007_returns)
ibov_2007_volatility_annual = ibov_2007_volatility * np.sqrt(252)

vol_2007 = str(round(ibov_2007_volatility_annual, 3) * 100)

ibov_2011 = yf.download(ibov, start4, end4)['Adj Close']
ibov_2011_returns = ibov_2011.pct_change()
ibov_2011_returns = ibov_2011_returns.fillna(0)
ibov_2011_volatility = np.std(ibov_2011_returns)
ibov_2011_volatility_annual = ibov_2011_volatility * np.sqrt(252)

vol_2011 = str(round(ibov_2011_volatility_annual, 2) * 100)

ibov_2015 = yf.download(ibov, start5, end5)['Adj Close']
ibov_2015_returns = ibov_2015.pct_change()
ibov_2015_returns = ibov_2015_returns.fillna(0)
ibov_2015_volatility = np.std(ibov_2015_returns)
ibov_2015_volatility_annual = ibov_2015_volatility * np.sqrt(252)

vol_2015 = str(round(ibov_2015_volatility_annual, 3) * 100)

ibov_2019 = yf.download(ibov, start6, end6)['Adj Close']
ibov_2019_returns = ibov_2019.pct_change()
ibov_2019_returns = ibov_2019_returns.fillna(0)
ibov_2019_volatility = np.std(ibov_2019_returns)
ibov_2019_volatility_annual = ibov_2019_volatility * np.sqrt(252)

vol_2019 = str(round(ibov_2019_volatility_annual, 2) * 100)

fig = make_subplots(rows = 2, cols = 3)
trace0 = go.Histogram(x = ibov_1999_returns, name = 'Ibov-1999')
trace1 = go.Histogram(x = ibov_2003_returns, name = 'Ibov-2003')
trace2 = go.Histogram(x = ibov_2007_returns, name = 'Ibov-2007')
trace3 = go.Histogram(x = ibov_2011_returns, name = 'Ibov-2011')
trace4 = go.Histogram(x = ibov_2015_returns, name = 'Ibov-2015')
trace5 = go.Histogram(x = ibov_2019_returns, name = 'Ibov-2019')

fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 2)
fig.append_trace(trace2, 1, 3)
fig.append_trace(trace3, 2, 1)
fig.append_trace(trace4, 2, 2)
fig.append_trace(trace5, 2, 3)

fig.update_layout(title = 'Frequency of Returns - 1Y After Election', xaxis = dict(title = 'Ibov 1999 Annualized Vol: ' 
                                                               + str(vol_1999 + '%')), 
                  xaxis2 = dict(title = 'Ibov 2003 Annualized Vol: ' + str(vol_2003 + '%')),
                  xaxis3 = dict(title = 'Ibov 2007 Annualized Vol: ' + str(vol_2007) + '%'), 
                  xaxis4 = dict(title = 'Ibov 2011 Annualized Vol: ' + str(vol_2011 + '%')),
                  xaxis5 = dict(title = 'Ibov 2015 Annualized Vol: ' + str(vol_2015) + '%'),
                  xaxis6 = dict(title = 'Ibov 2019 Annualized Vol: ' + str(vol_2019 + '%')),
                  )

fig.show()