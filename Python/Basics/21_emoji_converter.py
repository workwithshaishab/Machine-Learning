msg=input("Type what you feel:")
words= msg.split(' ')
emoji={
    ":)":"😄",
    ":(":"😔",
    ";)":"😉"
}

output=""
for word in words:
    output+= emoji.get(word,word)+" "
    """
    emoji.get(word, word) looks up word in the emoji dictionary. 
    If found, it returns the emoji (e.g. ":)" -> "😄"); 
    if not found, it returns the original word.
    """
print(output)