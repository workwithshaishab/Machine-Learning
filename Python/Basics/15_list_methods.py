# Initial list
fruits = ["apple", "banana", "cherry"]
print("Initial List:", fruits)

# 🔹 Adding Elements
fruits.append("orange")  # Add at end
print("After append:", fruits)

fruits.insert(1, "mango")  # Insert at index 1
print("After insert:", fruits)

fruits.extend(["kiwi", "grape"])  # Add multiple items
print("After extend:", fruits)

# 🔹 Removing Elements
fruits.remove("banana")  # Remove first occurrence
print("After remove:", fruits)

fruits.pop(2)  # Remove element at index 2
print("After pop:", fruits)

fruits_copy = fruits.copy()  # Copy the list
print("Copy of list:", fruits_copy)

fruits.clear()  # Remove all elements
print("After clear:", fruits)

# 🔹 Searching & Counting
numbers = [10, 20, 30, 20, 40, 50]
print("\nNumbers List:", numbers)
print("Index of 30:", numbers.index(30))
print("Count of 20:", numbers.count(20))

# 🔹 Sorting & Reversing
numbers.sort()
print("Sorted (ascending):", numbers)

numbers.sort(reverse=True)
print("Sorted (descending):", numbers)

numbers.reverse()
print("Reversed list:", numbers)

# 🔹 Other Built-in Functions
print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
