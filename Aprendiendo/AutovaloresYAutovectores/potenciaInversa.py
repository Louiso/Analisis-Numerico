import numpy as np

def potenciaInversa(A,X,eps,max_iter):
    l = 0
    num_iter = 0
    err = 1
    continuar = True
    while (num_iter<=max_iter) and continuar :
        #Y = A^-1(X) = (1/c)X
        Y = np.linalg.solve(A,X)
        m = np.max(np.abs(Y))
        c1 = m
        dc = np.abs(l-c1)
        Y = (1/c1)*Y
        dv = np.linalg.norm(X-Y)
        err = np.max([dc,dv])
        X = Y
        l = c1
        if err <= eps:
            continuar = False
        else:
            num_iter += 1
        pass
    V = X
    print("No. Iter. = {0:d}".format(num_iter))
    return(l,V)

A = np.array([
    [ 0,11,-5],
    [-2,17, 7],
    [-4,26,-10]
], dtype = 'f')

X0 = np.array([1,1,1], dtype = 'f').T
eps = 1E-5
max_iter = 100
(l,V) = potenciaInversa(A,X0,eps,max_iter)
