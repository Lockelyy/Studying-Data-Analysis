import pandas as pd # Uses C++ btw 
import quandl
import matplotlib
import time

avocado_data = 'Datasets/avocado.csv'
df = pd.read_csv(avocado_data)
df = df.copy()[df['type']=='organic']

# Sorting and setting index to 'Date'
df.sort_values(by='Date', ascending=True, inplace = True)
df.set_index('Date', inplace=True)

# Get rid of bag columns, bag bad
del df['Small Bags'], df['Large Bags'], df['Total Bags'], df['XLarge Bags']

print(df.head())

# Working on it...

price_by_year = (df[['year', 'AveragePrice']]).sort_values(by='AveragePrice', ascending=True)
print(price_by_year.head(5), "\n")

# Prints out every single row that has 'Albany' as the region. With 'Date' as the index.
df_albany = df[ df['region'] == 'Albany' ]
print(df_albany.head(), "\n")

# Prints out every unique value from the specified column
print(df['region'].unique())





