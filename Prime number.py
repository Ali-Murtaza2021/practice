wd = int(input("Enter a working days"))
ab = int(input("Enter a absent days"))
per = ab/wd*100
if per < 75:
    print("Not allow to sit the exam",per)
else:
    print("Allow sit in the exam",per)
