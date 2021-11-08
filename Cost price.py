Cp = int(input("Enter a Price"))
tax = 0

if Cp > 100000:
    tax = 15/100*Cp
    print("Cost of Price ",tax)
elif Cp > 50000 and Cp <= 100000:
    tax = 10/100*Cp
    print("Cost of Price",tax)
elif Cp <= 50000:
    tax = 5/100*Cp
    print("Cost of Price",tax)
else:
    print("Road tax to be paid")