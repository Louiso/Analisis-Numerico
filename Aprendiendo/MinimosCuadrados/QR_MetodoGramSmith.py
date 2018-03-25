import numpy as np

def FactorizacionQR(A):
    (m,n) = A.shape
    Q = np.empty_like(A)
    Q[:,:] = A[:,:]
    R = np.zeros([n,n])
    R[0,0] = np.sqrt(np.dot(Q[:,0],Q[:,0]))
    Q[:,0] /= R[0,0]
    for j in range(1,n):
        y = np.empty_like(Q[:,j])
        y[:] = Q[:,j]
        for i in range(j):
            R[i,j] = np.dot(Q[:,i],Q[:,j])
            y -= Q[:,i]*R[i,j]
        R[j,j] = np.sqrt(np.dot(y,y))
        Q[:,j] = y/R[j,j]
    return Q,R

A = np.array([
    [1,0,1,2,1],
    [0,1,1,1,0],
    [1,1,0,0,0]
],dtype = float )

A = A.T

(Q,R) = FactorizacionQR(A)

print A
print
print Q.dot(R)
