actual_num=6
guess_count=0
limit=3

while guess_count!=limit:
    user_input= int(input("Enter a number to guess(1-10):"))
    if user_input==actual_num:
        print("Correct!!! You've guessed the number.")
        break
    else:
        guess_count+=1
        print("Please Try again.")