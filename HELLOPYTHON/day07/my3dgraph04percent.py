import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import mariadb
from day07.mydao import DaoStock
import numpy as np

ds = DaoStock()
list_names = ds.get_all_names()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for idx, name in enumerate(list_names) :
    x = np.zeros((6)) + idx
    y = range(6)
    z = ds.get_prices(name)
    z_np = np.array(z)
    if z_np[0] == 0 :
        continue
    z_np = z_np / z_np[0]
    
    ax.plot(x, y, z_np)

plt.show()
