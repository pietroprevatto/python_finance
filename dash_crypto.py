import streamlit as st
import pandas as pd
import pandas_datareader as web
import seaborn as sns
import datetime as dt

cryptos = ('BTC-USD', 'ETH-USD', 'ADA-USD', 'SOL-USD', 'LUNA1-USD', 'AVAX-USD', 'FTM-USD', 'DOT-USD')



st.markdown('''# **Crypto Dashboard**
Simple cryptocurrency app using Binance API
''')

st.header('**Crypto Prices**')

df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 3))
    return a

col1, col2, col3, col4 = st.columns(4)

col1_selection = st.sidebar.selectbox('Crypto1', df.symbol, list(df.symbol).index('BTCUSDT'))
col2_selection = st.sidebar.selectbox('Crypto2', df.symbol, list(df.symbol).index('ETHUSDT'))
col3_selection = st.sidebar.selectbox('Crypto3', df.symbol, list(df.symbol).index('ADAUSDT'))
col4_selection = st.sidebar.selectbox('Crypto4', df.symbol, list(df.symbol).index('SOLUSDT'))
col5_selection = st.sidebar.selectbox('Crypto5', df.symbol, list(df.symbol).index('LUNAUSDT'))
col6_selection = st.sidebar.selectbox('Crypto6', df.symbol, list(df.symbol).index('AVAXUSDT'))
col7_selection = st.sidebar.selectbox('Crypto7', df.symbol, list(df.symbol).index('FTMUSDT'))
col8_selection = st.sidebar.selectbox('Crypto8', df.symbol, list(df.symbol).index('DOTUSDT'))

col1_df = df[df.symbol == col1_selection]
col2_df = df[df.symbol == col2_selection]
col3_df = df[df.symbol == col3_selection]
col4_df = df[df.symbol == col4_selection]
col5_df = df[df.symbol == col5_selection]
col6_df = df[df.symbol == col6_selection]
col7_df = df[df.symbol == col7_selection]
col8_df = df[df.symbol == col8_selection]

col1_price = round_value(col1_df.weightedAvgPrice)
col2_price = round_value(col2_df.weightedAvgPrice)
col3_price = round_value(col3_df.weightedAvgPrice)
col4_price = round_value(col4_df.weightedAvgPrice)
col5_price = round_value(col5_df.weightedAvgPrice)
col6_price = round_value(col6_df.weightedAvgPrice)
col7_price = round_value(col7_df.weightedAvgPrice)
col8_price = round_value(col8_df.weightedAvgPrice)

col1_percent = f'{float(col1_df.priceChangePercent)}%'
col2_percent = f'{float(col2_df.priceChangePercent)}%'
col3_percent = f'{float(col3_df.priceChangePercent)}%'
col4_percent = f'{float(col4_df.priceChangePercent)}%'
col5_percent = f'{float(col5_df.priceChangePercent)}%'
col6_percent = f'{float(col6_df.priceChangePercent)}%'
col7_percent = f'{float(col7_df.priceChangePercent)}%'
col8_percent = f'{float(col8_df.priceChangePercent)}%'

col1.metric(col1_selection, col1_price, col1_percent)
col2.metric(col2_selection, col2_price, col2_percent)
col3.metric(col3_selection, col3_price, col3_percent)
col4.metric(col4_selection, col4_price, col4_percent)
col1.metric(col5_selection, col5_price, col5_percent)
col2.metric(col6_selection, col6_price, col6_percent)
col3.metric(col7_selection, col7_price, col7_percent)
col4.metric(col8_selection, col8_price, col8_percent)

st.header('**All Infos**')
st.dataframe(df)

st.header('**Comparison**')
dropdown = st.multiselect('Pick your crypto', cryptos)

st.info('Created by Pietro Prevatto')


