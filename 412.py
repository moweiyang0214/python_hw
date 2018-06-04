import pandas as pd
fruit_df = pd.Series(['apple','orange', 'pear'], index=[0,2,5])
fruit_df = fruit_df.reindex(range(7))
# ffill表示用后一个数据代替NaN填充，而bfill表示用前一个数据代替NaN填充，请选择如下填充方式正确的结果。
fruit_df.fillna(method='ffill', inplace= True)
print(fruit_df)