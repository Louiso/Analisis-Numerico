import numpy as np

def newMatriz(A,B):
    (ra,ca) = A.shape
    (rb,cb) = B.shape
    C = np.zeros([ra+rb,ca+cb])
    C[:ra,:ca] = A[:,:]
    C[ra:,ca:] = B[:,:]
    print C

A = np.arange(10).reshape(2,5)
B = np.arange(9).reshape(3,3)
print A
print B
newMatriz(A,B)
