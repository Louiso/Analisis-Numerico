#El metodo de Jacoby no siempre funciona

import numpy as np


#Definicion de una multiplicacion normal
def mult(A,b):
    (ra, ca ) = A.shape
    rb = len(b)
    C = np.zeros((rb))
    for i in range(rb):
        C[i] = np.sum(A[i,:]*b)
    return C

def copyArray(a,b):
    for i in range(len(b)):
        a[i]=b[i]

    #Luego crearia las matrices D , E , F / A = D - E - F
    # D seria la matriz de la diagonal
    # E seria la matriz triangular inferior negativa
    # F seria la matriz triangular superior negativa
def GaussSeidel(AB):
    #Primero tomo el numero de filas y columnas
    (r,c) = AB.shape
    #Luego tomo el numero de filas y columnas de A
    n = r
    x = np.random.random([n])
    print('X-0\n')
    ep = 10**(-10)
    t = 0
    err = np.max(mult(AB[0:n,0:n],x)-AB[0:n,n])
    while np.abs(err)>ep:
        x_new = np.zeros([n])
        copyArray(x_new,x)
        for i in range(n):#i : 0 , ..... , n-1
            #DEFX
            E2X = -np.sum(AB[i,0:i]*x[0:i])
            F2X = -np.sum(AB[i,(i+1):n]*x_new[(i+1):n])
            # x_new[i] = (AB[i,n]+EX+FX)/AB[i,i]
            x[i] = (AB[i,n]+E2X+F2X)/AB[i,i]
        err = np.max(mult(AB[0:n,0:n],x)-AB[0:n,n])
        t = t + 1
    print(t)
    return x

A = np.array([
    [1,2,3],
    [4,2,3]
])
B = np.array([
    [1],
    [2],
    [3]
])
AB = np.array([
				[ 0.05,1, 1, 1],
				[1, 0.05, 1,0],
                [ 1, 1, 0.05, 0]
			],dtype = float)
print("\n")
print(AB)
print("\n")
print(GaussSeidel(AB))
