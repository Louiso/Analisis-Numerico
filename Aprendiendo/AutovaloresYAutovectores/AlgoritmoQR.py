import numpy as np

def norm(x):
    return np.sqrt(x.T.dot(x))

A = np.array([
    [ 5,-2, 0],
    [-2, 3,-1],
    [ 0,-1, 1]
],dtype=float)


def Mstack(A,B):
    (ra,ca) = A.shape
    (rb,cb) = B.shape
    C = np.zeros([ra+rb,ca+cb])
    C[:ra,:ca] = A[:,:]
    C[ra:,ca:] = B[:,:]
    return C

def sgn(x):
    if x<0:
        return -1
    else :
        return 1
def QR(A):
    (r,c) = A.shape
    R = np.empty_like(A)
    R[:,:] = A[:,:]
    Q = np.eye(r)
    for j in range(c):
        #Matriz de householder
        x = np.zeros([r-j,1])
        x[:,0] = R[j:,j]
        w = np.zeros_like(x)
        w[0,0] = -sgn(x[0,0])*norm(x)
        # w[0,0] = norm(x)
        v = x-w
        # if v[0,0] == 0 :
        #     break
        P = v.dot(v.T)/(v.T.dot(v))
        I = np.eye(len(v))
        H = I - 2*P
        #Fin de matriz householder
        I = np.eye(j)
        H = Mstack(I,H)
        Q = Q.dot(H)
        R = H.dot(R)
    return Q,R

def QR2(A):
    (m,n) = A.shape
    Q = np.empty_like(A)
    Q[:,:] = A[:,:]
    R = np.zeros([n,n])
    R[0,0] = np.sqrt(np.dot(Q[:,0],Q[:,0]))
    Q[:,0] /= R[0,0]
    for j in range(1,n):
        for i in range(j):
            R[i,j] = np.dot(Q[:,i],Q[:,j])
            Q[:,j] -= Q[:,i]*R[i,j]
        R[j,j] = np.sqrt(np.dot(Q[:,j],Q[:,j]))
        Q[:,j]/=R[j,j]
    return Q,R

def AlgoritmoQR(A):
    (m,n) = A.shape
    Q = np.eye(m)
    R = np.empty_like(A)
    R[:,:] = A[:,:]
    Qbar = np.empty_like(Q)
    Qbar[:,:] = Q[:,:]
    for i in range(22):
        (Q,R) = QR2(R.dot(Q))
        Qbar = Qbar.dot(Q)
    autovalores = np.diag(R*Q)
    autovectores = Qbar
    return autovalores,autovectores

# print A
(eigva,eigve) = AlgoritmoQR(A)
print eigva
print eigve

#
print 'Respuesta'
B = np.linalg.eig(A)
print np.sqrt(B[0])
print B[1]
