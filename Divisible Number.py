print("Enter a numerator value")
numn = int(input())

print("Enter a denomenator value")
numd = int(input())

if numn%numd==0:
    print("\n"+ str(numn) + "is divisible by" + str(numd))
else:
    print("\n"+ str(numn) + "is not  divisible by" + str(numd))