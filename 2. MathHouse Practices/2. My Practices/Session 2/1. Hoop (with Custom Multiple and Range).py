
min = int(input("Enter Minimum of the Range: "))
max = int(input("Enter Maximum of the Range: "))
hoop = int(input("Enter the Hoop: "))

i = min

while min<=i<max:
    i += 1
    if i%hoop==0:
        print("Hoop!")
        continue
    print(i)
