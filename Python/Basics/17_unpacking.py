#Unpacking means assigning each element of a tuple, list, or other iterable to a separate variable in one line.

info= ["John Doe", 24, "IT Professional"]
name, age, work= info
print(name)
print(age)
print(work)

numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4] *for remaining values
print(last)    # 5


'''
    def get_person():
    return "John Doe", 19
    name, age = get_person()
    print(name, age) 

'''