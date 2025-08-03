# Square Root Calculation in Python
# log of number 
# sin value of number
import math

def maths(n):
    return math.sqrt(n), math.log(n), math.sin(n)
x = int(input("Enter a number to calculate its square root: "))
root, log, sin = maths(x)
print(f"The square root of {x} is: {root}")
print(f"The log of {x} is: {log}")
print(f"The sin of {x} is: {sin}")