#Write a program to find the largest number from lists
num=[1,5,3,7,6]
max=num[0]
for i in range(1,len(num)):
        if num[i]>max:
            max= num[i]
print("Largest=", max)


#another method (easy one)
"""
    num=[1,5,3,7,6]
    max=num[0]
    for n in num:
        if n>max:
            max=n
    print("Largest=", max)
"""