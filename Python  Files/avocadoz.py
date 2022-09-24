import pandas as pd
import quandl
import matplotlib
import time

avocado_data = 'Datasets/avocado.csv'
df = pd.read_csv(avocado_data)

sorted_price = (df['AveragePrice']).sort_values()
price_by_year = (df[['year', 'AveragePrice']])
print(price_by_year.head(5), "\n")


df_albany = df[ df['region'] == 'Albany' ]
df_albany.set_index('Date', inplace = True)
print(df_albany.head(), "\n")

# Prints out every unique value from the specified column
print(df['region'].unique())



'''

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['High Low Percent'] = round((df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0, 2)
df['Percent change in stock'] = round((df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0, 2)

df = df[['Adj. Close', 'High Low Percent', 'Percent change in stock', 'Adj. Volume']]
print(df.head(5))

'''

