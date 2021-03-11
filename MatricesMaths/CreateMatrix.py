# Creating a matrix in Python
# there is no built in type for a matrix
# we can use a list of lists instead

mylist = [5,4,1,2,7]

print(type(mylist))

print(mylist)

mymatrix = [
            [5,4,1,2,7],
            [4,8,6,9,0],
            [2,4,8,0,3],
            ]

print(type(mymatrix))
print(mymatrix)

# use a numpy array instead
import numpy as np

myarray = np.array([[5,4,1,2,7],
                    [4,8,6,9,0],
                    [2,4,8,0,3]])


print(type(myarray))
print(myarray)

# can also use np.matrix to do the same thing but this is to be deprecated -- so use np.array