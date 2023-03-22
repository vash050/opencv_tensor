import numpy as np

my_array = np.array([[1, -1, 2, 3], [1, 2, -3, 0], [-2, 4, 0, 6], [3, 0, 0, 3]])
det = np.linalg.det(my_array)
print(det)
