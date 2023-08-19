
# 1. Class Methods :

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
    
    # 1.1. To Turn a Regular Method into a Class Method,
    # It's as Easy as Adding a Decorator to the Top Called 'classmethod';
    # Basically this is Altering the Functionality of our Method,
    # to Where now we Receive the Class as our First Argument, Instead of our Instance :
    @classmethod
    # Like 'self' Instance Variable, there's a Common Convention for Class Variables too, and that is 'cls';
    # Now we can't use the Word 'class' as the Variable Name here,
    # Because the Word has a Different Meaning Within the Language;
    # At up at the Top we used the Word 'class' to Create a New Class So that is a Keyword in Python.
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

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

# 3 Strings that are Employees Information(first name, last name, and salary), Separated by hyphens(-) :
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# Now to Create a New Employee from this String, we have to Split the String on the hyphens(-),
# And then we would have our first name, last name, and pay :
first, last, pay = emp_str_1.split('-')

# Then Based on those Values, we would be able to Create a New Employee By Passing in those Values And that would Run our '__init__' Method :
new_emp_1 = Employee(first, last, pay)

print(new_emp_1.email)
print(new_emp_1.pay)


# But if we Don't want to have to Parse these Strings Every time that we want to Create a New Employee,
# So we Create an Alternative Constructor that Allows us to Pass in the String,
# And we can Create the Employee :