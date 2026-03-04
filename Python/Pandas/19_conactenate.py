import pandas as pd
data1= {
    "ID": [1,2],
    "Name": ["Ram", "Shyam"]
}
df1= pd.DataFrame(data1)

data2= {
    "ID": [3,4],
    "Name": ["Ramesh", "Ghanashyam"]
}
df2= pd.DataFrame(data2)

# vertically
concat= pd.concat((df1,df2), axis=0, ignore_index=True)
print(concat)

# horizontally
concat= pd.concat((df1,df2), axis=1, ignore_index=True)
print(concat)


