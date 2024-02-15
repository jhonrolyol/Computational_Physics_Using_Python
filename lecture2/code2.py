# Computational Physics Lecture 2, Introduction to Python

'''
t = float(input("Enter temperature:"))
if t >= 100:
    print("Water is in gas state: ")
elif t >= 0 and t < 100:
    print("Water is in liquid state: ")
else:
    print("It is ice")
'''


t = float(input("Enter temperature:"))
if t >= 100:
    print("Water is in gas state: ")
elif t >= 0: # and t < 100:
    print("Water is in liquid state: ")
else:
    print("It is ice")

