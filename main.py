import pandas as pd
import quandl
quandl.ApiConfig.api_key = "o25QNDvSXrTmhzw8fpHv"
df = quandl.get('WIKI/GOOGL')


df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HC_PTL'] = (df['Adj. High'] - df['Adj. High']) / df['Adj. Close'] *100.0
df['PCT_Change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] *100.0

df = df[['Adj. Close','Adj. High','HC_PTL','PCT_Change','Adj. Volume']]
print(df.head())

print('all done')
print('dsa')



