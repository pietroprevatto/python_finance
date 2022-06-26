import yfinance as yf
import datetime as dt
import pandas as pd
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
df_1999 = pd.DataFrame(ibov_1999)
df_1999['retorno'] = ibov_1999.pct_change().iloc[1:]
ibov_1999_returns = df_1999['retorno']
ibov_1999_returns = ibov_1999_returns.fillna(0)
ibov_1999_cumulative = (1000 * (1 + ibov_1999_returns).cumprod())
peaks_1999 = ibov_1999_cumulative.cummax()
df_1999['drawdown'] = (ibov_1999_cumulative - peaks_1999) / peaks_1999
drawdown_1999 = df_1999['drawdown']
max_drawdown_1999 =(df_1999['drawdown'].min())*-100
max_drawdown_1999 = str(round(max_drawdown_1999, 2))

ibov_2003 = yf.download(ibov, start2, end2)['Adj Close']
df_2003 = pd.DataFrame(ibov_2003)
df_2003['retorno'] = ibov_2003.pct_change().iloc[1:]
ibov_2003_returns = df_2003['retorno']
ibov_2003_returns = ibov_2003_returns.fillna(0)
ibov_2003_cumulative = (1000 * (1 + ibov_2003_returns).cumprod())
peaks_2003 = ibov_2003_cumulative.cummax()
df_2003['drawdown'] = (ibov_2003_cumulative - peaks_2003) / peaks_2003
drawdown_2003 = df_2003['drawdown']
max_drawdown_2003 =(df_2003['drawdown'].min())*-100
max_drawdown_2003 = str(round(max_drawdown_2003, 2))

ibov_2007 = yf.download(ibov, start3, end3)['Adj Close']
df_2007 = pd.DataFrame(ibov_2007)
df_2007['retorno'] = ibov_2007.pct_change().iloc[1:]
ibov_2007_returns = df_2007['retorno']
ibov_2007_returns = ibov_2007_returns.fillna(0)
ibov_2007_cumulative = (1000 * (1 + ibov_2007_returns).cumprod())
peaks_2007 = ibov_2007_cumulative.cummax()
df_2007['drawdown'] = (ibov_2007_cumulative - peaks_2007) / peaks_2007
drawdown_2007 = df_2007['drawdown']
max_drawdown_2007 =(df_2007['drawdown'].min())*-100
max_drawdown_2007 = str(round(max_drawdown_2007, 2))

ibov_2011 = yf.download(ibov, start4, end4)['Adj Close']
df_2011 = pd.DataFrame(ibov_2011)
df_2011['retorno'] = ibov_2011.pct_change().iloc[1:]
ibov_2011_returns = df_2011['retorno']
ibov_2011_returns = ibov_2011_returns.fillna(0)
ibov_2011_cumulative = (1000 * (1 + ibov_2011_returns).cumprod())
peaks_2011 = ibov_2011_cumulative.cummax()
df_2011['drawdown'] = (ibov_2011_cumulative - peaks_2011) / peaks_2011
drawdown_2011 = df_2011['drawdown']
max_drawdown_2011 =(df_2011['drawdown'].min())*-100
max_drawdown_2011 = str(round(max_drawdown_2011, 2))

ibov_2015 = yf.download(ibov, start5, end5)['Adj Close']
df_2015 = pd.DataFrame(ibov_2015)
df_2015['retorno'] = ibov_2015.pct_change().iloc[1:]
ibov_2015_returns = df_2015['retorno']
ibov_2015_returns = ibov_2015_returns.fillna(0)
ibov_2015_cumulative = (1000 * (1 + ibov_2015_returns).cumprod())
peaks_2015 = ibov_2015_cumulative.cummax()
df_2015['drawdown'] = (ibov_2015_cumulative - peaks_2015) / peaks_2015
drawdown_2015 = df_2015['drawdown']
max_drawdown_2015 =(df_2015['drawdown'].min())*-100
max_drawdown_2015 = str(round(max_drawdown_2015, 2))

ibov_2019 = yf.download(ibov, start6, end6)['Adj Close']
df_2019 = pd.DataFrame(ibov_2019)
df_2019['retorno'] = ibov_2019.pct_change().iloc[1:]
ibov_2019_returns = df_2019['retorno']
ibov_2019_returns = ibov_2019_returns.fillna(0)
ibov_2019_cumulative = (1000 * (1 + ibov_2019_returns).cumprod())
peaks_2019 = ibov_2019_cumulative.cummax()
df_2019['drawdown'] = (ibov_2019_cumulative - peaks_2019) / peaks_2019
drawdown_2019 = df_2019['drawdown']
max_drawdown_2019 =(df_2019['drawdown'].min())*-100
max_drawdown_2019 = str(round(max_drawdown_2019, 2))

fig = make_subplots(rows = 2, cols = 3)

trace0 = go.Scatter(y = drawdown_1999, name = 'Ibov-1999', fill='tonexty')
trace1 = go.Scatter(y = drawdown_2003, name = 'Ibov-2003', fill='tonexty')
trace2 = go.Scatter(y = drawdown_2007, name = 'Ibov-2007', fill='tonexty')
trace3 = go.Scatter(y = drawdown_2011, name = 'Ibov-2011', fill='tonexty')
trace4 = go.Scatter(y = drawdown_2015, name = 'Ibov-2015', fill='tonexty')
trace5 = go.Scatter(y = drawdown_2019, name = 'Ibov-2019', fill='tonexty')

fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 2)
fig.append_trace(trace2, 1, 3)
fig.append_trace(trace3, 2, 1)
fig.append_trace(trace4, 2, 2)
fig.append_trace(trace5, 2, 3)

fig.update_layout(title = 'Drawdown Ibov - 1Y After Elections', xaxis = dict(title = 'Max Drawdown Ibov 1999: ' 
                                                               + '-' + max_drawdown_1999 + '%'), 
                  xaxis2 = dict(title = 'Max Drawdown Ibov 2003: ' + '-' + max_drawdown_2003 + '%'),
                  xaxis3 = dict(title = 'Max Drawdown Ibov 2007: ' + '-' + max_drawdown_2007 + '%'), 
                  xaxis4 = dict(title = 'Max Drawdown Ibov 2011: ' + '-' + max_drawdown_2011 + '%'),
                  xaxis5 = dict(title = 'Max Drawdown Ibov 2015: ' + '-' + max_drawdown_2015 + '%'),
                  xaxis6 = dict(title = 'Max Drawdown Ibov 2019: ' + '-' + max_drawdown_2019 + '%'))

fig.show()
