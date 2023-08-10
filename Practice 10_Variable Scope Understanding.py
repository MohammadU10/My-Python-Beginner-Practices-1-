
# 1.1. Variable Scope: This is What Determines Where our Variables can be Accessed From within the Program,
# And What Values those Variables Hold in Different Context.

# So Let's go ahead and look at some Examples to get a Better Understanding at this :


# 1.2. There is a Common Abbreviation for Understanding the Scoping Rules within Python :
# And that Abbreviation is LEGB: Local, Enclosing, Global, Built-in :

# 1) Local: Variables Defined within a Function;

# 2) Enclosing: Variables in the Local Scope Of Enclosing Functions;

# 3) Global: Variables Defined at the Top Level of a Module Or Explicitly Declared Global, Using the 'global' Keyword;

# 4) Built-in: Names that are pre-assigned in Python.

# * Now the Reason that the Abbreviation is in This Order,
# is Because This is the Order that Determines What a Variable is Assigned to;
# So Python First Checks the Variables in the Local Scope, Then the Enclosing Scope, Then the Global, And then Lastly the Built-ins. *


# 2.1. So Let's First Start off With the Global And Local Scope, Because these are probably the Most Commonly Confused :

# So Let's say that we have a Python Module Here:
# x = 'global x'
# Now the Variable 'x' Here is a 'global' Variable, Because it is in the 'main' body of our File.

""" # Now Let's make a Function Here:
def test():
    y = 'local y'
# Now this 'y' Variable Here is a 'local' Variable, And it's 'local' to this 'test' Function; So:
    print(y)

test() """
# If we Run the Function, it Prints out 'local y';
# So Python Use that LEGB Rule when we print out that 'y' Variable, And it Said:
# "Ok, So First I'm gonna Check if I have 'y' in my 'local' Scope, Which are Variables that are Defined Within a Function.";
# And it Found that Local 'y' Variable And Printed it out.

""" # So Now Within the 'test' Function:
def test():
    y = 'local y'
    # print(y)
    print(x)

test() """
# So if we Run this, we can see that even though we are within our 'test' Function, it still Printed out that 'global x';
# And the Reason for that is Because it said:
# "Ok, Do I Have an 'x' Variable in my 'local' Scope?", Which Means that is Defined Within this 'test' Function, So it Doesn't;
# So Now that it doesn't Find it there, it says:
# "Do I have anything in my 'enclosing' Scope?", But it doesn't Find that 'x' in the 'enclosing' Scope either;
# And then it Checks if it has an 'x' in its 'global' Scope, And it Does;
# So it Prints out the Value that it Found in that 'global' Scope, Which was 'global x'.

# But this Doesn't go Both Ways though, For Example, After the test(), if we Write:
# print(y)
# Now we got an error that says: "NameError: name 'y' is not defined";
# The 'y' Variable doesn't Live Outside of that 'test' Function;
# When we Print this 'y' Variable, it Doesn't Find a 'y' Variable in its Local, Enclosing, Global, Or Built-in Scope.

""" # So Now Instead of Printing this 'y' From Outside of the 'test' Function, Let's Print 'x' Global Variable:
x = 'global x'

# So Now Within the 'test' Function Here:
def test():
    x = 'local x'
    # print(y)
    print(x)

test()
print(x)
# So When we Run this, it ran the 'test' Function, came in and Printed out the 'local x',
# And then it comes out and Prints this 'x' after the 'test()' And it Prints 'global x'.
# Now some people might think that 'global x' Variable would have been OverWritten here Within the 'test' Function, But that's Not What Happened;
# So this just Creates a 'local x' Variable here, that Lives Only within this Function,
# And Anything Outside of that 'local' Scope Still Sees the 'global x' Variable. """


# 2.2. What if we actually wanted to Set a New Value for that 'global x' Variable From Within this 'test' Function?;
""" # To do this, we can Explicitly tell Python that the 'x' Variable we wanna work with is the 'global x' Variable:

# x = 'global x'

# To Do this, at the Top:
def test():
    global x
    x = 'local x'
    # print(y)
    print(x)

test()
print(x) """
# 2.3. One Thing About this 'global' Statement, is that we Don't Even Have to have a 'global x' Variable Defined Before we Set Here Within our Function.
""" # So we Come Up There and Comment out that 'global x' Variable,
# Then we can see When we Set this 'global x' within the 'test' Function, Even though it Didn't Exist Up There,
# It was Still Able to Find that Variable that we Printed out that at the Bottom;
# And that Only Works When we are Setting that as a 'global' Variable.
def test():
    # If we Comment Out the 'global x' Here, Now we are Just Setting that Locally:
    # global x
    x = 'local x'
    # print(y)
    print(x)

test()
print(x) """


