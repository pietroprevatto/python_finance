import yfinance as yf
import datetime as dt
import pandas as pd
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
df_1998 = pd.DataFrame(ibov_1998)
df_1998['retorno'] = ibov_1998.pct_change().iloc[1:]
ibov_1998_returns = df_1998['retorno']
ibov_1998_returns = ibov_1998_returns.fillna(0)
ibov_1998_cumulative = (1000 * (1 + ibov_1998_returns).cumprod())
peaks_1998 = ibov_1998_cumulative.cummax()
df_1998['drawdown'] = (ibov_1998_cumulative - peaks_1998) / peaks_1998
drawdown_1998 = df_1998['drawdown']
max_drawdown_1998 =(df_1998['drawdown'].min())*-100
max_drawdown_1998 = str(round(max_drawdown_1998, 3))

ibov_2002 = yf.download(ibov, start2, end2)['Adj Close']
df_2002 = pd.DataFrame(ibov_2002)
df_2002['retorno'] = ibov_2002.pct_change().iloc[1:]
ibov_2002_returns = df_2002['retorno']
ibov_2002_returns = ibov_2002_returns.fillna(0)
ibov_2002_cumulative = (1000 * (1 + ibov_2002_returns).cumprod())
peaks_2002 = ibov_2002_cumulative.cummax()
df_2002['drawdown'] = (ibov_2002_cumulative - peaks_2002) / peaks_2002
drawdown_2002 = df_2002['drawdown']
max_drawdown_2002 =(df_2002['drawdown'].min())*-100
max_drawdown_2002 = str(round(max_drawdown_2002, 2))

ibov_2006 = yf.download(ibov, start3, end3)['Adj Close']
df_2006 = pd.DataFrame(ibov_2006)
df_2006['retorno'] = ibov_2006.pct_change().iloc[1:]
ibov_2006_returns = df_2006['retorno']
ibov_2006_returns = ibov_2006_returns.fillna(0)
ibov_2006_cumulative = (1000 * (1 + ibov_2006_returns).cumprod())
peaks_2006 = ibov_2006_cumulative.cummax()
df_2006['drawdown'] = (ibov_2006_cumulative - peaks_2006) / peaks_2006
drawdown_2006 = df_2006['drawdown']
max_drawdown_2006 =(df_2006['drawdown'].min())*-100
max_drawdown_2006 = str(round(max_drawdown_2006, 2))

ibov_2010 = yf.download(ibov, start4, end4)['Adj Close']
df_2010 = pd.DataFrame(ibov_2010)
df_2010['retorno'] = ibov_2010.pct_change().iloc[1:]
ibov_2010_returns = df_2010['retorno']
ibov_2010_returns = ibov_2010_returns.fillna(0)
ibov_2010_cumulative = (1000 * (1 + ibov_2010_returns).cumprod())
peaks_2010 = ibov_2010_cumulative.cummax()
df_2010['drawdown'] = (ibov_2010_cumulative - peaks_2010) / peaks_2010
drawdown_2010 = df_2010['drawdown']
max_drawdown_2010 =(df_2010['drawdown'].min())*-100
max_drawdown_2010 = str(round(max_drawdown_2010, 2))

ibov_2014 = yf.download(ibov, start5, end5)['Adj Close']
df_2014 = pd.DataFrame(ibov_2014)
df_2014['retorno'] = ibov_2014.pct_change().iloc[1:]
ibov_2014_returns = df_2014['retorno']
ibov_2014_returns = ibov_2014_returns.fillna(0)
ibov_2014_cumulative = (1000 * (1 + ibov_2014_returns).cumprod())
peaks_2014 = ibov_2014_cumulative.cummax()
df_2014['drawdown'] = (ibov_2014_cumulative - peaks_2014) / peaks_2014
drawdown_2014 = df_2014['drawdown']
max_drawdown_2014 =(df_2014['drawdown'].min())*-100
max_drawdown_2014 = str(round(max_drawdown_2014, 2))

ibov_2018 = yf.download(ibov, start6, end6)['Adj Close']
df_2018 = pd.DataFrame(ibov_2018)
df_2018['retorno'] = ibov_2018.pct_change().iloc[1:]
ibov_2018_returns = df_2018['retorno']
ibov_2018_returns = ibov_2018_returns.fillna(0)
ibov_2018_cumulative = (1000 * (1 + ibov_2018_returns).cumprod())
peaks_2018 = ibov_2018_cumulative.cummax()
df_2018['drawdown'] = (ibov_2018_cumulative - peaks_2018) / peaks_2018
drawdown_2018 = df_2018['drawdown']
max_drawdown_2018 =(df_2018['drawdown'].min())*-100
max_drawdown_2018 = str(round(max_drawdown_2018, 2))

ibov_2022 = yf.download(ibov, start7, end7)['Adj Close']
df_2022 = pd.DataFrame(ibov_2022)
df_2022['retorno'] = ibov_2022.pct_change().iloc[1:]
ibov_2022_returns = df_2022['retorno']
ibov_2022_returns = ibov_2022_returns.fillna(0)
ibov_2022_cumulative = (1000 * (1 + ibov_2022_returns).cumprod())
peaks_2022 = ibov_2022_cumulative.cummax()
df_2022['drawdown'] = (ibov_2022_cumulative - peaks_2022) / peaks_2022
drawdown_2022 = df_2022['drawdown']
max_drawdown_2022 =(df_2022['drawdown'].min())*-100
max_drawdown_2022 = str(round(max_drawdown_2022, 2))

fig = make_subplots(rows = 2, cols = 4)

trace0 = go.Scatter(y = drawdown_1998, name = 'Ibov-1998', fill='tonexty')
trace1 = go.Scatter(y = drawdown_2002, name = 'Ibov-2002', fill='tonexty')
trace2 = go.Scatter(y = drawdown_2006, name = 'Ibov-2006', fill='tonexty')
trace3 = go.Scatter(y = drawdown_2010, name = 'Ibov-2010', fill='tonexty')
trace4 = go.Scatter(y = drawdown_2014, name = 'Ibov-2014', fill='tonexty')
trace5 = go.Scatter(y = drawdown_2018, name = 'Ibov-2018', fill='tonexty')
trace6 = go.Scatter(y = drawdown_2022, name = 'Ibov-2022', fill='tonexty')

fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 2)
fig.append_trace(trace2, 1, 3)
fig.append_trace(trace3, 1, 4)
fig.append_trace(trace4, 2, 1)
fig.append_trace(trace5, 2, 2)
fig.append_trace(trace6, 2, 3)

fig.update_layout(title = 'Drawdown Ibov - Election Years', xaxis = dict(title = 'Max Drawdown Ibov 1998: ' 
                                                               + '-' + max_drawdown_1998 + '%'), 
                  xaxis2 = dict(title = 'Max Drawdown Ibov 2002: ' + '-' + max_drawdown_2002 + '%'),
                  xaxis3 = dict(title = 'Max Drawdown Ibov 2006: ' + '-' + max_drawdown_2006 + '%'), 
                  xaxis4 = dict(title = 'Max Drawdown Ibov 2010: ' + '-' + max_drawdown_2010 + '%'),
                  xaxis5 = dict(title = 'Max Drawdown Ibov 2014: ' + '-' + max_drawdown_2014 + '%'),
                  xaxis6 = dict(title = 'Max Drawdown Ibov 2018: ' + '-' + max_drawdown_2018 + '%'),
                  xaxis7 = dict(title = 'Max Drawdown Ibov 2022: ' + '-' + max_drawdown_2022 + '%'))

fig.show()
