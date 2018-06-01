import pandas as pd
import numpy as np
aSer = pd.Series([1,2.0,'a'])
data = {'name': ['wang', 'lin','liu'], 'pay': [4000,5000,6000]}
frame = pd.DataFrame(data)
print(frame)

# data2 = np.array([('wang', 4000), ('lin', 5000), ('liu', 6000)])
# frame2 = pd.DataFrame(data2, index= range(1,4), columns=['name','pay'])
# print(frame2.index)
# print(frame2.columns)
# print(frame2.values)

# print(frame['name'])
# print(frame.pay)
# print(frame.iloc[:2,1])
# frame['name'] = 'admin'
# print(frame)
# del frame['pay']
# print(frame)
print(frame.pay.min())
print(frame[frame.pay>=5000])