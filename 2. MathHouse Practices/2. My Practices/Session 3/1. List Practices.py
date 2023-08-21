
# 1. Getting List Values from input :
nums = []

r = int(input("Enter the Range of the List: "))

for i in range(r):
    score = int(input("Enter your Score: "))
    nums.append(score)
print(nums, '\n')


# 2. Printing Total Sum of List Values :
total = 0

for num in nums:
    total += num

print("The Total Sum is:", total, '\n')


# 3. Finding and Printing Maximum And Minimum :
max = nums[0]
min = nums[0]

for num in nums:
    if num > max:
        max = num
    if num < min:
        min = num

print("The Maximum Score is:", max)
print("The Minimum Score is:", min, '\n')


# 4. Failed Lessons Count :

failed = 0
passed = 0

for num in nums:
    if num < 10:
        failed += 1
    else:
        passed += 1

print("Failed Lessons Count:", failed)
print("Passed Lessons Count:", passed)