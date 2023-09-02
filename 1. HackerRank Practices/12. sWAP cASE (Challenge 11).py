
def swap_case(s):
    new_s = ''

    for char in s:
        if char.islower():
            new_s += char.upper()
        elif char.isupper():
            new_s += char.lower()
        else:
            new_s += char
    return new_s


if __name__ == '__main__':
    s = input("Enter your String : ")

    result = swap_case(s)

    print(result)
    