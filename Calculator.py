def add(P,Q):
    return P + Q
def sub(P,Q):
    return P - Q
def Multi(P,Q):
    return P * Q
def divide(P,Q):
    return P/Q
print("Please Select The Operation")
print("A.Add")
print("B.sub")
print("C.Multi")
print("D.Divide")
choice = input("Please Enter Choice(A\B\C\D):")
num_1 = int(input("Please Enter The First Number"))
num_2 = int(input("Please Enter The Second Number"))
if choice == 'A':
    print(num_1,"+",num_2,"=", add(num_1,num_2))
elif choice == 'B':
    print(num_1,"-",num_2,"=", add(num_1,num_2))
elif choice == 'c':
    print(num_1,"*",num_2,"=", add(num_1,num_2))
elif choice == 'D':
    print(num_1,"/",num_2,"=", add(num_1,num_2))
else:
    print("This is an invalid input")
