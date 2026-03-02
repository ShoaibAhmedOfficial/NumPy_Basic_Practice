import numpy as np

x=np.array([1,2,3,4])

copy= x.copy()
x[2]=9
print(x)
print(copy)

y=np.array([9,8,7,6,5])
view=y.view()
y[2]=9
print(y)
print(view)