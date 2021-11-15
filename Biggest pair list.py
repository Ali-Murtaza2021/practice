list_a = [1,2,3,4,5]
list_b = [2,3,4,5,6,7,8,9]
for a , b in zip(list_a,list_b):
    if a > b:
        print (a)
    else:
        print (b)

