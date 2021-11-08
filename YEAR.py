Yr = int(input("Enter a Year"))

if Yr % 100 == 0:
    if Yr % 400 == 0:
        print("Year is leap year :")
    else:
        print("Year is not a leap year")
else:
    if Yr % 4 == 0:
        print("Year is leap year")
    else:
        print("Year is not a leap year")
