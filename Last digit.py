Per = int(input("Enter a number"))

if Per > 90:
    print("Grade A:",Per)
elif Per >80 and Per <=90:
        print("Grade B:",Per)
elif Per >=60 and Per <=80:
        print("Grade C:",Per)
elif Per <60:
        print("Grade D:",Per)
else:
    print("Error")
