import numpy as np

def flat_array(array_3D):
    return array_3D.reshape(-1)



arr = np.array([
                [[1, 2],
                 [3, 4]],

                [[5, 6],
                 [7, 8]] 
                 ])

print(flat_array(arr))
