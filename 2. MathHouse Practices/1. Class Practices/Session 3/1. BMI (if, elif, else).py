
h = 1.66
w = 80

BMI = w/h**2

if BMI<=18:
    print("Under Weight")
    print("You need to lose: ", round(18*h**2-w, 1))
if BMI>18 and BMI<=25:
    print("Normal")
else:
    print("Over Weight")
    print("You need to lose: ", round(w-25*h**2, 1))
