#import the math package
import math
# tell the user the purpose of the program
print("The purpose of this program is to calculate the length of a hypotenuse of a right triangle.")
# get first side
side1 = float(input("Give me the first side of the triangle: "))
# get second side
side2 = float(input("Give me the second side of the triangle: "))
# calculate third side
# a^2 + b^2 = c^2
sum_of_squares = side1*side1 + side2*side2
c = math.sqrt(sum_of_squares)
# print output to the user
print("The third side of the tiangle has a length of " + str(c))
