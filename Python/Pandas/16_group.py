import pandas as pd
emp_data= {
    "Name": ['Ram', 'Sita', 'Sudip','Ramesh','Ganesh','Ram'],
    "Age": [21, 22, 21, 24, 26, 21],
    "City": ["Kathmandu", "Pokhara", "Butwal", "Kavre", "Surkhet","Kathmandu"],
    "Salary":[55000,38000,25000,80000,95000,70000]
}

df= pd.DataFrame(emp_data)
grouped1= df.groupby("Age")["Salary"].sum()   # sum of salary of particular age group  # same age ko aadhar maa total salary nikaleko
print(grouped1)

grouped2= df.groupby(["Age", "Name"])["Salary"].sum()  # same age ra same name ko sum  of total salary
print(grouped2)
