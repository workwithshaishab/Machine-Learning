try:
    num= int(input('Enter a number:'))
    division= 2000/num

except ZeroDivisionError:
    print("Number cant be divide by zero")
except ValueError:
    print("Invalid value")