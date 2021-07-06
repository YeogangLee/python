# Standard import
import matplotlib.pyplot as plt
# Import 3D Axes 
from mpl_toolkits.mplot3d import axes3d
# Set up Figure and 3D Axes 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Get some 3D data
# X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Y = [2, 5, 8, 2, 10, 1, 10, 5, 7, 8]
# Z = [6, 3, 9, 6, 3, 2, 3, 10, 2, 4]

# X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# X = [0, 1]
# Y = [0, 2]
# Z = [0, 3]

X = [0, 0, 0, 0, 0, 0]
Y = [0, 2, 4, 6, 8, 10]
Z = [0, 3, 0, 0, 3, 0]

# Plot using Axes notation and standard function calls
ax.plot(X, Y, Z)
plt.show()