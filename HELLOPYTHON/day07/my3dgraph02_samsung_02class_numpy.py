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
Z = ds.get_prices("삼성전자")

X2 = [2, 2, 2, 2, 2, 2]
Y2 = [0, 2, 4, 6, 8, 10]
Z2 = ds.get_prices("LG전자")

X3 = [4, 4, 4, 4, 4, 4]
Y3 = [0, 2, 4, 6, 8, 10]
Z3 = ds.get_prices("SK")

X4 = [6, 6, 6, 6, 6, 6]
Y4 = [0, 2, 4, 6, 8, 10]
Z4 = ds.get_prices("SK하이닉스")

X5 = [8, 8, 8, 8, 8, 8]
Y5 = [0, 2, 4, 6, 8, 10]
Z5 = ds.get_prices("SK텔레콤")

z_np = np.array(Z) / Z[0]
z_np2 = np.array(Z2) / Z2[0]
z_np3 = np.array(Z3) / Z3[0]
z_np4 = np.array(Z4) / Z4[0]
z_np5 = np.array(Z5) / Z5[0]

ax.plot(X, Y, Z)
# ax.plot(X2, Y2, Z2)
# ax.plot(X3, Y3, Z3)
# ax.plot(X4, Y4, Z4)
# ax.plot(X5, Y5, Z5)

# ax.plot(X, Y, z_np)
# ax.plot(X2, Y2, z_np2)
# ax.plot(X3, Y3, z_np3)
# ax.plot(X4, Y4, z_np4)
# ax.plot(X5, Y5, z_np5)

plt.show()
