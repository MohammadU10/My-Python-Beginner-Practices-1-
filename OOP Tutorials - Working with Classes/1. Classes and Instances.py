# Python Object-Oriented Programming

# 1. Classes :

# 1.1. If we leave a Class Empty, we will get an Error;
# So If we want to have a Class or Function that we want to leave Empty for the time being,
# Then we can simply put in a 'pass' Statement :
""" class Employee:
    pass


# 1.2. The Difference Between a 'Class' And an 'Instance of a Class' :
emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)
# We can that Both of these are Employee Objects, And they are Both Unique.


# 1.3. Instance Variables :
# Let's say that we wanted 'Employee_1' to have a First Name, a Last_Name, an Email Address, And his Salary :
emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000

# Let's give 'Employee_2' Some of these Same Attributes :
emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000
# Now Each of these Instances have Attributes that are Unique to them.
print(emp_1.email)
print(emp_2.email) """


# 1.4. As we can see, we have to Manually Set these Variables Every time, it's a lot of Code and it's also prone to Mistakes,
# So we don't get much Benefit of using Classes if we do it this way;

# So to Make these Set up Automatically When we Create the Employee,
# We're gonna use a Special 'init' Method :
# (You can think of 'init' as 'initialize', If you're coming from another Language, Then you can think of it as the Constructor)
""" class Employee:
    
    # When we Create Methods Within a Class, they Receive the Instance as the First Argument Automatically;
    # And by Convention, We Should Call the Instance 'self';
    # Now you can Call it Whatever you want, But it's a good idea to Stick to Convention here And just use 'self'.
    
    # So After 'self', What Other Arguments that we want to Accept :
    # We had 'email' too, But we can Create the email Using the First Name And the Last Name.
    
    def __init__(self, first, last, pay):
        # So Now Within our 'init' Method, We're going to Set All of these Instance Variables :
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

# So Now When we Create our Instances of our 'Employee' Class, We can Pass in the Values that we Specified in our 'init' Method;
# Now our 'init' Method takes the Instances Which we called 'self' and the First Name, Last Name, and Pay as Arguments;

# But When We Create our Employee down here, the Instance is Passed Automatically,
# So we can leave off 'self', We Only need to provide the Names, and the Pay.
# So we could Create these By Passing in the 'first', 'last', and 'pay' in Order :
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email) """

# So Everything that we have so far, like the Names, Email, and the Pay are All Attributes of our Class.



# 2. Methods :

# 2.1. Now let's say that we wanted the Ability to Perform Some Kind of Action;
# Now to Do that, We can Add some 'Methods' to our Class.

# So let's say that we want the Ability to Display the Full Name of an Employee;
# We can do this Manually Outside of the Class, just By Using 2 PlaceHolders and format() :
""" print('{} {}'.format(emp_1.first, emp_1.last))
print('{} {}'.format(emp_2.first, emp_2.last)) """

# But that's a lot to Type in each time that you want to Display the Employees' Full Name,
# So Instead, We Create a Method Within our Class that allows us to put this Functionality in One Place :
""" class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    # Like Before, Each Method Within a Class Automatically takes the Instance as the First Argument,
    # So we're going to Always Call that 'self', And the Instance is the Only Argument that we'll need in Order to get to Full Name :
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname()) """


# 2.2. One Common Mistake When Creating Methods is Forgetting the 'self' Argument for the Instance :
""" class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname():
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.fullname()) """


# 2.3. We can Also Run these Methods Using the Class Name itself, Which makes it a bit More Obvious of What's going on in the Background :
class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# Now When we Run it from the Class, we have to Manually Pass in the Instance as an Argument;
# So in this Case, We Pass in 'Employee_1' :
Employee.fullname(emp_1)    # 1. Call on the Class
emp_1.fullname()            # 2. Call Without Class
# So these 2 Lines Above, do the Exact Same thing,
# But in 2. When we do emp_1, which is an Instance, And we Call the Method, We Don't need to Pass in 'self', it Does it Automatically;
# And in 1. When we Call the Method on the Class, Then it Doesn't know What Instance that we want to Run that Method With,
# So We Do have to Pass in the Instance, and that gets Passed in as 'self'.

# If we Print this out, it works Just Like if we were to Print Out '(emp_1.fullname())' :
print(Employee.fullname(emp_1))

# That's What Actually going on in the Background When we Run '(emp_1.fullname())';
# It gets Transformed into 'Employee.fullname(emp_1)' And Passes in 'emp_1' As 'self', And that's Why we have 'self' for those Methods.