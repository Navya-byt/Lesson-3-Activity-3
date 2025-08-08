Rows = int(input("Please Enter the Total No. of Rows"))
Num = 1
print("Floyd's Triangle")
for i in range(1,Rows+1):
    for j in range(1,i+1):
        print(Num, end= "")
        Num = Num+1
    print()