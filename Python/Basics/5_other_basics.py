course='Python for beginners'
print(course[0])
print(course[5])
print(course[-1])
print(course[-3])
print(course[0:8])
print(course[5:]) #starts from 5th character
print(course[:8]) #same as 0:8
print(course[1:-1])
msg= f"Course of {course}"  #In Python, f is used for f-strings (formatted string literals).
                            #It allows you to directly insert variables or expressions inside a string using {}.
print(msg)
print("Length=", len(course))