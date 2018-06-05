import requests
import re
import pandas as pd

def retrieve_dji_list():
    r = requests.get('http://money.cnn.com/data/dow30/')
    search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)<\/span>')
    dji_list_in_text = re.findall(search_pattern, r.text)
    dji_list = []
    for item in dji_list_in_text:
        dji_list.append([item[0], item[1], float(item[2])])
    return dji_list

dji_list = retrieve_dji_list()
djidf = pd.DataFrame(dji_list)
cols = ['code', 'name', 'lasttrade']
djidf.columns = cols
# print(djidf)

import tushare as ts
# print(ts.get_hist_data('600848',start='2018-03-01', end='2018-03-10'))

list1 = []
for i in range(len(quotes)):
    x = date.fromtimestamp(quotes[i][ 'date'])
    y = date.strftime(x, '___________')
list1.append(y)
quotesdf_ori = pd.DataFrame(quotes, index = list1)
quotesdf = quotesdf_ori.drop(['date'], axis = ____)