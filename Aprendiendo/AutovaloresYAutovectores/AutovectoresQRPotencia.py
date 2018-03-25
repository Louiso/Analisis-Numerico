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
