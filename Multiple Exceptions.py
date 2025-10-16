try:
    num1,num2=eval(input("Enter 2 numbers seperated by a comma"))
    result = num1/num2
    print("result is: ", result)
except ZeroDivisionError:
    print("Division by 0 is error")
except SyntaxError:
    print("Comma is missing")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what!")