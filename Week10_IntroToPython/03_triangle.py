#import the math package
import math

# tell the user the purpose of the program
print("The purpose of this program is to calculate the length of a hypotenuse of a right triangle.")

# get first side
side1 = float(input("First side: "))

# get second side
side2 = float(input("Second side: "))

# calculate third side
# a^2 + b^2 = c^2
sum_of_squares = side1*side1 + side2*side2
c = math.sqrt(sum_of_squares) #You'll need to find some online documentation for this!

# print output to the user
print("The third side of the tiangle has a length of " + str(c))
