def multipleOf5(n):
    if(n % 5 == 0):
        return n
myList = [10, 25, 17, 9, 30, -5]
myList2 = list(filter(multipleOf5, myList))
print(myList2)