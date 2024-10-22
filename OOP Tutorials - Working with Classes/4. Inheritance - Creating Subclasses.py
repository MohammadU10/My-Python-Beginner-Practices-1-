
# 1. Creating Subclasses :

# Let's say that We want to Create different Types of Employees, 
# For Example, we want to Create Developers And Managers;
# Now both Developers and Managers are going to have names, emails,
# and a salary, And those are all things that our Employee Class has;

# So Instead of Copying the codes in '__init__' Method into our Manager And Developer Subclasses,
# We can just Reuse that Code By Inheriting from Employee.

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
        
        
# Create Developer And Manager Subclasses :
""" class Developer(Employee):
    pass """
# So Right Now, Even Without Any Code of its Own, the Developer Class will have All of the Attributes And Methods of our Employee Class.


# Here we are Creating 2 new Employees and Printing out their emails :
""" # dev_1 = Employee('Corey', 'Schafer', 50000)
# dev_2 = Employee('Test', 'User', 60000)

# print(dev_1.email)
# print(dev_2.email) """

# But Now Instead, we're going to create 2 new Developers and Pass in All of the Same Information :
""" dev_1 = Developer('Corey', 'Schafer', 50000)
dev_2 = Developer('Test', 'User', 60000)

# print(dev_1.email)
# print(dev_2.email) """

# What happened Here is that when we Instantiated our Developers,
# It First looked in our Developer Class for our '__init__' Method,
# And it's Not going to Find it Within our Developer Class Because it's Currently Empty,
# So it walks up this Chain of Inheritance Until it Finds What it's Looking For;

# Now this Chain is Called the "Method Resolution Order".
# Now Here we have a Really Useful 'help()' Function that Makes these things a lot Easier to Visualize :
""" # print(help(Developer)) """
# Now When we Run this, the "Method Resolution Order" that we Mentioned is one of the First things that gets Printed out,
# And Basically these are the Places that Python Searches For Attributes And Methods :
# So When we Created our 2 new Developers, it First Looked at our Developer Class for the '__init__' Method,
# And When it Didn't Find it there, then it went up to the Employee class and it found it there, So that's Where it was Executed;
# Now if it Had Not Found it in our Employee Class,
# Then the Last Place that it would have Looked, is this Object Class and Every Class in Python Inherits From this Base Object.

# Now if we Look at this Output Further, Then it Actually Shows the Methods that were Inherited From Employee;

# And Then we have our Data And Other Attributes,
# And is shows that the Class Attribute 'raise_amt' was Also Inherited From the Employee Class.



# 2. Customization :

# 2.1. Now Let's say that we wanted to Customize our Subclass a little bit :
# Now we're going to Simply Change the 'raise_amt';
# But First Let's go ahead and see what Happens When We Apply a raise on our Current Developer :
""" print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay) """

# But Let's say that We wanted our Developers to have a 'raise_amt' of 10%,
# Now to Change that, it's just as easy as coming into our Developer Class here and Changing the 'raise_amt' to 10% :
""" class Developer(Employee):
    raise_amt = 1.10


dev_1 = Developer('Corey', 'Schafer', 50000)
dev_2 = Developer('Test', 'User', 60000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay) """
# Now if We rerun this, we can see that it Used our Developer Class's 'raise_amt', instead of our Employee Class's 'raise_amt'.

# Now if We were to Change this Instance Back to an Employee Instead of a Developer,
# And then reran this, Then we can see that Now it's Back to that Employee 4% raise amount :
""" dev_1 = Employee('Corey', 'Schafer', 50000)
dev_2 = Employee('Test', 'User', 60000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay) """

# So the thing to take away here, is that by Changing the 'raise_amt' in our subclass,
# It Didn't have any Effect on any of our Employee Instances, So they still have that 'raise_amt' of 4%;
# So we can make these changes to our Subclasses without worrying about breaking anything in the Parent Class.


# 2.2. So Now we gonna Change this back to Developer And we'll make a few more Complicated Changes :

# So Sometimes we want to Initiate our Subclasses with More Information Than our Parent Class can Handle;

