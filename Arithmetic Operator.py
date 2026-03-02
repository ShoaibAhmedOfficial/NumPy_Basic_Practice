import numpy as np
var = np.array([1,2,3,4])
varadd1 = var + 3
var = np.add(var,3)
print(varadd1,var)

var1 = np.array([1,2,3,4])
var2 =np.array([6,4,3,2])
varadd2 = var1 + var2
var3= np.add(var1,var2)
print(varadd2,var3)

var = np.array([1,2,3,4])
varadd1 = var - 3
var2=np.subtract(var,3)
print(varadd1,var2)

var = np.array([1,2,3,4])
varadd1 = var * 3
var2=np.multiply(var,3)
print(varadd1,var2)

var = np.array([1,2,3,4])
varadd1 = var / 3
var2= np.divide(var,3)
print(varadd1,var2)

var = np.array([1,2,3,4])
varadd1 = var % 3
var2=np.mod(var,3)
print(varadd1,var2)

var = np.array([1,2,3,4])
varadd1 = var ** 3
var2 = np.power(var,3)
print(varadd1,var2)

var = np.array([1,2,3,4])
varadd1 = 1/var
var2=np.reciprocal(var)
print(varadd1,var2)

var21= np.array([[1,2,3],[1,2,3]])
var22=np.array([[1,2,3],[1,2,3]])
print(var21)
print()
print(var22)
print()
var23=var21+var22
print(var23)

var21= np.array([[1,2,3],[1,2,3]])
var22=np.array([[1,2,3],[1,2,3]])
print(var21)
print()
print(var22)
print()
var23=var21-var22
print(var23)

var21= np.array([[1,2,3],[1,2,3]])
var22=np.array([[1,2,3],[1,2,3]])
print(var21)
print()
print(var22)
print()
var23=var21*var22
print(var23)

var21= np.array([[1,2,3],[1,2,3]])
var22=np.array([[1,2,3],[1,2,3]])
print(var21)
print()
print(var22)
print()
var23=var21/var22
print(var23)

var21= np.array([[1,2,3],[1,2,3]])
var22=np.array([[1,2,3],[1,2,3]])
print(var21)
print()
print(var22)
print()
var23=var21%var22
print(var23)

var21= np.array([[1,2,3],[1,2,3]])
var22=np.array([[1,2,3],[1,2,3]])
print(var21)
print()
print(var22)
print()
var23=var21**var22
print(var23)

var21= np.array([[1,2,3],[1,2,3]])
var22=np.array([[1,2,3],[1,2,3]])
print(var21)
print()
print(var22)
print()
var23=var21/var22
print(var23)