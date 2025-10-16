import random
number = random.randint(1,10)
user=int(input("Guess a number between 1 and 10: "))
if user == number:
    print("Wow! You guessed right!")
else:
     print("Oops!The correct number was: ",number)