import pandas as pd
data1={
    "Customer ID":[1,2,3],
    "Name":["Ram", "Sujit", "Prajwol"]
}

df1= pd.DataFrame(data1)

data2={
    "Customer ID":[1,2,4],
    "Product":["Mouse", "Keyboard", "Monitor"]
}

df2= pd.DataFrame(data2)

# inner join
merged_df1= pd.merge(df1, df2, on="Customer ID", how="inner")
print(merged_df1)

# outer join
merged_df2= pd.merge(df1, df2, on="Customer ID", how="outer")
print(merged_df2)

# left join
merged_df3= pd.merge(df1, df2, on="Customer ID", how="left")
print(merged_df3)

# right join
merged_df4= pd.merge(df1, df2, on="Customer ID", how="right")
print(merged_df4)

# cross join
data3={
    "Customer ID":[1,2,3],
    "Name":["Ram", "Sujit", "Prajwol"]
}
df3= pd.DataFrame(data3)
df3["key"]= 1

data4={
    "Price":[1000,2000,40000],
    "Product":["Mouse", "Keyboard", "Monitor"]
}
df4= pd.DataFrame(data4)
df4["key"]= 1

merged_df5= pd.merge(df3, df4, on="key")
print(merged_df5)

