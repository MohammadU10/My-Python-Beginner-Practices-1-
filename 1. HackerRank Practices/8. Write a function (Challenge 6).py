
def is_leap(year):
    leap = False
    
    # Write your logic here
    if ((year % 100 == 0) and (year % 400 != 0)):
        leap = False
    elif ((year % 100 == 0) and (year % 400 == 0)):
        leap = True
    elif ((year % 4 == 0) and (year % 100 != 0)):
        leap = True
    
    return leap
    
    

year = int(input("Enter a Year: "))
print(is_leap(year))