
if __name__ == '__main__':
    n = int(input("Enter a Number: "))


def nums_str():
    str = ''
    for i in range(1, (n + 1)):
        str += '{}'.format(i)
    return str


print(nums_str())