
""" # 0. type() is a built-in function for seeing the Data Type of an object :

num = 3
print(type(num))"""


""" # 1. Arithmetic Operators :

# Addition:
print(3 + 2)

# Substraction:
print(3 - 2)

# Multiplication:
print(3 * 2)

# Division:
print(3 / 2)

# Floor Division:
print(3 // 2)

# Exponent (Power):
print(3 ** 2)

# Modulus (Remainder):
print(3 % 2) """



""" # 2. for seeing if a number is Odd or Even :

print(2 % 2)
print(3 % 2)
print(4 % 2)
print(5 % 2)
# ((Remainder == 0 = Even Number), (Remainder == 1 = Odd Number)) """



""" # 3. Order of Operations :

print(3 * 2 + 1)
print(3 * (2 + 1)) """



""" # 4. Incrementing a variable :

num = 2

# Solution_1:
#num = num + 1

# Solution_2:
#num += 1

# Also for other Operations:
num *= 10

print(num) """



""" # 5. Some built-in Functions to work with Numbers :

# abs() for Absolute Value:
#print(abs(-5))

# round() (by default) --> for Rounding Our Value to the Nearest Integer Value:
print(round (3.75))
print(round (3.5))
print(round (3.4))
print(round (3.1))

# Also we can pass a second argument to specify how many digits we want to round to:
# (Here it is rounded to the first digit after decimal):
#print(round (3.75, 1)) """



""" # 6. Comparison Operators :

num_1 = 3
num_2 = 2

# Equal:
print(num_1 == num_2)

# Not Equal:
print(num_1 != num_2)

# Greater Than:
print(num_1 > num_2)

# Less Than:
print(num_1 < num_2)

# Greater or Equal:
print(num_1 >= num_2)

# Less or Equal:
print(num_1 <= num_2) """



""" # 7. a Common Problem in which Strings are like Numbers :

num_1 = '100'
num_2 = '200'

print(num_1 + num_2)

# So we use Casting (in order to turn the Strings into Numbers) :
num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2) """