# So Let's say that when we Created our Developers here,
# Then we wanted to Also Pass in their Main Programming Language as an Attribute,
# But currently our Employee Class only Accepts first-name, lastname, and pay;
# So if we Also wanted to Pass in a Programming Language there,
# Then we're going to have to give the Developer Class its Own '__init__' Method :

class Developer(Employee):
    raise_amt = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        # Now What you might be tempted to do here,
        # Is just go up and Copy All of the Code from our Employees Classes and '__init__' Method,
        # And Paste it into our Developer Classes '__init__' Method,
        # But we Don't want to do that, Because we want to Keep our Code DRY and Not Repeat this Logic in Multiple Places,
        # Because We Want it to be as Maintainable as Possible.
        
        # So Instead of Copying and Pasting that, What We're Instead going to Do,
        # Is just let our Employees and '__init__' Method Handle the first name, last name, and pay,
        # And Then We'll let the Developer Set the Programming Language.
        # So in Order to Let that Employee Handle the first name, last name, and pay :
        super().__init__(first, last, pay)
        # Now there are Multiple Ways of Doing this Logic here, you may see some people do :
        """ Employee.__init__(self, first, last, pay) """
        # Now Both of these Ways of Calling the Parent's '__init__' will work,
        # But Here We tend to Use 'super()', Because with Single Inheritance Like we are Using Here, it's a little bit More Maintainable,
        # But it's really Necessary Once you Start Using Multiple Inheritance;
        # But to Keep things Simple, we Usually just like to Always Stick With 'super()'
        
        # So Now we can Handle the Programming Language Argument just like we would in the other Class :
        self.prog_lang = prog_lang


""" dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

print(dev_1.email)
print(dev_1.prog_lang) """



# 3. Creating Another Subclass (Manager) :
class Manager(Employee):
    
    # 3.1 Now When we Create a New Manager, we're going to give the Option of Passing in a List of Employees that this Manager supervises;
    # So we're going to Need to Add an '__init__' Method for our Manager :
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        # Now you might be wondering Why we Didn't just Pass in an Empty List as Default Argument here Instead of 'None',
        # But you Never want to Pass Mutable Data Types Like a List Or a Dictionary as Default Arguments.
    
    # So Now Let's Add in a few Methods Here :
    # So we're going to give the Option to Add and Remove From our List of Employees that our Manager supervises :
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    # And Lastly, we're going to Add a Method that will Print out All of the Employees that this Manager supervises :
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


# 3.2. Testing :
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

""" # So Now Let's Make Sure that this Manager was Successfully Created,
# And that we have All of the Attributes And Methods Available,
# That it would have Inherited From that Employee Class :
print(mgr_1.email)

# Print out All the Employees that this Manager supervises :
mgr_1.print_emps()
print('\n')

# Add 'dev_2' to the List of Employees :
mgr_1.add_emp(dev_2)

mgr_1.print_emps()
print('\n')

# Remove 'dev_1' from the List of Employees :
mgr_1.remove_emp(dev_1)

mgr_1.print_emps() """



# 4. Python has Two Built-in Functions Called 'isinstance' And 'issubclass' :

# 1. 'isinstance' will tell us if an Object is an Instance of a Class, For Example :
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee), '\n')

# But if we Check if 'mgr_1' is an Instance of 'Developer' Class, Then that Returns 'False';
# Because Even though Developer And Manager Both Inherit From Employee, they Aren't Part of Each Other's Inheritance.
print(isinstance(mgr_1, Developer))


# 2. 'issubclass' will tell us if a Class is a Subclass of Another :
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee), '\n')

print(issubclass(Manager, Developer))



# 5. (*Extra*) A Practical Real-World Example of Inheritance :

# We can Find One the Easier Examples of Subclassing within the "Exceptions" Module of Python "whisky" Library.

# So This is a Really Popular Library And Used in a lot of Different Projects.

# @implements_to_string
class HTTPException(Exception):
    
    """This HTTPException is the Baseclass for all HTTP exceptions"""