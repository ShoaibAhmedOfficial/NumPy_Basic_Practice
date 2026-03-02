import numpy as np

x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])

z =np.concatenate((x,y))

print(z)


x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])

z =np.concatenate((x,y),1)

print(z)

x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])

z =np.stack((x,y),1)
c =np.hstack((x,y))   # along row we use hstack
v =np.vstack((x,y))  #along column we use vstack
m =np.dstack((x,y)) #along height we use dstack
print(z)
print(c)
print(v)
print(m)

# Split

x=np.array([1,2,3,4,5,6])
y=np.array_split(x,3)
print(y)

x=np.array([[1,2],[3,4],[5,6]])
y=np.array_split(x,3)
m=np.array_split(x,3,1)
print(y)
print(m)