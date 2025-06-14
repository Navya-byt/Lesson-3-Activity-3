height = int(input("Enter your height in cms"))
weight = int(input("Enter your weight in kgs"))
BMI = weight/(height/100)**2
print("Your BMI is:",BMI)
if BMI <= 19:
    print("You are under weight")
elif BMI <= 25:
    print("You are healthy!")
elif BMI <= 30:
    print("You are over weight")
elif BMI <= 35:
    print("You are severly over weight!!")
elif BMI <= 45:
    print("You are obesse!!")
else:
    print("YOU ARE SEVERLY OBESSE!!!!!")
