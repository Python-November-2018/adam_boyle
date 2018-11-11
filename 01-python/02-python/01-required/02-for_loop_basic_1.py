#1. Basic - Print all the numbers/integers from 0 to 150.

for count in range(0,151):
    print(count)

#2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.

for count in range(5,1000001,5):
    print(count)

#3. Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".

for count in range(1,101):
    if count%10==0:
        print(count,' Dojo')
    elif count%5==0:
        print('Coding')
    else:
        print(count)

#4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum = 0
for count in range(0,500001):
    if count%2==0:
        pass
    else:
        sum += count
print(sum)

#5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).

for count in range(2018,0,-4):
    if count%2==0:
        print(count)
    else:
        pass

#6. Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)

for count in range(2018,0,-4):
    lowNum = range[0]
    if count%2==0:
        print(count)
    else:
        pass


#This prints out the values of each index in the list.
list = [3,5,1,2]
for i in list:
    print(i)

3
5
1
2

#This returns an error because the list cannot be interpreted as an integer.
list = [3,5,1,2]
for i in range(list):
    print(i)

#This returns each index length, starting with <index>[0].
list = [3,5,1,2]
for i in range(len(list)):
    print(i)
    
0
1
2
3

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


test_list = [10, 20, 30]
print(ultimate_analyze(test_list))

# {
#     "sum_total": 6,
#     "average": 2,
#     "minimum": 1,
#     "maximum": 3,
#     "length": 3
# }

my_dict = {
    "name": "Wes",
    "favorite_number": 17
}

my_dict['name'] = "Adam"
my_dict["new_key"] = "new value"
