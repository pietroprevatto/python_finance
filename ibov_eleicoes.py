import yfinance as yf
import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default ='browser'

ibov = yf.download('^BVSP', start = '1995-01-01')[['Adj Close']]
df = ibov.copy()

df['Year'] = df.index.year
df['Days'] = df.index.dayofyear

table = df.pivot(index = 'Days', columns = 'Year', values = 'Adj Close')
table = table.fillna(method = 'bfill')
table = (table/table.iloc[0]) - 1

anos_eleitorais = [1998, 2002, 2006, 2010, 2014, 2018]

fig = px.line(
    table[anos_eleitorais],
    height = 600,
    width = 800,
    title = 'IBOV Election Years',
    labels = {'value':'Returns'}  
)


fig.update_traces(line = dict(width = 0.7))
fig.add_scatter(x = table.index, y = table[2022], name = '2022', line = dict(width = 3.5))

fig.add_vline(x = pd.to_datetime('2022-10-01').dayofyear)
fig.add_vline(x = pd.to_datetime('2022-10-31').dayofyear)
fig.layout.yaxis.tickformat = '.0%'

fig.show()
