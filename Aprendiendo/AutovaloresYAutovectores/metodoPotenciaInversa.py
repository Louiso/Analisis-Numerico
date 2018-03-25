import numpy as np
import matplotlib.pyplot as plt

def metodoPotenciaInversa(A,iter):
    (r,c) = A.shape
    x = np.random.random([r,1])
    for i in range(iter):
        u = x/np.sqrt(x.T.dot(x))
        invA = np.linalg.inv(A)
        x = invA.dot(u)
        lnd = u.T.dot(A).dot(u)
    return (lnd, x/np.sqrt(x.T.dot(x)))

A = np.array([
    [1,2,3],
    [12,3,4],
    [1,2,4]
])

(lnd , v ) = metodoPotenciaInversa(A,100)
print lnd
print v
print A.dot(v)
print lnd*v


#
