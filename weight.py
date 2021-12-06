w = float(input("Enter a weight is = "))
h = float(input("Enter a height is = "))
x = w/(h*h)
print(x)
if x < 18.5:
    print("Underweight")
elif x >= 18.5 and x < 25:
    print("Normal")
elif x >= 25 and x < 30:
    print("Overweight")
else :
    print("obesity")