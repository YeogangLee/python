import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import pymysql
from day07.mydao import DaoStock
ds = DaoStock()

conn = pymysql.connect(user="root", password="python",
                       host="localhost", database="mypydb", charset='utf8')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = list() # []
Y = list()
Z = list()

idx = 0
for c_name in ds.retrieveAll() :
    X.clear()
    Y.clear()
    Z.clear()
    
    for i  in range(6) :
        X.append(idx)
        Y.append(i*2)
    Z = ds.get_prices(c_name)
    
    min_z = min(Z)
    max_z = max(Z)
    if (max_z - min_z) == 0 :
        Z[:] = [0 in Z]
    else :
        Z[:] = [(ele - min_z)/(max_z-min_z) for ele in Z]
    
    ax.plot(X, Y, Z)
    idx+=1
    
print(3)
plt.show()
