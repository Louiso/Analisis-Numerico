import numpy as np
import matplotlib.pyplot as plt

#Calcula una matriz que representa a un conjunto de vectores ortonormales
def MetodoDeGranSmith(V):
    #r denota el tamano de cada vector , c denota cuantos vectores tengo
    (r,c) = V.shape
    U = np.zeros_like(V)
    u = np.zeros_like(V)
    U[:,0:1] = V[:,0:1]
    u[:,0:1] = U[:,0:1]/np.sqrt(U[:,0:1].T.dot(U[:,0:1]))
    for i in range(1,c):
        S = np.zeros([r,1])
        for j in range(i):
            uu = u[:,j:j+1]
            vv = V[:,i:i+1]
            S+= uu*uu.T.dot(vv)
        U[:,i:i+1] = V[:,i:i+1] - S
        uu =  U[:,i:i+1]
        u[:,i:i+1] = U[:,i:i+1]/np.sqrt(U[:,i:i+1].T.dot(U[:,i:i+1]))
    return u

V = np.array([
    [1,0,0,2],
    [0,1,1,1],
    [1,2,1,0]
],dtype=float)
V = V.T
print  'Los vectores son : '
print V[:,0] , V[:,1]

O = MetodoDeGranSmith(V)
print O[:,0].T.dot(O[:,1])

O = O.T
print O

#
