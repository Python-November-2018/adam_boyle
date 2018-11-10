def a():
    return 5
print(a())

#Prediction: 5
#Outcome: 5

def a():
    return 5
print(a()+a())

#Prediction: 10
#Outcome: 10

def a():
    return 5
    return 10
print(a())

#Prediction: 5
#Outcome: 5
#Note: This only returns 5 because the return the function stops prematurely once a 'return' is executed.

def a():
    return 5
    print(10)
print(a())

#Prediction: 5
#Outcome: 5
#Note: This only returns 5 because the return the function stops prematurely once a 'return' is executed.

def a():
    print(5)
x = a()
print(x)

#Prediction: 5
#Outcome: 5

def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

#Prediction: 3
             5
#Outcome: 3
          5
#Note: This outcome is because the function says to print(b+c) each time it's called. If it said 'return(b+c)' instead, the answer would be different.

def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#Prediction: 25
#Outcome: 25
#Note: As a string, the results are 'strung' together as one line with no seperation.

def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#Prediction: 100
             10
#Outcome: 100
          10
#Note: This function stops at 'return 10' because the return the function stops prematurely once a 'return' is executed.

def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#Prediction: 7
             14
             21
#Outcome: 7
          14
          21
#Note: The third 'print' command was not two seperate results because the term 'return' was used. If 'print' was used instead, the answer would be different.

def a(b,c):
    return b+c
    return 10
print(a(3,5))

#Prediction: 8
#Outcome: 8

b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#Prediction: 500
             500
             300
             500
#Outcome: 500
          500
          300
          500

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

#Prediction: 500
             500
             300
             500
#Outcome: 500
          500
          300
          500
#Note: The 'return b' statement in the function is not in the answer because it was returned, but never printed.

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#Prediction: 500
             500
             300
             300
#Outcome: 500
          500
          300
          300
#Note: Unlike, the previous problem, this 'return b' statement was in the answer, because it was told to be printed.

def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#Prediction: 1
             3
             2
#Outcome: 1
          3
          2

def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

#Prediction: 1
             3
             5
             10
#Outcome: 1
          3
          5
          10