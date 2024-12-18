import pandas as pd
import numpy as np

dates = pd.date_range(start='2022-07-26', periods=10, freq='D')

values = np.random.rand(10)

df = pd.DataFrame({'Dates': dates, 'Value': values})

df.set_index('Dates', inplace=True)

print(df)


month = df.resample('M').mean()

print(month)