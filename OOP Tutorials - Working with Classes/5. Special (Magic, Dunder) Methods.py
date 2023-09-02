
# 1. Special Methods that we can use Within our Classes (aka Magic Methods) :

# 1.1. This Special Methods allow us to Emulate some Built-in Behavior Within Python,
# And it's Also How we Implement Operator Overloading; For Example :
""" print(1 + 2)
print ('a' + 'b') """
# We can see that the Behavior When we Add 2 Strings together, is Different that When we Add 2 Integers together;
# So the Strings were just Concadinated, And the Integers were Actually Added together.
# So Depending on What Objects you're working with, the Addition Actually has Different Behavior.


""" class Employee:
    
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1) """
# 1.2. If we Print our Employee Instance here, Then we just get a Vague Employee Object;
# And it would be nice if we could Change this Behavior to Print out something a little bit More User-Friendly;
# And that's What these Special Methods are going to allow us to do;
# So by Defining our Own Special Methods, we'll be able to Change some of this Built-in Behavior and Operations.

# So these Special Methods are Always Surrounded By Double Underscores(__method__);
# So a lot of people call these Double Underscores "dunder",
# So if we ever hear something like "dunder init", Then it Means '__init__'.

# So speaking of '__init__', that is a Special Method,
# That is Probably the First And Most Common Special Method that people Use When Working With Classes;

# So just like we learned Before, this Special '__init__' Method is Implicitly Called When we Create our Employee Objects up there,
# And it comes in And Sets All of our Attributes for us.


# 1.3. So Let's take a look at Some Other Common Special Methods :
class Employee:
    
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
# So 2 More Common Special Methods that we should Probably Always Implement Are '__repr__' And '__str__' :
    # 1) In Short, '__repr__' is Meant to be Unambiguous Representation of the Object,
    # And Should be Used for Debugging And Logging And things Like that, It's Really Meant to be Seen By Other Developers :
    def __repr__(self):
        # So First, We want to be Sure to At Least have an 'repr' Method,
        # Because if we have this Without an 'str', Then Calling 'str' on an Employee, we'll just Use the 'repr' As a Fallback,
        # So it's Good to Have this as a Minimum.
        
        # Now a good rule of thumb When Creating this Method,
        # Is to try to Display something that you can Copy And Paste Back in the Python Code That would Recreate that Same Object :
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
        # So Here, we are trying to Return a String that we can Use Recreate the Object.
    
    # 2) And '__str__' is Meant to be More of a Readable Representation of an Object,
    # And is Meant to be Used As a Display to the End-User :
    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# Now These 2 Are What Implicitly Called Anytime we Run 'repr' on One of our Objects OR 'str' on One of our Objects,
# And These Are What we're going to Use to Fix our Problem of Printing out the Vague Employee Object,
# When we Printed out our Employee Instance there :
""" repr(emp_1)
str(emp_1) """

# 1) Using '__repr__' Method :
""" print(emp_1) """
# Now Instead of the Vague Employee Output we got When we Printed out the Instance Before,
# Whenever we Rerun this with 'repr' Method, we can see that it Returns the String that we Specified in our 'repr' MEthod.

# 2) Using '__str__' Method :
# So Now if we Print out this Employee Object Again, Now it will Use that '__str__' Method Instead :
""" print(emp_1) """

# Now we can Still Access the 'repr' And the 'str' Specifically :
""" print(repr(emp_1))
print(str(emp_1)) """

# Now When we Run this 'repr' And 'str', What's Actually going on in the Background,
# Is that it's Directly Calling those Special Methods, So Instead it's Actually Calling '__repr__' And '__str__' :
""" print(emp_1.__repr__())
print(emp_1.__str__()) """
# Then we can see that we get the Exact Same Object By Calling those Directly.
# So These 2 Special Methods Allow us to Change How our Objects are Printed And Displayed.


# 1.4. Now In Fact, Unless you're Writing some More Complicated Classes,
# These 3 Methods of '__init__','__repr__', And '__str__', Will be the Ones that we'll probably Use Most Often;
# But Let's Look at a Few More just to get an Idea of How these work.

# Now There are Also a lot of Special Methods For Arithmetic;
# So Like we saw Before, When we said:
""" print(1+2) """
# It's Actually Using a Special Method in the Background Called '__add__';
# So we can Actually Access this Directly :
""" print(int.__add__(1, 2,)) """

# And Strings are Actually Using their Own '__add__' Method,
# So if we Use a String Object :
""" print(str.__add__('a', 'b')) """


# 1.5. So we can Actually Customize How Addition Works For our Objects By Creating that '__add__' Method;
# So Let's say that With our Employee Class,
# We wanted to be able to Calculate Total Salaries, just By Adding Employees Together.

# * Note: That's Kind of a Contrived Example, Because if we were to Make a Class Like that in Real Life,
# Then it's Probably Better to be Explicit About What you're Adding Together,
# But just for the sake of this Example, Let's go ahead and see How we do this. *