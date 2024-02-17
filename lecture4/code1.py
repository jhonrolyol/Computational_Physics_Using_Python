# Computational Physics Lecture 4, Introduction to Matplotlib

import matplotlib.pyplot as plt
#%matplotlib inline

plt.plot([1, 2, 3, 4],[1, 4, 9, 12], label = "Line", linewidth = 2, color = "g", linestyle = "--")
plt.xlabel("$x$ axis", size = 10)
plt.ylabel("$y$ axis", size = 10)
plt.legend()
plt.savefig("figures/plot1.pdf")
plt.show()


import numpy as np

#x = np.arange(0,20,1)
#x = np.arange(0,20.1,1)
x = np.arange(0,20,0.1)
y = np.cos(x)

plt.plot(x,y, label = "Oscilattion 1", linewidth = 3, color = "b")
plt.xlabel("$x$ axis", size = 15)
plt.ylabel("$\cos(x)$", size = 15)
plt.legend()
plt.savefig("figures/plot2.pdf")
plt.show()

y1 = np.exp(-x/10)*np.cos(x)
plt.plot(x,y1, label = "Oscillation 2", linewidth = 3, color = "r")
plt.xlabel("$x$ axis", size = 10)
plt.ylabel("$e^{-x/10}\cos(x)$", size = 10)
plt.legend()
plt.savefig("figures/plot3.pdf")
plt.show()

