## Code from stock price analyzer (utilizes quandl dataset: WIKI/GOOGL):

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['High Low Percent'] = round((df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0, 2)
df['Percent change in stock'] = round((df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0, 2)

df = df[['Adj. Close', 'High Low Percent', 'Percent change in stock', 'Adj. Volume']]
print(df.head(5))


