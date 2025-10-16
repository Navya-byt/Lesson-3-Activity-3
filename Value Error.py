try: 
    number = int(input("Enter a Number: "))
    print("The number entered is: ",number)
except ValueError as EX:
    print("Exception", EX)