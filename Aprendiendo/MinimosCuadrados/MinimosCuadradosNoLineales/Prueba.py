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

e = np.exp(1)
#El tamano de mi entrada sera 2
R = np.array([
    [lambda x: e**(x[0,0]-2*x[1,0]) - 0.5],
    [lambda x: e**(x[0,0]-x[1,0])   - 1],
    [lambda x: e**(x[0,0])          - 2],
    [lambda x: e**(x[0,0]+x[1,0])   - 4]
])

x = np.array([
    [1],
    [1]
],dtype=float)


iter = 10

A = None
for k in range(iter):
    A = J(R,x)
    Rx = dot(R,x)
    ATA = A.T.dot(A)
    ATRx = -A.T.dot(Rx)
    v = np.linalg.inv(ATA).dot(ATRx)
    x = x + v
    print x
    print

print x
