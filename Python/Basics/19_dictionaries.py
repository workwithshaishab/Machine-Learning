'''
    A dictionary in Python is a collection of key-value pairs.

    Each key must be unique.
    Values can be any data type.
    Dictionaries are mutable (you can change, add, or remove items).
'''

info= {
    "name": "John Doe",
    "age":25,
    "address":"Nepal"
}

print(info["name"])
print(info.get("phone-number"))
print(info.get("phone-number", 9800000000))
info["gender"]="male"
print(info["gender"])

