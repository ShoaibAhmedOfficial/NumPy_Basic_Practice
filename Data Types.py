import numpy as np
var = np.array([1,2,3,4])
print("Data Type: ",var.dtype)

var1=np.array([1.0,2.2,32.2])
print("Data Type: ",var1.dtype)

var2=np.array(["A","b","c"])
print("Data Type: ",var2.dtype)

var3=np.array(["A","b","c",1,2,3,4,])
print("Data Type: ",var3.dtype)

x = np.array([1,2,3,4],dtype = np.int8)
print("Data Type: ",x.dtype)
print(x)


x1 = np.array([1,2,3,4],dtype = "f")
print("Data Type: ",x1.dtype)
print(x1)

x2 = np.array([1,2,3,4])

new=np.float32(x2)

print("Data Type: ",x2.dtype)
print("Data Type: ",new.dtype)
print(x2)
print(new)

x3 = np.array([1,2,3,4])
new1=x3.astype(float)
print(new1)
print(x3)
