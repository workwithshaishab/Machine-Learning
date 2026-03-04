text = "   hello World 123   "

print("Original String:", repr(text))

# --- Case Methods ---
print("\n--- Case Methods ---")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Capitalize:", text.capitalize())
print("Swapcase:", text.swapcase())

# --- Search & Check Methods ---
print("\n--- Search & Check Methods ---")
print("Find 'World':", text.find("World"))
print("Index of 'hello':", text.index("hello"))
print("Count of 'l':", text.count("l"))
print("Starts with '   h':", text.startswith("   h"))
print("Ends with '123   ':", text.endswith("123   "))

# --- Check Content ---
print("\n--- Check Content ---")
print("Is Alpha (only letters):", text.isalpha())
print("Is Digit:", text.isdigit())
print("Is Alnum:", text.isalnum())
print("Is Space:", text.isspace())
print("Is Upper:", text.isupper())
print("Is Lower:", text.islower())

# --- Modify String ---
print("\n--- Modify String ---")
print("Replace 'World' with 'Python':", text.replace("World", "Python"))
print("Strip spaces:", text.strip())
print("Left Strip:", text.lstrip())
print("Right Strip:", text.rstrip())

data = "a,b,c"
print("Split by comma:", data.split(","))
print("Join with dash:", "-".join(["a", "b", "c"]))

# --- Formatting ---
print("\n--- Formatting ---")
name = "MrShJ"
age = 19
print("Using format(): My name is {} and I am {} years old".format(name, age))
print(f"Using f-string: My name is {name} and I am {age} years old")