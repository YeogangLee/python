import numpy as np

arr = [1,2,3]
arr_np = np.array(arr)

arr_np = arr_np % 2

# 똑같은 배열인데, 쉼표가 안 보이면, numpy 배열이다.
print(arr_np)
