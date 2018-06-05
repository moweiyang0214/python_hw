import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
# def create_df(list):
#   return pd.DataFrame(list)
listDji=['MMM','AXP','AAPL','BA','CAT','CVX','CSCO','KO','DIS','DD']
listTemp = [0]* len(listDji)
for i in range(len(listTemp)):
  listTemp[i] = create_df(listDji[i]).close
status = [0]* len(listDji)
for i in range(len(status)): 
  status[i]= np.sign(np.diff(listTemp[i]))
kmeans= KMeans(n_cluster=3).fit(status)
pred = kmeans.predict(status)
print(pred)
