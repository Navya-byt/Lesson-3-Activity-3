def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print("The factorial of 0",factorial(0))
print("The factorial of 1",factorial(1))
print("The factorial of 3",factorial(3))
print("The factorial of 9",factorial(9))