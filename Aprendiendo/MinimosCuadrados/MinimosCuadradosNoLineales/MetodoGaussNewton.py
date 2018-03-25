import numpy as np
from numpy import linalg as la

def dot(R,x):
    (rR,cR) = R.shape
    C = np.empty_like(R)
    for i in range(rR):
        C[i,0] = R[i,0](x)
    return C

def d(r,i):
    def dr(x):
        h = 1.E-4
        xih = np.empty_like(x)
        xih[:,:] = x[:,:]
        xih[i,0] += h
        return (r(xih)-r(x))/h
    return dr
#
def H(r,x):
    (rx,cx) = x.shape
    H = np.zeros([rx,rx])
    for i in range(rx):
        for j in range(rx):
            H[i,j] = d(d(r,i),j)(x)
    return H

def J(R,x):
    (rR,cR) = R.shape
    (rx,cx) = x.shape
    J = np.zeros([rR,rx])
    for i in range(rR):
        for j in range(rx):
            J[i,j] = d(R[i,0],j)(x)
    return J

efe = lambda x: x[0,0]*x[0,0]
#El tamano de mi entrada sera 2
R = np.array([
    [lambda x: x[0,0]+2*x[1,0]],
    [lambda x: x[0,0]*x[0,0]-x[1,0]],
    [lambda x: x[0,0]*x[1,0]]
])

#Numero de funcion:
nr = 0
#Derivada respecto de
dx = 0
dy = 1

x = np.array([
    [4],
    [2]
],dtype=float)

# print d(d(R[nr,0],dx),dy)(x)
#
# print H(R[2,0],x)
#
# print J(R,x)
#
# print dot(R,x)

iter = 10
A = None
for k in range(iter):
    A = J(R,x)
    Rx = dot(R,x)
    ATA = A.T.dot(A)
    ATRx = -A.T.dot(Rx)
    v = np.linalg.inv(ATA).dot(ATRx)
    x = x + v

print A
