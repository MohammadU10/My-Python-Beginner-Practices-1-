
for num in range(1, 101):
    count = False
    for i in range(2, (num // 2 + 1)):
        if (num % i == 0):
            count = True
            break

    if (count == False and num != 1):
        print(num)
