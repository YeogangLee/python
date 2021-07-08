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

# X2 = [2, 2, 2, 2, 2, 2]
# X2 = [5, 5, 5, 5, 5, 5]
X2 = [2/10, 2/10, 2/10, 2/10, 2/10, 2/10]
Y2 = [0, 2, 4, 6, 8, 10]
Z2 = ds.get_prices("LG전자")

# X3 = [4, 4, 4, 4, 4, 4]
X3 = [4/10, 4/10, 4/10, 4/10, 4/10, 4/10]
Y3 = [0, 2, 4, 6, 8, 10]
Z3 = ds.get_prices("SK")

# X4 = [6, 6, 6, 6, 6, 6]
X4 = [6/10, 6/10, 6/10, 6/10, 6/10, 6/10]
Y4 = [0, 2, 4, 6, 8, 10]
Z4 = ds.get_prices("SK하이닉스")

# X5 = [8, 8, 8, 8, 8, 8]
X5 = [8/10, 8/10, 8/10, 8/10, 8/10, 8/10]
Y5 = [0, 2, 4, 6, 8, 10]
Z5 = ds.get_prices("SK텔레콤")

min_z = min(Z)
max_z = max(Z)
Z[:] = [(ele - min_z)/(max_z-min_z) for ele in Z]

min_z2 = min(Z2)
max_z2 = max(Z2)
Z2[:] = [(ele - min_z2)/(max_z2-min_z2) for ele in Z2]

min_z3 = min(Z3)
max_z3 = max(Z3)
Z3[:] = [(ele - min_z3)/(max_z3-min_z3) for ele in Z3]

min_z4 = min(Z4)
max_z4 = max(Z4)
Z4[:] = [(ele - min_z4)/(max_z4-min_z4) for ele in Z4]

min_z5 = min(Z5)
max_z5 = max(Z5)
Z5[:] = [(ele - min_z5)/(max_z5-min_z5) for ele in Z5]



ax.plot(X, Y, Z)
ax.plot(X2, Y2, Z2)
ax.plot(X3, Y3, Z3)
ax.plot(X4, Y4, Z4)
ax.plot(X5, Y5, Z5)

plt.show()
