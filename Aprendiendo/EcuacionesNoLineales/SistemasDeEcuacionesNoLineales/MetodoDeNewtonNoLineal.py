import numpy as np
from numpy import linalg as la
def copyArray(a,b):
    for i in range(len(b)):
        a[i]=b[i]

#Crear una vector donde cada elemento sea una funcion

def f1(x):
    return x[0] + x[1] + x[2] - 3
def f2(x):
    return x[0]**2 + x[1]**2 + x[2]**2 - 5
def f3(x):
    return np.exp(x[0]) + x[0]*x[1] - x[0]*x[2] -1

F = np.array([f1,f2,f3])
#
# x = np.array(
#     [1,2]
# , dtype=float)
# # print(F[0](x))
#
# def f(x):
#     return x[0]**2 + x[1]

#Definiendo una derivada parcial respecto a uno de sus variables
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
#Definiendo una aplicacion del vector funcion con las variables
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

def MetodoNewtonNoLineal(F):
    n = len(F)
    x = np.random.random([n])
    x_new = x-la.inv(D(F,x)).dot(mult(F,x))
    err = x - x_new
    err = la.norm(err)
    eps = 10**(-16)
    while err > eps:
        x_new = x-la.inv(D(F,x)).dot(mult(F,x))
        err = x - x_new
        err = la.norm(err)
        x = x_new
    return x

x = MetodoNewtonNoLineal(F)
print(x,mult(F,x))
