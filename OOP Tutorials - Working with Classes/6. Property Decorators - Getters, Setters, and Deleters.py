
# *** How to Use Property Decorators ***

# 1. Getters :

# 1.1.
""" class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith') """

# As we can see, All of these are giving us What we would expect :
""" print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname()) """


# Now Let's Set Employee first name to 'Jim' And Rerun this :
""" emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname()) """

# So we can see in the Output, that the first name was Changed to 'Jim', But the email still has our Old first name;
# Now the 'fullname()' Method Doesn't have this Problem, Because Every Time we Run the 'fullname()' Method,
# It goes into the Method And Grabs the Current first name And last name;

# So What if the People who are Using our Class said that we need to Fix this?
# So they Don't want to Change the email Every Time they Change the first name Or last name,
# They want it to Update the email Automatically When Either the first name Or last name has Changed;

# Now your first thought might be to just Create an email Method just like we did there With our 'fullname()',
# But the Problem with that, is that it will Break the Code For Everyone Currently Using the Class,
# So they would have to go through And Change Every Instance of the email Attribute with an 'email()' Method;


# 1.2. Now this is Where People From Other Languages like Java will bring up the Benefits of 'getter' And 'Setter' Methods And they really Come in Handy,
# But Within Python, We Can Do this Using the "Property Decorator";
""" class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # So Now we can Remove our email Attribute.
    
    # Now the "Property Decorator" Allows us to Define a Method, But We Can Access it Like an Attribute.
    # So For Example, Let's Pull this email Attribute out into a Method, Similar to our 'fullname()' Method :
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    # So Right Now, our email() Method is Similar to our fullname() Method;
    # So Each time we ran it, it would get the Current first name And last name,
    # But we'd Also Have to go through And Change our Code to Where Every email Attribute is a Method Call.

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')

emp_1.first = 'Jim'

print(emp_1.first)

# So For Example, When we're Printing this out down here,
# We Instead have to Add Parentheses to '.email' :
print(emp_1.email())

print(emp_1.fullname())
# So we can see that it Solved our Problem Where it Set our email address to the New first name,
# But this Also Means that Anyone Using our Class would have to Change their Code Also, So That's Not What We Want. """


# 1.3.
""" class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    # So in Order to Continue Accessing email Like an Attribute, We Can just Add a Property Decorator Above this Method :
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    # * Also Adding a Property Decorator for fullname() :
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last) """


""" emp_1 = Employee('John', 'Smith')

emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname) """
# So Now if we Run this, Then we can see that Works;
# So we are Defining our email in our Class Like it's a Method,
# But we are Able to Access it like an Attribute;

# * And We Could Do this just as Easily With 'fullname()' As Well. *

# Now that goes against What we said about Changing the Code,
# But as an Example, we Also wanted to Use the 'fullname()' to Show an Example How We Can Use a "Setter".



# 2. Setters :

# 2.1.
""" emp_1 = Employee('John', 'Smith')

# So For Example, We Want the Ability to Say :
emp_1.fullname = 'Corey Schafer'
# And Let's say that by Setting this 'fullname',
# We Also Wanted it to Change Our first name, last name, and email, And Right Now We Can't Do this.

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
# So if Only Have the 'fullname()' With the Property Decorator And We Try to Set 'fullname' Like this,
# If We Run this, We get an Error there saying that: "We Can't Set the Attribute". """


# 2.2. So in Order to Do What we were trying to Do there,
# We are going to Have to Use a 'Setter', And That is Another Decorator :
""" class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    # Now the Name that We are going to Use for our Setter, is going to be the Name of the Property;
    # So in this Case, it's going to be 'fullname' :
    @fullname.setter
    # And Then Underneath this Decorator, We just need to Create Another Method With the Same Name :
    def fullname(self, name):
        # Now this 'name' Value Here is the Value that we are trying to Set;
        # So in this Case Down there Below the Class, it would be the 'fullname = 'Corey Schafer''.

        # So Here, We Want to Set the first name And the last name, Using that 'fullname' Down there;
        # So We Can just Split that Name that we Pass in on the Space Separator :
        first, last = name.split(' ')
        # Splitted that name into 2 Parts: 1. first name, 2. last name.

        # Now Want to Set our Employee's first name And last name Equal to those Values :
        self.first = first
        self.last = last


emp_1 = Employee('John', 'Smith')

emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
# That Works! :)

# So What Happened Here is that Whenever we Set the 'fullname' Equal to this Name,
# It Came into our Setter there And it Parsed the Names From that Value that We Set,
# And Then it Set Our first name and last name;

# And Since We Set the first name And last name, Even we Printed out Our email,
# It Came in there And Grabbed those Correct Values. """



# 3. Deleters :

# Now We Can Also Make a Deleter in the Same Way;
# So Let's Say if we were to Delete the fullname of our Employee that We Wanted to Run Some Kind of Cleanup Code :
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    # So Instead of a 'setter', this is going to be a 'deleter' For fullname,
    # And this Won't be Accepting Any Other Values Other than 'self' :
    @fullname.deleter
    def fullname(self):
        # And just to see this Doing Something :
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')

emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# So the Deleter Code there is What gets Run Whenever We Delete an Attribute, So if we say :
del emp_1.fullname


# * So in Overall, "Property Decorator" is a Nice Feature Because it Allows Us to Access Attributes Without Putting Getters And Setters Everywhere,
# But if We Need that Functionality, Then it's Easy to Add in With the "Property Decorator";
# And if We Do this Correctly, Then People Using our Class Won't Even Need to Change Any of their Code,
# Because they'll Still be Able to Access those Attributes in the Same Way that they Did Before.