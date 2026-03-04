import pandas as pd
emp_data= {
    "Name": ['Ram', 'Sita', 'Sudip','Ramesh','Ganesh','Ram'],
    "Age": [21, 22, 21, 24, 26, 21],
    "City": ["Kathmandu", "Pokhara", "Butwal", "Kavre", "Surkhet","Kathmandu"],
    "Salary":[55000,38000,25000,80000,95000,55000]
}

df= pd.DataFrame(emp_data)
print(df.duplicated())   # returns true if duplicated

# removing duplicates
df.drop_duplicates(inplace=True)
print(df)