# 2.4. How to use the 'global' Statement Correctly :
""" # If you Find yourself Using it Often, then you probably doing Something Wrong.

# So Using the 'local' Scope of a Function, Makes it Easier to Understand and Work with;
# So you can Imagine How Difficult it would be to Maintain our Code if you Used these 'global' Statements,
# And Had to worry about Variables And Your Functions OverWriting Values Outside of that Function;
# So with the 'local' Scope, Being Self-Contained, it allows us to Not Have to worry about What's going on Outside of our Function;
# So we wanted to see How the 'global' Statement Works, *But Be Careful Not to OverUse it.* """


# 2.5. Now All of us have most likely seen Functions that take Arguments :

""" # x = 'global x'


def test(z):
    # x = 'local x'
    # print(y)
    print(z)
# Now 'z', is going to be a Local Variable Within this 'test' Function Also;
# So it's Not going to Exist Outside of that Function Either; it's Just like When we Set our 'local x' Variable Within this Function;
# The Only Difference is that as a Function Parameter, it could now be Assigned Values that we Pass into our Function

test('local z')

# If we try to Print out that Outside of the Function here:
# print(z) """



# 3. 'Built-in' Scope: It's pretty Easy to Understand Because it's just Names that are pre-assigned in Python :

# 3.1. So For Example, 'min' is a Built-in Function in Python that Finds the Smallest Value of an Iterable;
""" # So For Example we can use 'min' by saying:
m = min([5, 1, 4, 2, 3])
print(m)
# If we run this, it Prints out '1', Because '1' is the Smallest Value in that Iterable.
# We were able to use min() Here, Because it's a Built-in Function in Python;

# So if we would like to View the Variables that are Within the 'Built-in' Scope:
import builtins

print(dir(builtins))
# Now 'dir()' Just gets a List of the Attributes of a Given Object.
# If we Run that, it Returns All of the Built-ins. """


# 3.2. Now One Thing that you wanna Be Careful With, as far as Built-ins go, is Accidentally OverWriting them;
""" # So this Isn't something that Python Prevents us from doing;
# Now there are Reasons for this, But Basically they are just trusting us with Having the Power to Do that;
# So For Example, if we were to Create a 'min' Function here :
def min():
    pass

min()
# If we Run this, We Don't get Any Errors, But now if we try to Use that Built-in 'min' Function, :
m = min([5, 1, 4, 2, 3])
print(m)
# It gets an Error: "TypeError: min() takes 0 positional arguments but 1 was given";
# Now the Reason for that, is when we ran the 'min()' Function with an Argument,
# Python Found our 'min' Function in the 'Global' Scope Before We fell back to the 'Built-in' Scope, So we have to Be Careful With that. """

# So if we Change the Name of our 'Global' min Function to:
""" def my_min():
    pass

m = min([5, 1, 4, 2, 3])
print(m)
# Then it works Again, Because Now it Doesn't Find 'min()' in that 'Global' Scope,
# And Instead Uses the Built-in 'min()' Function, Just like we Expected. """



# 4. 'Enclosing' Scope :
# The Reason that we Saved it For Last,
# Is Because it's Easier to Understand Once we Understand the 'Local' and 'Global' Scope.

# So the 'Enclosing' has to do With 'Nested Functions' :
# 4.1. So Let's say For Example that we have a Function Within a Function:

""" # x = 'global x'


def outer():
    x = 'outer x'
    
    def inner():
        x = 'inner x'
        print(x)
    
    inner()
    print(x)

outer()
# So we have our outer() Function here that we ran, So we came in there and we Set our Local 'x' Variable,
# Now this Variable is Local to our outer() Function;
# And Then we come in there and Run our inner() Function,
# And Within our inner() Function, we Set that 'x' Variable,
# And that 'x' Variable is Local to our inner() Function, And Then we Print that 'x' Variable;

# Now Uses our Rule(LEGB), So it looks if it had Any Local 'x' Variables,
# And it Does, it has that 'inner x' there,
# And That's Why it Prints out 'inner x' here, Because that is in the 'Local' Scope;

# And then we Printed out 'x' in our outer() Function there,
# And it looked if it had Any Local 'x' Variables,
# And it Does, it has that 'outer x' Local Variable,
# And it Printed out 'outer x' here.

# print(x) """


