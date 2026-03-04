add= lambda a,b: a+b
sub= lambda a,b: a-b
mul= lambda a,b: a*b
print(add(3,4))
print(sub(3,4))
print(mul(3,4))

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, numbers))
print(squares)


numbers=[10,11,12,13]
even= list(filter(lambda x:x%2==0, numbers))
print(even)