import numpy as np
import matplotlib.pyplot as plt

def metodoPotencia(A,iter):
    (r,c) = A.shape
    x = np.random.random([r,1])
    for i in range(iter):
        u = x/np.sqrt(x.T.dot(x))
        x = A.dot(u)
        lnd = u.T.dot(A).dot(u)
    return (lnd, x/np.sqrt(x.T.dot(x)))

A = np.array([
    [1,2,3],
    [12,3,4],
    [1,2,4]
])

(lnd , v ) = metodoPotencia(A,100)
print lnd
print v
print A.dot(v)
print lnd*v


#
