# Get decimal number from user
 
num = int(input("Enter a decimal number: "))
n = num
binary = ""

# Outer loop: keep dividing the number until it becomes 0
while n > 0:
    rem = n % 2  # Get remainder (0 or 1)

    # Inner loop (just to show nested loop usage)
    count = 0
    while count < 1:
        binary = str(rem) + binary
        count += 1

    n = n // 2  # Move to next digit

# Print the result
print("Binary of", num, "is:", binary)
