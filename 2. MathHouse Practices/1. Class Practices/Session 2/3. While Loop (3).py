
positive = 0
negative = 0

while True:
    num = int(input("Enter a Number: "))
    if num > 0:
        positive += 1
        #continue
    if num < 0:
        negative += 1
        #continue
    else:   # num == 0
        break
    
print("Positive Nums Count: ", positive)
print("Negative Nums Count: ", negative)
