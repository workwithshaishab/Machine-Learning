import pandas as pd
emp_data= {
    "Name": ['Ram', 'Sita', 'Sudip','Ramesh','Ganesh'],
    "Age": [21, 22, 21, 24, 26],
    "City": ["Kathmandu", "Pokhara", "Butwal", "Kavre", "Surkhet"],
    "Salary":[55000,38000,25000,80000,95000]
}
df= pd.DataFrame(emp_data)
print(df)
df.drop(columns=["Age", "City"], inplace=True)   # modifies in same dataframe, if false it creates new dataframe
print(df)