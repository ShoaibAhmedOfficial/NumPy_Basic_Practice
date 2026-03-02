import numpy as np
# Insert
x=np.array([1,2,3,9])
y=np.insert(x,3,5)
z=np.append(x,10)
print(y)
print(z)

x=np.array([[1,2,4],[3,9,7]])
y=np.insert(x,2,5,0)
z=np.append(x,[[10,11,15]],0)
print(y)
print(z)

# Delete
x=np.array([1,2,3,9])
y=np.delete(x,2)
print(y)