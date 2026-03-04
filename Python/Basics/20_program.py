phone= input("Phone:")
digit_inword={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}

output="" #to print in one line
for ch in phone:
    output+=digit_inword.get(ch, "Not in dictionary!!")+" "
print(output)


#if not
"""
for ch in phone:
    print(digit_inword.get(ch,"Not in dictionary!!"))
"""