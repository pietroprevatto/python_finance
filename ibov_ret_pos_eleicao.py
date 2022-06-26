import yfinance as yf
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

anos_eleitorais = [1999, 2003, 2007, 2011, 2015, 2019]

fig = px.line(
    table[anos_eleitorais],
    height = 600,
    width = 800,
    title = 'IBOV 1Y After Election',
    labels = {'value':'Returns'}  
)

fig.update_traces(line = dict(width = 2.5))
fig.layout.yaxis.tickformat = '.0%'
fig.show()