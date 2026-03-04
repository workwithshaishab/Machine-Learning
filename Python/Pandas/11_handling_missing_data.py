import pandas as pd
emp_data= {
    "Name": ['Ram', None, 'Sudip','Ramesh','Ganesh'],
    "Age": [21, 22, 21, 24, None],
    "City": ["Kathmandu", "Pokhara", None, "Kavre", "Surkhet"],
    "Salary":[None, 38000, 25000, 80000, 95000]
}

df= pd.DataFrame(emp_data)
print(df)

print(df.isnull())  # true means missing values and false means not missing.
print(df.isnull().sum())  # return number of missing values in each column.

