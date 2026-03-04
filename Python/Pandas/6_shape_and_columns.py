import pandas as pd
data = {
    "Name:": ['Ram', 'Sita', 'Sudip','Ramesh','Ganesh'],
    "Age:": [21, 22, 21,25,26],
    "City:": ["Kathmandu", "Pokhara", "Butwal", "Kavre", "Surkhet"],
    "Marks:":[97,91,86,79,81]
}
df= pd.DataFrame(data)
print(df)
print("Shape:", df.shape)
print(f"Columns: {df.columns}")