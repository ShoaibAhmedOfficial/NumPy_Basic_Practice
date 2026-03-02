import numpy as np

x= np.array([1,2,3,4])

print(x)
# the answer given in array

y=[1,2,3,4,5]
print(y)
# the answer is given in list
z=np.array(y)
print(z)

l=[]
for i in range(1,5):
    int1=int(input("enter: "))
    l.append(int1)

print(np.array(l))

ar2=np.array([[1,2,3,4],[2,34,4,3]])
print(ar2)
print(ar2.ndim)