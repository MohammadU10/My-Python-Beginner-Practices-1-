
# 1. Sorting Lists :

# 1.1. sorted() and sort() Functions :
# li = [5, 8, 2, 4, 3, 9, 1, 6, 7]

""" s_li = sorted(li)

# Print Sorted Version of the List:
print('Sorted Variable:\t', s_li)
# Print Original Version of the List:
print('Original Variable:\t', li) """

# We can use sort() Function to Sort the Original List, Without Creating a New Variable :
""" li.sort()
print('Original Variable:\t', li) """

# * One Difference Between sorted() And sort() is that the sorted() Funtion, Returns a New Sorted List, that's Why we can set it to a Variable;
# But the sort() Method, just Sorts the List In Place and then Returns 'None'.*


# 1.2. How to Sort Lists in Descending Order (From Highest to Lowest) :
""" s_li = sorted(li, reverse=True)

print('Sorted Variable:\t', s_li)

li.sort(reverse=True)

print('Original Variable:\t', li) """



# 2. Why we Choose the sorted() Over the sort() Method :

# The sorted() Function gives us more Flexibility,
# Because we can Pass in any iterable, as opposed to sort() Method which works Specifically on Lists; For Example :
""" tup = (5, 8, 2, 4, 3, 9, 1, 6, 7)
# Tuples Don't have the sort() Method :
# tup.sort()

# So we have to use the sort() Function :
s_tup = sorted(tup)

print('Tuple:\t', s_tup) """


# You can Pass in a Dictionary into sorted() Also :
""" di = {'name': 'Muhammad', 'job': 'programming', 'age': None, 'os': 'Windows'}

s_di = sorted(di)

print('Dict:\t', s_di) """


# * For the rest of this File, we gonna use the sorted() Function,
# Because we gonna be working with Examples other than Lists.



# 3. How to Sort Values Based on a Different Criteria :

# 3.1. How to Sort Integers Based on their Absolute Value :
""" li = [-6, -5, -4, 1, 2, 3]

s_li = sorted(li)

print(s_li) """
# If we run this, we get the exact Same Values in it;

# What if we wanted to Sort the List Based on the Absolute Value of these Values :
""" li = [-6, -5, -4, 1, 2, 3]

s_li = sorted(li, key=abs)

print(s_li) """


# 3.2. 'key' Parameter is Extremely Useful When you are Sorting Objects with Named Attributes :
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

# 3 Sample Employees :
e1 = Employee('Muhammad', 20, 100000)
e2 = Employee('Carl', 28, 90000)
e3 = Employee('John', 42, 80000)

# Put all 3 Employees in a List:
employees = [e1, e2, e3]

# Now we gonna try to Sort these Based on its Specific Attribute :
""" s_employees = sorted(employees)

print(s_employees) """
# So if we try to Sort these without a 'key', Then its not really gonna know How to Sort them;
# So it's getting the 'Employee' Object here from the List,
# And it's saying: "Hey, I Don't know How you want me to Sort these."

# So we need to use a 'key' to Sort these on, And we gonna Write a Custom Funtion in order to Sort them;
# So Remember that our 'key' takes a Function that takes Each Element of our List And Returns What we want to Sort on;
# So with the Absolute Value Example that we used earlier, We were able to use a Built-in Function for the 'key',
# But for this Example, we need to Write a Custom Funtion :
""" def e_sort(emp):
    return emp.name

s_employees = sorted(employees, key=e_sort)

print(s_employees) """
# If we run this, it Returns All of our Employees Based on their 'name'.

# Now if we wanted to Sort these Based on the Employee's Age :
""" def e_sort(emp):
    return emp.age

s_employees = sorted(employees, key=e_sort)

print(s_employees) """

# Also if we wanted to Sort these Based on the Employee's Salary :
""" def e_sort(emp):
    return emp.salary

s_employees = sorted(employees, key=e_sort)

print(s_employees) """

# We can Also Still Pass in other Parameters in the sorted(), such as 'reverse=' :
""" def e_sort(emp):
    return emp.salary

s_employees = sorted(employees, key=e_sort, reverse=True)

print(s_employees) """


# Now if you have a Complicated Sort Function, it's probably best to Break out these Functions into Separate Functions like this,
# But if you are Familiar with 'lambda' Functions, Then you probably noticed that something this Short would we Easy to turn into a 'lambda' Function;
# So Instead :

# 'lambda' Functions are just Way to Quickly Write an Anonymous Function:
""" s_employees = sorted(employees, key=lambda e: e.name)

print(s_employees) """

# Also you should Mention that if you are working with Attributes like this,
# Then you Can import a Function that Specifically does this :
from operator import attrgetter

# We can use this as a Replacement for our 'key' :
s_employees = sorted(employees, key=attrgetter('age'))

print(s_employees)