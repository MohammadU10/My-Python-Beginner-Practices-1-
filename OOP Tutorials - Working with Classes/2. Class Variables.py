
# 1. Why Class Variables Would be a Better Use Case :

# 1.1. Method 1 (Without Class Variables) :
""" class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # A Method for giving 4% Annual Raise :
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay) """


# 1.2. Method 2 (With Class Variables, that we Don't have to Manually Change the Raise Amount each time) :
""" class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Now if we Just type in 'raise_amount', we get a: "NameError: name 'raise_amount' is not defined";
    # And that's Because When we Access these Class Variables,
    # We need to Either Access them through the Class itself Or an Instance of the Class :
    def apply_raise(self):
        # We could Either use 'Employee.raise_amount',
        # Or we can Also Access through the Instance by using 'self.raise_amount' :
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000) """

""" print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay) """

# 1.3. If these are Class Variables, Then Why can we Access them From our Instance?
# So Let's Print Out a few lines here to get a Better Idea of What's going on :
""" print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount) """
# So Now if we Print these out, we can see that we can Access this Class Variable From Both our Class itself,
# As well as From Both Instances;
# Now What's going on here?
# When we try to Access an Attribute on an Instance, it will First Check if the Instance Contains that Attribute;
# And if it Doesn't it will see if the Class or Any Class that it Inherits From Contains that Attribute.

# Now there's a little Trick to get a Better Idea of What's going on :
""" print(emp_1.__dict__, '\n')

print(Employee.__dict__) """
# Now we can see that the Class Does Contain the 'raise_amount' Attribute,
# And that is the Value that our Instances see When we Access that 'raise_amount' Attribute From our Instances.

# 1.4. An Important Concept :
""" Employee.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount) """
# We can see that it Changed the 'raise_amount' For the Class And All of the Instances;

# Now What if we were to Set the 'raise_amount' Using an Instance Instead of Using the Class?
# So Instead :
""" emp_1.raise_amount = 1.05

print(emp_1.__dict__)
# Now we can see that 'emp_1' has Set 'raise_amount' Within its Namespace Equal to 5%,
# And it Finds this Within its Own Namespace And Returns that Value Before going and searching the Class;
# And we didn't Set that 'raise_amount' on 'emp_2', So that Still falls back to the Class's Value.

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount) """

# So in this Case, we're gonna leave this as '(self).raise_amount' in 'apply_raise(self)' Method,
# Because that will give us the Ability to Change that Amount for a Single Instance if we really wanted to.

# And Also Using 'self' here will Allow Any Subclass to Overwrite that Constant if they wanted to.



# 2. Another Example of a Class Variable Where it Wouldn't really Make Sense to use 'self' :

# We want to Keep Track of How Many Employees that we have,
# So the Number of Employees should be the Same for All Instances of our Class.
class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # Now we gonna use this here Instead of 'self.num_of_emps',
        # Because with the Raises, it's nice to have that Constant Class Value that can Overwritten per Instance if we really need it to be,
        # But in this Case, there's No Use Case we can think of,
        # Where we would want our Total Number of Employees to be Different for Any One Instance :
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps)

# So Now if we run this, it Returns 2, Because it was Incremented Twice When we Instantiated Both of our Employees here.
