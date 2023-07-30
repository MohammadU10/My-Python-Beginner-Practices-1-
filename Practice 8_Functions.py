
# 1. How to Create a Function :
# * to Create a Function, we use the 'def' Keyword (Stands for Definition).
# * the Parameters go in the Parentheses().

""" # 1.1. an Empty Function that does not do anything (We use 'pass' Keyword) :
def hello_func():
    pass

# * We need to add Parentheses After the Function in order to Execute it.
# * If we don't add Perentheses there, it is Equal to the Funtion itself:
# in the Example Below, the Output says that: "This is a Function in a Certain Location in Memory.", But it didn't Execute to it:
print(hello_func)

# to Execute it, we Add in the Parentheses:
print(hello_func()) """


""" # 1.2. a Function with some code inside :
def hello_func():
    print('Hello Function!')

hello_func() """


""" # 1.3. Keeping Your Code DRY (Don't Repeat Yourself) :
# It's a Common Mistake for people New to Programming to Repeat the Same things throughout their Code :
# One Benefit of Functions is that they allow us ro Re-Use Code Without Repeating Ourselves:

# *For Example, if we want to change the exclamation point to a normal point:
# *Instead of this:
print('Hello Function!')
print('Hello Function!')
print('Hello Function!')
print('Hello Function!')
print('\n')

# *We can use this:
def hello_func():
    print('Hello Function.')

hello_func()
hello_func()
hello_func()
hello_func()

# * Using Functions makes Manipulating and Modifying a repeated code across the Program much Easier. *
# * (When using the Function, Only 1 Change needed instead of 4 Changes.) * """



""" # 2. return :
# 2.1. a Function that Returns a Value :
def hello_func():
    return 'Hello Function.'

hello_func()

print(hello_func())

# *This Means that when we Execute our Function, it Actually gonna be Equal to our Returned Value.* """


""" # * 2.2. So Basically, Think of a Function as a Machine, that Takes Input and Produces a Result.

# For Example, When we call the len() Function on a String,
# This just Returns an Integer that is the Number of Characters in our String :

print(len('Test'))

# (We Passed in a String, and it Returned an Integer.) * """


""" # 2.3. We can treat the Executed Function just like a String :
def hello_func():
    return'Hello Function.'

# We can take the Executed Function and just Chain another Function onto the end of it:
print(hello_func().upper())
print(hello_func().lower()) """



# 3. Arguments :

""" # 3.1. How to Pass Arguments to our Function :
# We need to Create some Parameters within the Parentheses:
def hello_func(greeting):
    return '{} Function.'.format(greeting)

# So now Before we run this, we have to pass in the 'greeting' Argument When we Execute our Function:
print(hello_func('Hi'))

# * the 'greeting' Variable Doesn't Effect Any Variables Outside the Funtion,
# Because its Scope is Only Local to the Function. * """


""" # 3.2. Argument Default Value :

# The 'greeting' Parameter is a Required Argument, Because it doesn't have a Default Value;
# If we had a Default Value, it would just fall back to the Default Value Whenever We Didn't Pass the Argument in:
def hello_func(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)

print(hello_func('Hi'))
print(hello_func('Hi', name = 'Mohammad')) """



""" # 4. Positional Arguments and Keyword Arguments :

# *Note: Your Required Positional Arguments, have to come Before your Keyword Arguments;
# If you try to Create a Function with those Out of Order, it will give you an Error.*

# At some point, you probably run across a Funtion in Python that looks sth Like This:
# Basically, all *args and **kwargs are doing is allowing us to accept an Arbitrary(Optional) Number of Positional or Keyword Arguments;
# For Example, student_info Function, takes Positional Arguments(*args) that Represent the Classes that the Student is taking,
# Plus the Keyword Arguments(**kwargs) passed in will be Random Information about the Student:
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

# *In Both of those Examples, we don't know How Many of these Positional Or Keyword Arguments there will be,
# That's Why we use (*args) and (**kwargs);
# And the (Names) Don't Have to be args and kwargs, But that's a Convention that you see a lot.*

# So let's Call this Function with some Random Values:
student_info('Math', 'Art', name='John', age='20')
print('\n')
# When we Run this, it Prints the (args) As a Tuple with All of our Positional Arguments,
# And our (kwargs) as a Dictionary with All of our Keyword Values.
# So Once we have that Tuple and Dictionary, we'll be Able to do whatever we want with that Information.


# Sometimes you might see a Function Call, with Arguments Using * Or **,
# When it's Used in that Context, it Actually Unpack a Sequence Or Dictionary And Pass those Values into the Function Individually.
# So let's make a List and a Dictionary of Everything that we just Passed into our Function:
courses = ['Math', 'Art']
info = {'name': 'John', 'age': '20'}

student_info(courses, info)
print('\n')
# If we Run this, Instead of Passing the Values in Individually,
# It Instead Passed in the Complete List and the Complete Dictionary as Positional Arguments.

# So If we use * in Front of our List And ** in Front of our Dictionary,
# it will Unpack these Values and Pass them in Individually, just like our Previous Execution:
student_info(*courses, **info)
print('\n', '\n') """


# 5. * An Example that Ties Together Everything That We've Learned So Far :

# Number of days per month. First Value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]



def is_leap(year):
    # This String after the Function Definition with """ is called a "Docstring";
    # And Docstrings help Document what a Function Or a Class is Supposed to do.
    """Return True for leap years, False for non-leap years."""
    
    # Code for How a Leap year is Calculated (Not Important):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""
    
    # year 2017, 2020
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'
    
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]


# So let's just Run through this one time and see how these Functions Work :
print(is_leap(2017))
print(is_leap(2020), '\n')

print(days_in_month(2017, 2))
print(days_in_month(2020, 2))