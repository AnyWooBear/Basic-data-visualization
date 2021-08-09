import pandas as pd
from matplotlib import pyplot as plt

#We establish the data set
x = [4, 2, 7]
y = [3, 1, 5]
z = [1, 5, 3]

#we set the parameters
plt.plot(x, y)
plt.plot(x, z)

#we set the title and labels for the axis
plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y and z") 
plt.legend(["This is y", "This is z"])

#Show the graph
plt.show()