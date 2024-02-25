#Computational Physics Lecture 5, Round-off and Truncation Errors

import math
x = 1.0
y = 1.0+1e-15*math.sqrt(2)
dt = 1e-15*math.sqrt(2)
dn = y - x
print(dt)
print(dn)