# 4.2. So Now Let's Comment out Where we Set our 'x' Variable Within our inner() Function :
""" def outer():
    x = 'outer x'
    
    def inner():
        # x = 'inner x'
        print(x)
    
    inner()
    print(x)

outer()
# So Now if we re-Run this, we see that it Printed out 'outer x', Both times;
# And this is What the 'Enclosing' Scope is;
# So When we got to the Point Within our inner() Function Where we Printed out that 'x',
# It First Checked if it had Any 'x' Variables Local to that inner() Function,
# And it Doesn't bBcause we just Commented it out,
# So Then it Checks if it has an 'x' Variable and the Local Scope of Any 'Enclosing Functions';
# So That's Why it's Called the 'Enclosing' Scope;

# So Now we are Looking in the 'Local' Scope of Any Enclosing Functions,
# So our Enclosing Function Here is the outer() Function,
# And We Do Have an 'x' Variable in the Local Scope of that Enclosing Function,
# So That's Why it Printed out 'outer x'. """


# 4.3. So we can see that That's Kind of Similar to our 'Global' and 'Local' Scope Example,
""" # Except Now we are Inside Functions; But the Same Concept Kind of Applies:
# When we Set 'x' in our inner() Function, It Doesn't Affect the 'x' Variable in the outer() Function;

# And Just Like with our 'Global' and 'Local' Scopes,
# If we Come out here and Comment out this 'outer x' And Then Uncomment out that 'inner x',
def outer():
    # x = 'outer x'
    
    def inner():
        x = 'inner x'
        print(x)
    
    inner()
    print(x)

outer()
# And Save And Run that, Then we get an Error,
# Because this Printed out 'x' Within our inner() Function,
# Because it has that Local 'x' Variable Within the inner() Function;

# Then When we try to Print it Outside of that Function,
# It Checked its 'Local' Scope But That's Commented out;

# And Then it's 'Enclosing' Scope Which it Doesn't Have Any Enclosing Functions;

# And Then 'Global' Which There's No 'global x' Function;

# And Then Built-ins So it threw an Error there. """


# 4.4. So When we Looked at our 'global' And 'local' Variables,
""" # We saw that How we could Use that 'global Statement' in Order to
# Explicitly tell Python that we wanted to work With the 'global x' Variable;

# So There is a Way that we can Do this With the 'Enclosing' Scope Variables as well :

# So Let's say Within our inner() Function Here,
# That we wanted to actually Change the 'x' Variable of our outer() Function;

# Now We Shouldn't Use 'global', Because 'global' will Affect the 'global' Scope in this Case;
# We Use the 'non-local' Statement :
def outer():
    x = 'outer x'
    
    # So At the Top of This inner() Function:
    def inner():
        nonlocal x
        # x = 'inner x'
        print(x)
    
    inner()
    print(x)

outer()
# Now This will Allow us to work With the 'local' Variables of Enclosing Functions;
# So in this Case, It Means that we are Now Affecting this 'x' Variable of the outer() Function;

# So Now if we Uncomment out that 'inner x' And we re-Run this,
# And Now we can see that it Prints out 'inner x' Twice;
# And That's Because When we Set our 'x' here to 'inner x' Within our inner() Function,
# We were actually Affecting That 'local x' of our Enclosing Function so it Prints out 'inner x' Within this inner() Function;

# And Also When we Print it out here, it got OverWritten here, So Now it Prints out 'inner x' Twice.

# * Now we can actually see the 'non-local' Statement Being Used More Often Than the 'global' Statement,
# Because 'non-local' Can Be Useful in Order to Change the State of 'Closures' And 'Decorators' and things like that. * """



# 5. Now Just to Wrap All of This Up :

""" x = 'global x'

def outer():
    # x = 'outer x'
    
    def inner():
        # x = 'inner x'
        print(x)
    
    inner()
    print(x)

outer()
print(x)

# So Now if we Run this, We are Simply Setting an 'x' Variable in Each of these Scopes, And Then Printing them out;

# * So Now that we've gone over the "LEGB Rule",
# Then We Should know Exactly What Would Happen if we were to Come in here and Comment out Where we Set the 'x' here Within the inner() Function,
# So if we Run that, Then we can see that When we Printed that it Didn't Find it in its 'Local' Scope,
# And Instead fell back to that 'Enclosing' Scope;

# And if we were to Comment out Where we Set the 'x' here Within the outer() Function And Run that,
# Then we can see that Each Time we Printed All of those 'x' Variables,
# Then it Doesn't Find Either of These and Their 'Local' Scopes Or Their 'Enclosing' Scopes,
# And Instead falls back to that 'Global' Scope in that 'global x' String;

# And if it Didn't Find Anything in that 'Global' Scope,
# Then it would Look in that List of Built-ins that we Looked at earlier;

# And if it Doesn't Find it There, Then an Error is thrown. * """