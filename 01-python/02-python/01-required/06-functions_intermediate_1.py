# randInt() returns a random integer between 0 to 100

def uptohundred():
    import random
    print(random.random()*100)

uptohundred()

# randInt(max=50) returns a random integer between 0 to 50

def uptofifty():
    import random
    print(random.random()*50)

uptofifty()

# randInt(min=50) returns a random integer between 50 to 100

def fiftytohundred():
    import random
    print(random.randrange(50,100))

fiftytohundred()

# randInt(min=50, max=500) returns a random integer between 50 and 500

def fiftytofivehundred():
    import random
    print(random.randrange(50,500))

fiftytofivehundred()