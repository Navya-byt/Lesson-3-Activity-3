medic_cause = input("Do you have a medical condition Y or N")
attendence = int(input("Enter attendence of the student"))
if medic_cause == "Y":
    print("You are allowed!!!")
else:
    if attendence >= 75:
        print("You are allowed!!!")
    else:
        print("You are not allowed")