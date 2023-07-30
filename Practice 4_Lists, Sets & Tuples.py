
""" # 1. Lists :

courses = ['History', 'Math', 'Physics', 'CompSci']

# Print a List:
print(courses)

# to Print the length of a List: 
print(len(courses))

# to access each Value individually using index:
# (index of the first value starts from 0 and for the last value is: [((Total Length of List)) - 1])
print(courses[0])
print(courses[3])

# Also we can use negative indexes (a negative index starts from the end of the list):
# (the Nagative One (-1) index, will always be the last value of a list)
print(courses[-1])
print(courses[-4])

# to access a Range of Values (also called Slicing):
print(courses[0:2])

# When start of the range is from 0 index:
print(courses[:2])

# When end of the range is the last index(to print all the way to the end of the list):
print(courses[2:]) """



""" # 2. Some of the Lists Methods that allows us to Modify the List :

courses = ['History', 'Math', 'Physics', 'CompSci']


# append() to Add an Item to the End of the List:
#courses.append('Art')

#print(courses)

# insert() to Add an Item to a Specific Location in the List:
# (It takes 2 Arguments: First the Index where you want to insert the Value and Second the Value itself)
#courses.insert(0, 'Geography')

#print(courses)


# extend() to Add Multiple Values to the List:

# (If we use insert() to do such thing, we don't get the result that we actually wanted):
courses_2 = ['Art', 'Education']

courses.insert(0, courses_2)

print(courses)
print(courses[0])

# Also the same thing with append():
courses_2 = ['Art', 'Education']

courses.append(courses_2)

print(courses)
print(courses[0])

# We wanted to add all the Values from the Second List to the Original List:
# It extends each Individual Item to our List:
courses_2 = ['Art', 'Education']

courses.extend(courses_2)

print(courses)
print(courses[0]) """


""" # 3. Some ways to Remove Items(Values) from our List :

courses = ['History', 'Math', 'Physics', 'CompSci']


# remove() to Remove a Specific Value:
courses.remove('Math')

print(courses)


# pop() to Remove the Last Value of our List (by Default):
# (Useful if we have a Stack or Queue, we can keep popping off Values until our List is Empty.)
# (It also returns the value that it removed):
popped = courses.pop()

print(popped)
print(courses) """



""" # 4. Two Different Ways to Sort our List :

courses = ['History', 'Math', 'Physics', 'CompSci']


# 4.1. reverse() to Reverse our List :
courses.reverse()

print(courses)


# 4.2. sort() to sort our List :

# 1. For a List of Strings, it Sorts the List in Alphabetical Ascending Order:
courses.sort()

print(courses)

# 2. For a List of Numbers, it Sorts the List in Ascending Order (From Smallest to Largest):
nums = [0, -5, -1, -4, -3, 1, 5, 4, -2, 2, 3]

nums.sort()

print(nums)

# 3. to Sort the List in Descending Order:
courses.sort(reverse=True)
nums.sort(reverse=True)

print(courses)
print(nums)


# 4.3. sorted() Function returns a Sorted Version of the List:
# (In this Way, We can get a Sorted Version of the List without Altering the Original List.)
nums = [0, -5, -1, -4, -3, 1, 5, 4, -2, 2, 3]

sorted_courses = sorted(courses)
sorted_nums = sorted(nums, reverse=True)

print(courses)
print(nums)

print(sorted_courses)
print(sorted_nums)"""



""" # 5. Some built-in Functions we can use with Sequences (min, max & sum):

courses = ['History', 'Math', 'Physics', 'CompSci']

nums = [1, 5, 2, 4, 3]


# min() for Minimum Value of a Nums List:
print(min(nums))

# max() for Maximum Value List:
print(max(nums))

# sum() for Summation of Values:
print(sum(nums)) """



""" # 6. How to Find Some Value within our List :

courses = ['History', 'Math', 'Physics', 'CompSci']


# index() to Find the Index of a Value:
print(courses.index('Physics'))

# to Check if a Value is in our List (True or False Result):
print('Art' in courses)
print('Physics' in courses) """



""" # 7. We can use (in) to Loop through our Values by using a (for) Loop :
courses = ['History', 'Math', 'Physics', 'CompSci']

for course in courses:
    print(course)


# Also We can use enumerate() to keep track of the Index of What Value we are on:
# The enumerate() Function returns 2 Value: the Index that we are on and the Value.
for index, course in enumerate(courses):
    print(index, course)
    
# If we don't want to start at [0] index, we can pass in a Start Value to the enumerate():
for index, course in enumerate(courses, start=1):
    print(index, course) """



""" # 8. How to turn our List into Strings, Separated by a Certain Value :
courses = ['History', 'Math', 'Physics', 'CompSci']

# We use join() Method with our List as its Argument:
#course_str = ', '.join(courses)
course_str = ' - '.join(courses)
#course_str = '_'.join(courses)

print(course_str)


# Also We can use split() to turn a String back into a List:
new_list = course_str.split(' - ')

print(new_list) """



# 9. Tuples :

""" # 9.1. Lists are Mutable Objects (can be changed and modified):
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Geography'

print(list_1)
print(list_2) """


""" # 9.2 Tuples are Immutable Objects (can't be changed and modified):
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Geography'

print(tuple_1)
print(tuple_2) """



""" # 10. Sets : Sets are Values that are *UnOrdered* and have *No Duplicates*.

cs1_courses = {'History', 'Math', 'Physics', 'CompSci'}

print(cs1_courses)

cs2_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math', 'History'}

print(cs2_courses, '\n')


# Sets are More Optimized than Lists & Tuples for Membership Test of a Value:
print('Math' in cs1_courses)
print('Geography' in cs1_courses) """


""" # Something Useful that Determines What Values that Sets either Share or Don't Share with each other:
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

# intersection() to see What Values they Share:
print(cs_courses.intersection(art_courses), '\n')

# difference() to see What Values they Don't Share:
print(cs_courses.difference(art_courses), '\n')

# union() to Combine Sets:
print(cs_courses.union(art_courses)) """



# 11. How to Create Empty Lists, Tuples & Sets :

# Empty Lists:
empty_list = []
empty_list = list()

# Empty Tuples:
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets:
empty_set = {}  # --> This isn't Right! It's an Empty Dictionary.
empty_set = set()  # --> The Proper Way to Create an Empty Set.