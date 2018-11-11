# 1. Countdown - Create a function that accepts a number as an input.  Return a new array that counts down by one, from the number (as arrays 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].

def countdown(arr):
    list = []
    for i in range(5,-1,-1):
        if i >= 0:
            list.append(i)
    return list

print(countdown(list))

# 2. Print and Return - Your function will receive an array with two numbers. Print the first value, and return the second.

def print_return(arr):
    list = [5,1]
    for i in list:
        print(i)
    return i

print_return(list)

# 3. First Plus Length - Given an array, return the sum of the first value in the array, plus the array's length.

def add_length(arr):
    list = [1,2,3,4,5]
    for i in list:
        if i <= list[0]:
            i += len(list)
            return i
        else:
            pass

add_length(list)

# 4. Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value.  Print how many values this is.  If the array is only one element long, have the function return False

def greater(arr):
    a = [1,2,3,4,5]
    list = []
    for i in a:
        if i > a[1]:
            list.append(i)
        else:
            pass
    return list

greater(list)

#5. This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size and value. This function should take two numbers and return a list of length size containing only the number in value. For example, lengthAndValue(4,7) should return [7,7,7,7].

def lengthAndValue(x,y):
    list = [y] * x
    print(list)

lengthAndValue(5,10)