import numpy as np
# Indexing
var=np.array([1,2,3,4])
print(var[3])

var1=np.array([[9,8,7,6],[1,2,3,4]])
print(var1[1,-1])

var1=np.array([[[9,8,7,6],[1,2,3,4]]])
print(var1[0,0,-2])

# Slicing
x=np.array([1,2,3,4,5,6,7])
print(x)
print("2 to 5: ",x[:5])

y=np.array([[1,2,3,4,5,6],[11,12,13,14,15,16]])
print(y[1,2:])