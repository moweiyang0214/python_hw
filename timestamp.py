import pandas as pd
dates = pd.date_range('20170520', periods=7)
import numpy as np
datadf = pd.DataFrame(np.random.randn(7,3), index=dates, columns= list('ABC'))
print(datadf)