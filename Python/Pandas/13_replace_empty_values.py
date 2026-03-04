import pandas as pd
emp_data= {
    "Name": ['Ram', None, 'Sudip','Ramesh','Ganesh'],
    "Age": [21, 22, 21, 24, None],
    "City": ["Kathmandu", "Pokhara", None, "Kavre", "Surkhet"],
    "Salary":[None, 38000, 25000, 80000, 95000]
}

df= pd.DataFrame(emp_data)
print(df)

#replace null values with something
"""
    df.fillna(111, inplace= True)
    print(df)
"""
#replace for specified colum
df["Age"].fillna(df["Age"].mean(), inplace=True)
print(df)