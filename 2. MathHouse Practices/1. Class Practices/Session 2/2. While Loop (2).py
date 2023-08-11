
total = 0
i = 1

count = int(input("Enter the Count: "))

while i <= count:
    num = int(input("Enter a Number: "))
    total += num ** 2 
    i += 1

print("The Total is: ", total)
