import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mystock.mystock_dao import MystockDao 
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ds = MystockDao()
first_count = ds.get_first_day_count()[0]
last_count = ds.get_last_day_count()[0]

"""
first_x = np.zeros((first_count))
first_y = range(first_count)

for i in range(first_count) :    
    first_z = ds.get_first_day_list()
    z_np = np.array(first_z)
    if z_np[0] == 0 :
        continue
    z_np = z_np / z_np[0]

    ax.plot(first_x, first_y, z_np)


last_x = np.zeros((last_count)) + 1
last_y = range(last_count)

for i in range(last_count) :    
    last_z = ds.get_last_day_list()
    z_np2 = np.array(last_z)
    if z_np2[0] == 0 :
        continue
    z_np2 = z_np2 / z_np2[0]

    ax.plot(last_x, last_y, z_np2)
"""    
    
first_x2 = np.zeros((first_count))
first_y2 = range(first_count)
first_z2 = ds.get_first_day_list()
        
ax.plot(first_x2, first_y2, first_z2)

last_x2 = np.zeros((last_count))
last_y2 = range(last_count)
last_z2 = ds.get_last_day_list()
        
ax.plot(last_x2, last_y2, last_z2)



# ax.plot(x, y, z_np2)
plt.show()
