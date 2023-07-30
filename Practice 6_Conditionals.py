
""" # 1. a Simple if Statement :

if True:
    print('Conditional was True')

if False:
    print('Conditional was True') """



""" # 2. Also with an Example of a Code that Evaluates to True or False :

language = 'Python'

# We Only want to Execute the print() Statement if the language is Equal to 'Python':
if language == 'Python':
    print('Conditional was True') """



""" # 3. else Statements :

language = 'Python'

if language == 'Python':
    print('Language is Python')
else:
    print('No Match')


if language == 'Java':
    print('Language is Python')
else:
    print('No Match') """



# *Note (1): We can use different Comparisons for Conditional Statements.* :

""" # Comparison Operators :

num_1 = 3
num_2 = 2

# Equal:            ==
print(num_1 == num_2)

# Not Equal:        !=
print(num_1 != num_2)

# Greater Than:     >
print(num_1 > num_2)

# Less Than:        <
print(num_1 < num_2)

# Greater or Equal: >=
print(num_1 >= num_2)

# Less or Equal:    <=
print(num_1 <= num_2) """

# Object Identity:  is


""" # 4. elif Statements:

language = 'JavaScript'

# the elif Statements give us the same Functionality as a ((switch: case)) from another languages:
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No Match') """



# *Note (2): In Addition to the Comparisons, We also have some Boolean Operations that we can use.* :

""" # Some of Boolean Operators :

# and
# or
# not """



""" # 5. elif & if/else Statements with Boolean Operators :

user = 'Admin'
logged_in = False

# and Statement:
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')


# or Statement:
if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')


# not Statement:
if not logged_in:
    print('Please Log In')
else:
    print('Welcome') """



# 6. The Difference between '==' and 'is' Statements :

""" # Object Identity: Test if Two Objects have the same 'id': --> They are the Same Object in Memory.
# So Two Objects can actually be Equal, and Not be the Same Object in Memory, For Example:
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)


# We can Print out these Locations with built-in id() Function:
print(id(a))
print(id(b)) """


""" # If we say "b = a", they have the same id and it prints 'True', Because they are the Same Object in Memory:
a = [1, 2, 3]
b = a

print(id(a))
print(id(b), '\n')
print(a is b, '\n')
print(a == b, '\n')


# Behind the Scenes, the 'is' Comparison is same as saying:
print (id(a) == id(b)) """



""" # 7. What Python Evaluates to False :
# (Everything Else will By Default, Evaluate to True)

# False Values:

# 1. False
condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


# 2. None
condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


# 3. Zero of Any Numeric Data Type
# (0 = False, 'Any Other Number' = True)
condition = 0

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


# 4. Any Empty Sequence. For Example: '', (), [].
condition = []

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


# 5. Any Empty Mapping (Dictionary). For Example: {}.
condition = []

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


# Example for True:
condition = 'Test'

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False') """