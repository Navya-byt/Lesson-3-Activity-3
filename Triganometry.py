import random
import math

#Pick a random angle
angle = random.randint(0, 360)

#Convert to radians
radians = math.radians(angle)

#Calculate sin, cos, tan
sin_val = math.sin(radians)
cos_val = math.cos(radians)
tan_val = math.tan(radians)

#Print results
print("Angle (degrees):", angle)
print("sin:", sin_val)
print("cos:", cos_val)
print("tan:", tan_val)

