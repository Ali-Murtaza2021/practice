age1 = int(input("Enter a age"))
age2 = int(input("Enter a age"))
age3 = int(input("Enter a age"))
age4 = int(input("Enter a age"))

if age1 > age2 and age1 > age3 and age1 > age4:
    print("Youngest age is :",age1)
elif age2 > age3 and age2 > age4 and age2 > age1:
    print("Youngest age is :",age2)
elif age3 > age4 and age3 > age2 and age3 > age1:
    print("Youngest age is :",age3)
elif age4 > age1 and age4 > age2 and age4 > age3:
    print("Youngest age is :",age4)
else:
    print(" Age Error")