import pyjokes

# Get one joke
joke = pyjokes.get_joke()
print(joke)

# Get multiple jokes (list)
jokes = pyjokes.get_jokes()
print(jokes[:3])  # print first 3 jokes
