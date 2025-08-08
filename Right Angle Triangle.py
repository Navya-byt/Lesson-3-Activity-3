print("Half pyramid pattern of stars(*)")
n = int(input("Enter the Number of Rows"))
for i in range (n):
    for j in range (i+1):
        print("*",end = "")
    print()
