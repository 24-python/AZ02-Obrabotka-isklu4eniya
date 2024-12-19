import pandas as pd

import matplotlib.pyplot as plt

data = {'Values': [1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 45, 5, 6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

#df['Values'].hist()

df.boxplot(column='Values')

plt.show()

Q1 = df['Values'].quantile(0.25)
Q3 = df['Values'].quantile(0.75)
IQR = Q3 - Q1

downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

df_new = df[(df['Values'] >= downside) & (df['Values'] <= upside)]

df_new.boxplot(column='Values')
plt.show()
