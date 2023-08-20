
# 1. Class Methods :

""" class Employee:
    
    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) """
    
    # 1.1. To Turn a Regular Method into a Class Method,
    # It's as Easy as Adding a Decorator to the Top Called 'classmethod';
    # Basically this is Altering the Functionality of our Method,
    # to Where now we Receive the Class as our First Argument, Instead of our Instance :
    # @classmethod
    # Like 'self' Instance Variable, there's a Common Convention for Class Variables too, and that is 'cls';
    # Now we can't use the Word 'class' as the Variable Name here,
    # Because the Word has a Different Meaning Within the Language;
    # At up at the Top we used the Word 'class' to Create a New Class So that is a Keyword in Python.
    # def set_raise_amt(cls, amount):
    #     cls.raise_amt = amount


""" emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000) """

""" Employee.set_raise_amt(1.05)
# It is Same as saying 'Employee.raise_amt = 1.05'.

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt) """

# You can Run Class Methods From Instance as well, But that Doesn't really make a lot of sense And that is Not Common;
# But just to Show What that would look like :
""" emp_1.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt) """


# 1.2. Class Methods as Alternative Constructors :
# This Means that we can use these Class Methods in Order to Provide Multiple Ways of Creating our Objects; For Example :

""" # 3 Strings that are Employees Information(first name, last name, and salary), Separated by hyphens(-) :
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# Now to Create a New Employee from this String, we have to Split the String on the hyphens(-),
# And then we would have our first name, last name, and pay :
first, last, pay = emp_str_1.split('-')

# Then Based on those Values, we would be able to Create a New Employee By Passing in those Values And that would Run our '__init__' Method :
new_emp_1 = Employee(first, last, pay)

# new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay) """


# But if we Don't want to have to Parse these Strings Every time that we want to Create a New Employee,
# So we Create an Alternative Constructor that Allows us to Pass in the String,
# And we can Create the Employee for us :

""" class Employee:
    
    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    
    # Our Alternative Constructor :
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)


emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay) """
# So Now if we Run this, we get the Exact Same Values,
# So Now we would have No need to Parse the Strings Anymore;
# We have Provided them with a 'from_string' Alternative Constructor,
# And Now we can Pass in those Strings And get their New Employee Objects.

# So When People say that they Use Class Methods as Alternative Constructors, Then This is What they Mean.


# 1.3. A Real-World Example of Alternative Constructors (With datetime Module) :
# import datetime

# So the Default Way of Creating a 'date/time' Object is to say Something Like 'datetime' And Then Pass in the year, month And date;

# But if we look Here at these Class Methods, Which are Alternative Constructors,
# Then What they Do is They have this 'fromtimestamp()', And we can use the Current Time, Which is 'today()',
# And they have a Couple of Other Examples Here as well.

# And we can see that They are Basically Doing the Same thing that We just Did in our 'Employee' Example;
# So we can see that They are Accepting the Class(cls) and a Timestamp(t) With this 'fromtimestamp()' Constructor,
# And Then they are Parsing out some Dates, And Then they are Creating that New 'date/time' Object And Returning that;
# So it's a New Way of Creating 'date/time' Objects.
""" class datetime:
    
    @classmethod
    def fromtimestamp(cls, t):
        "Construct a date from a POSIX timestamp (like time.time())."
        y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
        return cls(y, m, d)
    
    @classmethod
    def today(cls):
        "Construct a date from time.time()."
        t = _time.time()
        return cls.fromtimestamp()
    
    @classmethod
    def fromordinal(cls, n):
        # Construct a date from a proleptic Gregorian ordinal.
        
        # January 1 of year 1 is day 1. Only the year, month and day are
        # non-zero in the result.
        
        y, m, d = _ord2ymd(n) """



# 2. Static Methods :

# Now When Working With Classes,
# "Regular Methods" Automatically Pass the "Instance" as the First Argument And We Called that 'self';
# And "Class Methods" Automatically Pass the "Class" as the First Argument And We Called that 'cls';

# And "Static Methods" Don't Pass Anything Automatically, They Don't Pass the Instance Or the Class;
# So really, They Behave just like Regular Functions,
# Except we Include them in our Classes, Because They have some Logical Connection With the Class.

# So Let's take a look at an Example to Better know What we Mean here :

class Employee:
    
    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    # So we want a Function that takes in a Date And Returns Whether Or Not that Was a Workday,
    # So that has a Logical Connection to our 'Employee' Class,
    # But it Doesn't Actually Depend on Any Specific Instance Or Class Variable;
    # So Instead we gonna make this a Static Method :
    @staticmethod
    # Now Remember, Static Methods Don't take the Instance Or the Class as the First Argument,
    # So we can just Pass in the Arguments That we want to Work With :
    def is_workday(day):
        # So we're just going to Return whether or Not our Day Falls on a Weekday;
        # So in Python, Dates have these Weekday Methods Where Monday = 0 And Sunday = 6, And All the Other Days in Between.
        # (Saturday = 5, Sunday = 6)
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# Now Sometimes people Write Regular Methods Or Class Methods, That Actually Should be Static Methods;
# And Usually a Giveaway That a Method Should be a Static Method,
# Is if you Don't Access the Instance Or the Class Anywhere Within the Function,
# So for Example, we're Using that Class Variable in the Class Method 'from_string()',
# But if we weren't Using it Anywhere Within that Method, Then it Probably Doesn't Need to be a Class Method;
# And the Same With Regular Methods if we're Not Using that 'self' Variable,
# Then we Probably want to Check if it would be Appropriate to Use a Static Method in that Place.


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# Let's see if our Static Method is Working :
import datetime
my_date1 = datetime.date(2016, 7, 10)
my_date2 = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date1))
print(Employee.is_workday(my_date2))
