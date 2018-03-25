import numpy as np
from numpy import linalg as la
def copyArray(a,b):
    for i in range(len(b)):
        a[i]=b[i]

#Crear una vector donde cada elemento sea una funcion

def g1(x):
    return (x[0]**2 - x[1]**2- x[0]-3)/3
def g2(x):
    return (-x[0] + x[1]-1)/3

G = np.array([g1,g2])
#
# x = np.array(
#     [1,2]
# , dtype=float)
# # print(F[0](x))
#
# def f(x):
#     return x[0]**2 + x[1]

def d(f,i):
    def df(x):
        h = 10**(-6)
        xih = np.zeros([len(x)])
        copyArray(xih,x)
        xih[i] = xih[i] + h
        return (f(xih)-f(x))/h
    return df
# Imprime la derivadas parciales
# print(d(f,0)([2,3]))
#Quiero que me bote un array
# print(f)
def mult(F,x):
    if len(F)!=len(x):
        return None
    x_new = np.zeros([len(x)])
    for i in range(len(F)):
        x_new[i] = F[i](x)
    return x_new
# print(mult(F,x))

#Definiendo la matriz de Jacoby

def D(F,x):
    n = len(x)
    DF = np.zeros((n,n),dtype = float)
    for i in range(n):
        for j in range(n):
            DF[i,j] = d(F[i],j)(x)
    return DF

# print(la.inv(D(F,x)).dot(D(F,x)))

def PuntoFijo(G):
    n = len(G)
    x = np.random.random([n])
    x_new = mult(G,x)
    err = x - x_new
    err = la.norm(err)
    x = x_new
    eps = 10**(-5)
    while err > eps:
        x_new = mult(G,x)
        err = x - x_new
        err = la.norm(err)
        x = x_new
    return x

x = PuntoFijo(G)
print(x,mult(G,x))
