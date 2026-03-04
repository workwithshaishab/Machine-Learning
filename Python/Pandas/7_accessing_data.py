import pandas as pd
emp_data = {
    "Name": ['Ram', 'Sita', 'Sudip','Ramesh','Ganesh'],
    "Age": [21, 22, 21, 24, 26],
    "City": ["Kathmandu", "Pokhara", "Butwal", "Kavre", "Surkhet"],
    "Salary":[55000,38000,25000,80000,95000]
}
df= pd.DataFrame(emp_data)
print(df)

# Accessing names
print(df["Name"])

# Selecting multiple columns
print(df[["Name", "Salary"]])


# Employee with salary greater han 60000
cond1= df[df["Salary"]>60000]
print("Employee with salary greater than 60000\n", cond1)


# Employee with salary greater than 60000 and age more than 25
cond2= df[(df["Salary"]>60000) & (df["Age"]>25)]
print("Employee with salary greater than 60000 and age more than 25:\n", cond2)

# Employee with salary greater than 60000 or age more than 21
cond2= df[(df["Salary"]>60000) | (df["Age"]>21)]
print("Employee with salary greater than 60000 and age more than 21:\n", cond2)
