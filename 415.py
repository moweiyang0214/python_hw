import pandas as pd
import numpy as np
index_df = pd.DataFrame(np.random.randn(3,3), index=['a','b','c'], columns=['index_1','index_2','index_3'])
print(index_df.describe())
# 即为index_df.corr(method = 'pearson')，另也可用method='spearman'等
print(index_df.corr())