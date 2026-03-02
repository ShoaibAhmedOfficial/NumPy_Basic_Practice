import numpy as np
x= np.matrix([[1,2],[1,2]])
x1= np.matrix([[1,2],[1,2]])
print(x*x1)
print(x.dot(x1))

y= np.array([[1,2,3],[1,2,3]])
print(y*y)

# Transpose
x=np.matrix([[1,2,3],[4,5,6]])
print(np.transpose(x))
print(x.T)

# Swapaxes
x=np.matrix([[1,2,3],[4,5,6]])
print(np.swapaxes(x,0,1))

# Inverse
x=np.matrix([[1,2],[4,5]])
print(np.linalg.inv(x))

# power
x=np.matrix([[1,2],[4,5]])
print(np.linalg.matrix_power(x,2))
print(np.linalg.matrix_power(x,0))
print(np.linalg.matrix_power(x,-2))

# Dterminate
x=np.matrix([[1,2],[4,5]])
print(np.linalg.det(x))