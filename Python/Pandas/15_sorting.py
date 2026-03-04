import pandas as pd
emp_data= {
    "Name": ['Ram', 'Sita', 'Sudip','Ramesh','Ganesh'],
    "Age": [21, 22, 21, 24, 26],
    "City": ["Kathmandu", "Pokhara", "Butwal", "Kavre", "Surkhet"],
    "Salary":[55000,38000,25000,80000,95000]
}

df= pd.DataFrame(emp_data)

# sorting only one values
df.sort_values(by="Age", ascending= True, inplace=True)
print(df)

# sorting multiple values
df.sort_values(by=["Name", "Salary"], ascending= [True, False], inplace=True)
print(df)
