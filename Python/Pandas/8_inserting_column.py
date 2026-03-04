import pandas as pd
emp_data = {
    "Name": ['Ram', 'Sita', 'Sudip','Ramesh','Ganesh'],
    "Age": [21, 22, 21, 24, 26],
    "City": ["Kathmandu", "Pokhara", "Butwal", "Kavre", "Surkhet"],
    "Salary":[55000,38000,25000,80000,95000]
}

df= pd.DataFrame(emp_data)
print(df)


# 1st method=> We cannot insert the column in our preferred position
df["bonus"]= df["Salary"]*0.1
print(df)

# 2nd method=> We can insert column in our preferred position
df.insert(0, "Employee ID", [1,2,3,4,5])
print(df)