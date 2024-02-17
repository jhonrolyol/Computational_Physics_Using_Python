# Computational Physics Lecture 4, Introduction to Matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,20,0.1)
y = (10**x)*(np.cos(x)**2)
print(y)

plt.plot(x,y)
plt.yscale("log")
plt.xscale("log")
plt.savefig("figures/plot4.pdf")
plt.show()








