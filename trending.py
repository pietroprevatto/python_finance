from pytrends.request import TrendReq
import numpy as np

pytrends = TrendReq(hl = 'en-US')

all_keywords = ['Cryptocurrency', 'Blockchain', 'Metaverse', 'DeFi' , 'Web3']
keywords = []

timeframes = ['today 5-y', 'today 12-m', 'today 3-m', 'today 1-m']
cat = '0'
geo = ''
gprop = ''

def check_trends():
  pytrends.build_payload(keywords, cat, timeframes[0], geo, gprop)
  data = pytrends.interest_over_time()
  mean = round(data.mean(),2)
  avg = round(data[kw][-52:].mean(),2)
  avg2 = round(data[kw][:52].mean(),2)
  trend = round(((avg/mean[kw])-1)*100,2)
  trend2 = round(((avg/avg2)-1)*100, 2)
  print('The average 5 years interest of ' + kw + ' was ' + str(mean[kw]) + '.')
  print('The last year interest of ' + kw + ' compared to the last 5 years' + ' has changed by ' + str(trend) + '%.')

  if mean[kw] > 75 and abs(trend)<=5:
    print('The interest for ' + kw + ' is stable in the last 5 years.')
  elif mean[kw] > 75 and trend > 5:
    print('The interest for ' + kw + ' is stable and increasing in the last 5 years.')
  elif mean[kw] > 75 and trend < -5:
    print('The interest for ' + kw + ' is stable and decreasing in the last 5 years.')
  elif mean[kw] > 60 and abs(trend) <= 15:
    print('The interest for ' + kw + ' is relatively stable in the last 5 years.')
  elif mean[kw] > 60 and trend > 15:
    print('The interest for ' + kw + ' is relatively stable and increasing in the last 5 years.')
  elif mean[kw] > 60 and trend < -15:
    print('The interest for ' + kw + ' is relatively stable and decreasing in the last 5 years.')
  elif mean[kw] > 20 and abs(trend) <= 15:
    print('The interest for ' + kw + ' is seasonal.')
  elif mean[kw] > 20 and trend > 15:
    print('The interest for ' + kw + ' is trending.')
  elif mean[kw] > 20 and trend < -15:
    print('The interest for ' + kw + ' is significantly decreasing.')
  elif mean[kw] > 5 and abs(trend) <= 15:
    print('The interest for ' + kw + ' is cyclical.')
  elif mean[kw] > 0 and trend > 15:
    print('The interest for ' + kw + ' is new and trending.')
  elif mean[kw] > 0 and trend < -15:
    print('The interest for ' + kw + ' is decreasing and not comparable to its peak.')
  else:
    print('This is something to be checked.')
  
  if avg2 == 0:
    print("This didn't exist 5 years ago.")
  
  elif trend2 > 15:
    print('The last year interest is quite higher compared to 5 years ago.' + ' It has increased by ' + str(trend2) + '%.') 
  elif trend2 < 15:
    print('The last year interest is quite lower compared to 5 years ago.' + ' It has decreased by ' + str(trend2) + '%.') 
  else:
    print('The last year interest is comparable to 5 years ago.' + ' It has changed by ' + str(trend2) + '%.')
  
  print('')
  
for kw in all_keywords:
  keywords.append(kw)
  check_trends()
  keywords.pop()

