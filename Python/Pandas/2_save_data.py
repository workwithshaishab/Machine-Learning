import pandas as pd

data = {
    "Name:": ['Ram', 'Sita', 'Sudip'],
    "Age:": [21, 22, 21],
    "Ciy:": ["Kathmandu", "Pokhara", "Butwal"]
}

df=pd.DataFrame(data)
print(df)
#df.to_csv("info.csv", index=False)
#df.to_csv("info.xlsx", index=False)
df.to_csv("info.json", index=False)