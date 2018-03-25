import numpy as np

def norm(x):
    return np.sqrt(x.T.dot(x))

A = np.array([
    [ 4, 2, 2, 1],
    [ 2,-3, 1, 1],
    [ 2, 1, 3, 1],
    [ 1, 1, 1, 2]
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
def Tridiagonal(A):
    (r,c) = A.shape
    R = np.empty_like(A)
    R[:,:] = A[:,:]
    Q = np.eye(r)
    for j in range(c-2):
        #Matriz de householder
        x = np.zeros([r-j,1])
        x[:,0] = R[j:,j]
        print "x : \n",x
        w = np.zeros_like(x)
        w[0,0] = x[0,0]
        w[1,0] = -sgn(x[1,0])*norm(x[1:,0])
        print "w : \n",w
        # w[0,0] = norm(x)
        v = x-w
        print "v : \n",v
        # if v[0,0] == 0 :
        #     break
        P = v.dot(v.T)/(v.T.dot(v))
        print "P : \n",P
        I = np.eye(len(v))
        H = I - 2*P
        #Fin de matriz householder
        I = np.eye(j)
        H = Mstack(I,H)
        print "H : \n",H
        R = H.dot(R).dot(H)
        print "R :"
        print R


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

Tridiagonal(A)
