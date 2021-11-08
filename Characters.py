char = ord(input("Enter a character"))

if char>=ord("a") and char<=ord("z"):
    print("Lowestcase letters",char)
elif char>=ord("A") and char<=ord("Z"):
    print("Uppercase letters",char)
else:
    print("Error")