myList = [10, 25, 17, 9, 30, -5]
# Returns the elements which are multiples of 5
myList2 = list(filter(lambda n : n%5 == 0, myList))
print(myList2)