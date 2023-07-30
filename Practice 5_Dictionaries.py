
"""  # 1. How to Define a Dictionary :

# dictionary = {'((Key))': '((Value))'}
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student) """



""" # 2. How to get a Value of One Key :
print(student['name'])
print(student['age'])
print(student['courses']) """



""" # 3. Keys can be any type of Immutable Data Type :

student = {1: 'John', 2.5: 25, 'C': ['Math', 'CompSci']}
print(student[1])
print(student[2.5])
print(student['C']) """



""" # 4. What Happens if we try to Access a Key that Doesn't Exist :

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student['phone'])


# By Default, get() Method returns 'None' if we try to Access a Key that Doesn't Exist:
print(student.get('name'))

print(student.get('phone'))


# Also, We Can Specify a Default Value for Keys that Don't Exist by Passing a Default Value as a Second Argument to get():
print(student.get('phone', 'Not Found')) """



""" # 5. How to Add a new Entry to our Dictionary :

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student['phone'] = '913-1234'

print(student.get('phone'), '\n')


# If a Key Already Exists, it will Update the Value of the Key:
student['name'] = 'Tom'

print(student, '\n')


# Also We can use update() Method to Update Multiple Values At a Time:
# It takes in a Dictionary as an Argument:
student.update({'name': 'Jane', 'age': 30, 'phone': '555-4321'})

print(student) """



# 6. How to Delete a Specific Key and its Value :

# student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}


""" # 6.1. "del" Keyword :
del student['age']

print(student) """


""" # 6.2. pop() Method :
# the pop() method will Remove, but also Return that Value.
# So that allows to Grab the Removed Value with a Variable.
age = student.pop('age')

print(student)
print(age) """



""" # 7. How to Loop through all the Keys & Values of our Dictionary:

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}


# 7.1. How many Keys are in our Dictionary :
print(len(student), '\n')


# 7.2. How to see all of the Keys :
print(student.keys(), '\n')


# 7.3. How to see all of the Values :
print(student.values(), '\n')


# 7.4. How to see the Keys And Values:
print(student.items(), '\n')


# 7.5. How to Loop through all of the Keys & Values :

# 1. If we Loop through our Dictionary Without using any Method, it will just Loop through the keys :
for key in student:
    print(key)
print('\n')


# 2. In Order to Loop through the Keys & Values, we need to use items() Method :
for key, value in student.items():
    print(key, value) """