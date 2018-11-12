# 1. Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].

def return_big(arr):
    a = [-5,12,-8,20]
    list = []
    for i in a:
        if i > 0:
            list.append('big')
        else:
            list.append(i)
    return list

return_big(list)

# 2. Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

def countPositives(arr):
    list = [-1,2,-3,1,-2,1]
    a = 0
    for i in list:
        if i > 0:
            a += 1
        list[5] = a
    return list

countPositives(list)

# 3. SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10

def sumTotal(arr):
    list = [1,2,3,4,5,6]
    sum = 0
    for i in list:
        if i <= len(list):
            sum += i
    return sum

sumTotal(sum)

# 4. Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5

def average(arr):
    result = 0
    for value in arr:
        result += value / len(arr)
    return result

list = [10, 20, 30]

average(list)

# 5. Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4

def length(arr):
    a = [1,2,3,4,5,6]
    list = len(a)
    return list

length(list)

# 6. Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def minimum(arr):
    list = [1,2,3,4,5,6]
    min = 0
    for i in list:
        if i <= i:
            min = i
        else:
            pass
    return min

minimum(min)


# 7. Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def maximum(arr):
    list = [1,2,3,4,5,6]
    max = 0
    for i in list:
        if i >= i:
            max = i
        else:
            pass
    return max

maximum(max)

# 8. UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.

def ultimate_analyze(arr):
    result = {
        "sum_total": 0,
        "average": 0,
        "minimum": arr[0],
        "maximum": arr[0],
        "length": len(arr)
    }

    for value in arr:
        # find minimum
        if value < result["minimum"]:
            result['minimum'] = value
        elif value > result['maximum']:
            result['maximum'] = value
        result['sum_total'] += value
        result['average'] += value / len(arr)

    return result

list = [10, 20, 30]
print(ultimate_analyze(list))

# 9. ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

def reverse(list):
    new = []
    count = len(list)-1
    while count >= 0:
        new.append(list[count])
        count -= 1
    return new

reverse([1,2,3,4,5])