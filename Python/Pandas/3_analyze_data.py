import pandas as pd
df= pd.read_csv('data.csv')
print(df.head())   # prints first 5 data's
print(df.head(10)) # prints first 10 data's
print(df.tail())   # prints last 5 data's
print(df.tail(15)) # prints last 15 data's