import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import mariadb
from day07.mydao import DaoStock
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

X2 = [1, 1, 1, 1, 1, 1]
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

ax.plot(X, Y, Z)
ax.plot(X2, Y2, Z2)
ax.plot(X3, Y3, Z3)
ax.plot(X4, Y4, Z4)
ax.plot(X5, Y5, Z5)

plt.show()
