Num = int(input("Enter a number: ")) #User input for base
Power = int(input("Enter a power: "))#User iput for exponent
#Intializing the Result
Result = 1 
#Iterates for i=1 to i=power
for i in range(Power):
  Result = Result * Num
  #Prints the Number to the given Power
print("Result:",  Result)

