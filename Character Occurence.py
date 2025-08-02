lettr = input("Enter an word: ")
char = input("Enter a character: ")
i = 0
count = 0
while (i<len(lettr)):
    if(lettr[i] == char):
        count = count + 1
    i = i+1
print("The total Number of times", char,"has occured = ", count)