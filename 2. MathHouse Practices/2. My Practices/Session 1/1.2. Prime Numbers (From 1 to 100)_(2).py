
for i in range(2, 101):
    if (i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0) and (i % 7 != 0):
        message = '{}, is a Prime Number'.format(i)
        print(message)
