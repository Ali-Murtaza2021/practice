classheld = int(input("Enter Held classes >>>"))
classattend = int(input("How many classes have you attended ? >>>"))

per = classattend/classheld*100
print("Your percentage is: ",per,"%")
 
if per<75:
    medicalissue = input("Do you have any medical issue ? [Y or N]>>>")
    if medicalissue == 'Y':
        print("The student is allowed",per)
    
    else:
        print("The student is not allowed",per)
else:
    print("The student is allowed",per)
