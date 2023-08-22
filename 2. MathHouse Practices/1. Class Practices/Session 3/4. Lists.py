
# List Indexes :
# nomarat = [19, 15, 18, 11, 8, 14]

# print(nomarat[0])
# print(nomarat[5])

# print(nomarat[-1])
# print(nomarat[-6])

# print(nomarat[0:3])
# print(nomarat[0:])
# print(nomarat[3:])

# nomarat[0] = 17
# print(nomarat)


# Some of List Built-in Methods (And 'del' Keyword) :
# nomarat = [19, 15, 18, 11, 8, 14]

# print(len(nomarat))

# nomarat.append(10)
# print(nomarat)

# nomarat.remove(11)
# print(nomarat)

# del nomarat[3]
# print(nomarat)

# nomarat.insert(3, 1)
# print(nomarat)


# Print All Values of a List, one by one, with 'for' Loops :
# nomarat = [19, 15, 18, 11, 8, 14]

# Method (1) :
# for adad in nomarat:
#     print(adad)
    
# print('\n')

# Method (2) :
# for i in range(len(nomarat)):
#     print(nomarat[i])


# Input an Integer List and then Print it with the Average of its Values :
# l = []
# print(l)

# for i in range(6):
#     adad = int(input("Enter your Score: "))
#     l.append(adad)

# print(l, '\n')


# total = 0

# for i in l:
#     total += i

# print(total/len(l))


# Average of a Scores List (Method 1) :
# nomarat = [19, 15, 18, 11, 8, 14, 20]
# jam = 0
# for adad in nomarat:
#     jam = jam + adad
# print("Moaadel:", jam/len(nomarat))


# Average of a Scores List (Method 2) :
# scores = [19, 15, 18, 11, 8, 14, 20]
# sum = 0

# for i in range(len(scores)):
#     sum += scores[i]

# print("The Average Score is:", sum/len(scores))


# Find and Print Maximum And Minimum Value of an Integer List :
my_list = [3, 7, 12, 5, 9]
max = 0
min = my_list[0]

for i in range(len(my_list) - 1):
    current_value = my_list[i]
    next_value = my_list[i + 1]
    
    if current_value > next_value:
        max = current_value
    elif current_value < min:
        min = current_value

print("The Maximum is:", max)
print("The Minimum is:", min, '\n')
