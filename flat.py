import numpy as np

def flat_matrix(matrix_3D):
    """
    Flatten matrix function
    Parameters:
        matrix_3D (numpy array)
    Returns:
        array_1D (numpy array)
    """
    return matrix_3D.reshape(-1)


arr = np.array([
                [[1, 2],
                 [3, 4]],

                [[5, 6],
                 [7, 8]] 
                 ])

# Prepare matrix by Input 
print("Enter Dimensions of 3D Matrix:")
n = int(input("Enter N:"))
m = int(input("Enter M:"))
p = int(input("Enter P:"))

#initalize a 3D matrix by the input parameters
np.zeros([n,m,p])
print("Enter the entries in a single line (separated by space): ")

#slice the input and map it into list
entries = list(map(int, input().split()))

#put the the list in the np.array
matrix = np.array(entries).reshape(n,m,p)
print("Before calling the function")
print(matrix)


flatten = flat_matrix(matrix)

#print the output
print("After calling the function")
print(flatten)
