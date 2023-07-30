
""" # 1. an Example of Looping through a List ('for' Loops) : 

nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num) """


""" 
# 2. Two Important Keywords: 'break' and 'continue' :

nums = [1, 2, 3, 4, 5]

# # 2.1. 'break' Keyword will Completely Break Out of the Loop :
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)


# 2.2. 'continue' Keyword will kip to the next iteration of the Loop :
# We use 'continue' Keyword to just ignore a Value, but Not Break Out of the Loop Completely.
for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num) """



""" # 3. a Loop Within a Loop (Nested Loops):

nums = [1, 2, 3, 4, 5]

for num in nums:
    for letter in 'abc':
        print(num, letter) """



""" # 4. How to go through a Loop a Certain Number of Times :

nums = [1, 2, 3, 4, 5]

# There is a built-in Funtion called range() :
# for i in range(10):
#     print(i)

# If we don't want to start at 0, we can also Pass a Starting Value into range() :
for i in range(1, 11):
    print(i) """



# 5. 'while' Loops :

# 'for' Loops iterated through a Certain Number of Values,
# But 'while' Loops will just keep going Until a Certain Condition is met,
# OR Until we Hit a Break.

# For Example:
""" x = 0

while x < 10:
    print(x)
    x += 1 """


# Also at Any Point we can use a 'break' to Break Out, just like 'for' Loops:
""" while x < 10:
    if x == 5:
        break
    print(x)
    x += 1 """


# Now Sometimes we want to create an Infinite Loop, that Never Ends Until we Get some Input or Find some Value:
""" while True:
    if x == 5:
        break
    print(x)
    x += 1 """


# *Note: If we accidentally get stuck in Infinite Loop,
# Then within most Environments or Operating Systems,
# We can Interrupt that By Pressing "Ctrl + C" to Stop the Process:
""" while True:
    # if x == 5:
    #     break
    print(x)
    x += 1 """