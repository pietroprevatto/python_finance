import pandas as pd
from neuralprophet import NeuralProphet
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

dados = pd.read_csv('C:/Users/pprev/Documents/TCC/BTC-USD.csv')
dados['Date'] = pd.to_datetime(dados['Date'])
dados = dados.fillna(method = 'bfill')

btc = dados[['Date', 'Volume']]
btc.columns = ['ds', 'y']

m = NeuralProphet(n_forecasts = 150, n_lags = 150, n_changepoints = 100, yearly_seasonality = True, weekly_seasonality = False, daily_seasonality = False,
                  batch_size = 64, epochs = 150, learning_rate = 1.5)

metrics = m.fit(btc, freq = 'D')
future = m.make_future_dataframe(btc, periods = 150, n_historic_predictions = len(btc))
prediction = m.predict(future)

forecast = m.plot(prediction)
plt.title('BTC Trading Volume Prediction - 150 days')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.show()