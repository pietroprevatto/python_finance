from pytrends.request import TrendReq
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.style.use('seaborn')

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
    
def relative_comparison():
    plt.figure(figsize = (10,8))
    x_pos = np.arange(len(all_keywords))
    pytrends.build_payload(all_keywords, cat, timeframes[0], geo, gprop)
    data = pytrends.interest_over_time()
    mean = data.mean()
    mean = round(mean / mean.max() * 100, 2)
    ax1 = plt.subplot2grid((4,2), (0,0), rowspan = 1, colspan = 1)
    ax2 = plt.subplot2grid((4,2), (0,1), rowspan = 1, colspan = 1)
    
    for kw in all_keywords:
        ax1.plot(data[kw], label = kw)
    ax2.bar(x_pos, mean, align = 'center')   
    plt.xticks(x_pos, all_keywords) 
               
    pytrends.build_payload(all_keywords, cat, timeframes[1], geo, gprop)
    data = pytrends.interest_over_time()
    mean = data.mean()
    mean = round(mean / mean.max() * 100, 2)
    ax3 = plt.subplot2grid((4,2), (1,0), rowspan = 1, colspan = 1)
    ax4 = plt.subplot2grid((4,2), (1,1), rowspan = 1, colspan = 1)
    
    for kw in all_keywords:
        ax3.plot(data[kw], label = kw)
    ax4.bar(x_pos, mean, align = 'center')   
    plt.xticks(x_pos, all_keywords) 
    
    pytrends.build_payload(all_keywords, cat, timeframes[2], geo, gprop)
    data = pytrends.interest_over_time()
    mean = data.mean()
    mean = round(mean / mean.max() * 100, 2)
    ax5 = plt.subplot2grid((4,2), (2,0), rowspan = 1, colspan = 1)
    ax6 = plt.subplot2grid((4,2), (2,1), rowspan = 1, colspan = 1)
    
    for kw in all_keywords:
        ax5.plot(data[kw], label = kw)
    ax6.bar(x_pos, mean, align = 'center')   
    plt.xticks(x_pos, all_keywords) 
    
    pytrends.build_payload(all_keywords, cat, timeframes[3], geo, gprop)
    data = pytrends.interest_over_time()
    mean = data.mean()
    mean = round(mean / mean.max() * 100, 2)
    ax7 = plt.subplot2grid((4,2), (3,0), rowspan = 1, colspan = 1)
    ax8 = plt.subplot2grid((4,2), (3,1), rowspan = 1, colspan = 1)
    
    for kw in all_keywords:
        ax7.plot(data[kw], label = kw)
    ax8.bar(x_pos, mean, align = 'center')   
    plt.xticks(x_pos, all_keywords) 
    
    ax1.set_ylabel('Last 5 years')
    ax3.set_ylabel('Last 12 months')
    ax5.set_ylabel('Last 3 months')
    ax7.set_ylabel('Last month')
    ax1.set_title('Relative interest over time', fontsize = 14)
    ax2.set_title('Relative interest for the period', fontsize = 14)
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y'))
    ax5.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y'))
    ax7.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y'))
    ax1.legend()
    ax3.legend()
    ax5.legend()
    ax7.legend()
    
    plt.show()
    
                
relative_comparison()


