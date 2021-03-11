# Adding vectors using Python
import numpy as np   

vector1 = np.array([[10],[3],[21]])
vector2 = np.array([[3],[2],[4]])

output = vector1 + vector2
print(output)

"""

gives a result:

[[13]
 [ 5]
 [25]]

which is the component-wise sum of the elements of each vector

"""