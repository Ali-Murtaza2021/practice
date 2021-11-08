
n1 = int(input("Enter your age"))
n2 = int(input("Enter your age"))
n3 = int(input("Enter your age"))

if n1 > n2 and n1 > n3:
      print("Oldest age is:",n1)
      if n2 < n3:
            print("Youngest age is:",n2)
      else:
            print("youngest age is:",n3)
elif n2 > n3 and n2 > n1:
      print("Oldest age is:",n2)
      if n1 < n3:
            print("youngest  age is:",n1)
      else:
            print("youngest age is:",n3)

else:
      print ("Oldest age is:",n3)
      if n1 < n2:
            print("youngest age is:",n1)
      else:
            print("youngest age is:",n2)





      