
""" # 1. ** Now When we Import a File, it Runs All of the Code From the Module that We Import. **
# So to Import this Module :
import Practice_9_my_module

# 1. * So We have another module over here :
courses = ['History', 'Math', 'Physics', 'CompSci']

# 1. *** Let's say that We want to use 'find_index' Function;
# When Importing Modules like this, we just Can't Call our 'find_index' Function;
# We Instead have to Type the Module Name First and Then What We Wanna Grab from the Module :
index = Practice_9_my_module.find_index(courses, 'Math')
print(index) """



""" # 2. If we are using 'find_index' Function Multiple Times throughout our Script,
# It might get a little Old and Take Up a lot of Room to keep Typing 'my_module.find_index()' Everywhere;

# We can Specify a Name that we wanna Use for our Imported Module,
# And Usually this is used to make the Module Name Shorter;

# So When we are Importing my_module at the top, we could Instead say :
import Practice_9_my_module as mm

courses = ['History', 'Math', 'Physics', 'CompSci']

# And Now When Using this Import throughout the Script, Instead of Typing my_module Everywhere, we can just use 'mm' :
index = mm.find_index(courses, 'Math')
print(index) """



# 3. How to Import the Function Itself :
""" from Practice_9_my_module import find_index

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index) """

# * Note: It Only gives us Access to that 'find_index' Function, And Not Everything Else in the Module.
# For Example we had the 'test' Variable in the Module;
# So When we Import this way, now we Don't have Access to it, Since we are Only Importing find_index(). *
# If we wanted to Import the Variable :
""" from Practice_9_my_module import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test) """

# ** Also When Importing in this Way, we can Access to them as Keyword, So to make this even Shorter :
""" from Practice_9_my_module import find_index as fi, test as t

courses = ['History', 'Math', 'Physics', 'CompSci']

index = fi(courses, 'Math')
print(index)
print(t) """

# *** Using this Method of Importing, we'll have to Add Commas and Specify Each Value that we want to Import;
# There is a Way to just Import Everything, But It's pretty Uncommon to use that :
""" from Practice_9_my_module import *

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test) """

# But the Reason this Method is Uncommon and frowned upon,
# is Because Now We Can't tell What Came From that Imported Module, And What Didn't (It's Just Not Obvious);
# So Basically Importing Everything with *, just makes it Harder to track down a Problem.



""" # 4. So When we Import a Module, How Does it Know to Where to Find the Module?
# When we Import a Module, It Checks Multiple Locations,
# And the Locations that it Checks, is Within a List Called 'sys.path';
# And we can see this List if we Import the 'sys' Module :
from Practice_9_my_module import find_index, test
import sys

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
# print(index)
# print(test)

print(sys.path)

# * So it Prints the List of Directories on our Machine Where Python Looks for Modules When we Run an 'import';
# So Directories get Added in This Order :
# 1) The First Value is the Directory Containing the Script that we are Currently Running,
# And the Practice_9_my_module.py File that we are Importing, it Within that Directory Also, so that's How it Founded.
# 2) Next it Adds Directories Listed in the "Python Path Environment Variable".
# 3) After the "Python Path", it Adds the "Standard Library Directories", And that's How we can Import those Modules From the "Standard Library".
# 4) Lastly, it Adds the "Side Packages" Directory For "Third Party Packages". """



# 5. When the Module that we want to Import isn't in the Same Directory As the Script that we are trying to Import it From :
# (We Moved the my_module.py File to Desktop)

# Now There a Couple of Approaches that we can take here :

# 1. We can Manually Add that Directory to Our 'sys.path' List, we can Treat this List, just like Any Other List; :
# So Before we Import my_module, we could Add that Directory to 'sys.path' :
""" import sys
sys.path.append('/Users/Yousefian/Desktop/My-Modules')

from Practice_9_my_module import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
# print(index)
# print(test)

print(sys.path) """

# * But This isn't the Best-Looking Approach, Because we are Appending this Directory Before our Other Imports;
# And Also, if we were to Import our Module And we had This Manually Hard-Coded in Multiple Locations, Then we have to Change All of those.

# So Instead, we can make this Change in the Next Place 'sys.path' looks,
# 2. And as we Mentioned in #4, that is the "Python Path Environment Variable";
# And we can Set that By going to :
# "This PC Properties >> Advanced system settings >> Environment Variables >> User Variables for 'PC_Name' >> New...";
# And Then going to 'cmd' and typing 'python' and then 'import (module_name)'



# 6. Some of Useful Standard Library Modules :

""" # 6.1. 'random' Module :
import random

courses = ['History', 'Math', 'Physics', 'CompSci']

random_course = random.choice(courses)

print(random_course) """


""" # 6.2. 'math' Module to Perform some Common Mathematical Operations :
import math

rads = math.radians(90)
print(rads)

print(math.sin(rads)) """


""" # 6.3. 'datetime' And 'calendar' Modules to Work With Dates and Times :
import datetime
import calendar
# These Two have some Similarities But they are Also Very Different.

# For Example, if we want Today's Date :
today = datetime.date.today()
print(today)

# With the 'calendar' Module, we can ask, for Example, Is 2023 a Leap Year :
print(calendar.isleap(2023))
print(calendar.isleap(2020)) """


""" # 6.4. 'os' Module that gives us Access to the Underlying Operating System :
import os

# For Example, to see What Directory we are Currently in :
# (cwd Stands For "Current Working Directory")
# print(os.getcwd())


# 6.5. These Modules are Just Python Files themselves,
# And We Can View the Location of a Module, Just By Printing Out its 'Dunder File' Attribute :
# Dunder just Means Two Underscores ('__')
print(os.__file__)

# 6.6. 'antigravity' Module is a kind of a joke in the Python Community :
import antigravity """