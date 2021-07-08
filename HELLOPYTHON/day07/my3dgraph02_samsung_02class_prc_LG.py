import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import mariadb
from day07.mydao import DaoStock
import numpy as np

ds = DaoStock()

conn = mariadb.connect(
    user="root",
    password="python",
    host="localhost",
    database="mypydb")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# X = list()
X = [0, 0, 0, 0, 0, 0]
Y = [0, 2, 4, 6, 8, 10]
Z = ds.get_prices("LG")

x = [0, 0, 0, 0, 0, 0]
y = [0, 2, 4, 6, 8, 10]
z = ds.get_prices("LG")
z_np = np.array(z)

z_np0 = z_np / z_np[0]
z_np1 = z_np / z_np[1]
z_np2 = z_np / z_np[2]
z_np3 = z_np / z_np[3]
z_np4 = z_np / z_np[4]
z_np5 = z_np / z_np[5]

x0 = [0, 0, 0, 0, 0, 0]
x1 = [1, 1, 1, 1, 1, 1]
x2 = [2, 2, 2, 2, 2, 2]
x3 = [3, 3, 3, 3, 3, 3]
x4 = [4, 4, 4, 4, 4, 4]
x5 = [5, 5, 5, 5, 5, 5]


min_z = min(Z)
max_z = max(Z)
Z[:] = [(ele - min_z)/(max_z-min_z) for ele in Z]

ax.plot(X, Y, Z)
# ax.plot(x0, y, z_np0)
# ax.plot(x1, y, z_np1)
# ax.plot(x2, y, z_np2)
# ax.plot(x3, y, z_np3)
# ax.plot(x4, y, z_np4)
# ax.plot(x5, y, z_np5)

plt.show()
