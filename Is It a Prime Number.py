uppr = int(input("Enter a number: "))
lowr = int(input("Enter a number: "))
print("Prime numbers between",uppr, "and", lowr, "are: ")
for num in range(lowr,uppr+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
            else:
                print(num)