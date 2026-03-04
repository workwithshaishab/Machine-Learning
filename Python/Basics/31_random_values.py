import random
print(random.random())
print(random.randint(1,100))
names = ["Leo", "Maya", "Arun", "Sita"]
print(random.choice(names)) 
print(random.choices(names, k=2))   # Picks 2 elements (with replacement)
print(random.sample(names, 2))      # Picks 2 unique elements (no repeats)
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print(cards)   # List order will be shuffled
