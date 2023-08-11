
a = int(input(" Enter a(Shibe Khat): "))
b = int(input(" Enter b(Arz az Mabdaa): "))


if a == 0:
    Equation = 'y = {}'.format(b)
elif b == 0:
    Equation = 'y = {}x'.format(a)
elif b < 0:
    Equation = 'y = {}x{}'.format(a, b)
elif a == 0 and b == 0:
    Equation = 'y = 0'
else:
    Equation = 'y = {}x+{}'.format(a, b)

print(Equation)
