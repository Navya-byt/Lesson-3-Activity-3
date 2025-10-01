import math   # To Use the Value of pi

# Function to Calculate the Circumference
def circumference(radius):
    return 2 * math.pi * radius

#Ask the user for radius
r = float(input("Enter the radius of the circle: "))

# Call the Function and Display the Result
c = circumference(r)
print("The circumference of the circle is:", c)