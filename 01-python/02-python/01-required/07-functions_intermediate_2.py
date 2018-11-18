# 1. Given

x = [[5,2,3], [10,8,9]]
students = [
    {'first_name' : 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15 # Changes the value 10 in x to 15

students[0]['last_name'] = 'Bryant' # Changes the last_name of the first student from 'Jordan' to 'Bryant'

sports_directory['soccer'][0] = 'Andres' # Changes 'Messi' to 'Andres' in sports_directory

z[0]['y'] = 30 # Changes the value 20 to 30

# 2. Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.  For example, given the following list:

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names():
    i = 0
    while i < len(students):
        print('first_name -', students[i]['first_name'] + ',','last_name -', students[i]['last_name'])
        i += 1

names()

# 3. Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names():
    i = 0
    while i < len(students):
        print(students[i]['first_name'])
        i += 1

names()

#4. Say that

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# Create a function that prints the name of each location and also how many locations the Dojo currently has.  Have the function also print the name of each instructor and how many instructors the Dojo currently has.

def coding():
    i = 0
    print(len(dojo['locations']),'LOCATIONS')
    while i < len(dojo['locations']):
        print(dojo['locations'][i])
        i += 1
    print('')
    i = 0
    print(len(dojo['instructors']), 'INSTRUCTORS')
    while i < len(dojo['instructors'][i]):
        print(dojo['instructors'][i])
        i += 1

coding()