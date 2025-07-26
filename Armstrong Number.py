anum = int(input("Enter a Number: "))
sum = 0
temp = anum
while temp>0:
    digit = temp%10
    sum+=digit**3
    temp//=10
if anum == sum:
    print(anum,"Is an Armstrong Number")
else:
    print(anum,"It is not an Armstrong Number")
