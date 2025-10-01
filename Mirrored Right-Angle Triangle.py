# Program: Mirrored Right-Angled Triangle

#Step 1: Ask user for number of rows
rows = int(input("Enter number of rows: "))

#Step 2: Outer loop for each row
for i in range(1, rows + 1):

    # Inner loop 1: Print Spaces
    for j in range(rows - i):
        print(" ", end="")

    # Inner loop 2: Print Stars
    for k in range(i):
        print("*", end="")

    # Move to the next line
    print()

