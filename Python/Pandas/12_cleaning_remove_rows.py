import pandas as pd
emp_data= {
    "Name": ['Ram', None, 'Sudip','Ramesh','Ganesh'],
    "Age": [21, 22, 21, 24, None],
    "City": ["Kathmandu", "Pokhara", None, "Kavre", "Surkhet"],
    "Salary":[None, 38000, 25000, 80000, 95000]
}

df= pd.DataFrame(emp_data)
print(df)

#remove rows
df.dropna(inplace=True)   #changes original value, if not written it will return new dataframe and will not change the original.
print(df)