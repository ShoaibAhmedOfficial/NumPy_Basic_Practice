import numpy as np

x=np.array([1,2,3,4,5])

for i in x:
    print(i)


x=np.array([[1,2,3,4,5],[6,7,8,9,10]])

for i in x:
    print(i)

for k in x:
    for i in k:
        print(i)

x=np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])

for i in x:
    print(i)

for j in x:
    for k in j:
        for i in k:
            print(i)
print()


x=np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])

for i in x:
    print(i)

for j in np.nditer(x):
    print(j)
for i in np.nditer(x,flags=['buffered'],op_dtypes=["S"]):
    print(i)

x=np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])

for i in x:
    print(i)

for j,d in np.ndenumerate(x):
    print(j,d)