import numpy as np

def FactorizacionQR(A):
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

A = np.array([
    [ 1, 1],
    [-2, 4],
],dtype=float)

#Permite calcular los vectores propios en one!!!!
def ItrSmltNrmlizada(A):
    (r,c) = A.shape
    Q = np.eye(r)
    _A = np.empty_like(A)
    _A[:,:] = A[:,:]
    for i in range(50):
        (Q,R) = FactorizacionQR(_A.dot(Q))
        # print Q
        # print R
    print Q
    print np.diag(Q.T.dot(_A).dot(Q))

ItrSmltNrmlizada(A)

eig = np.linalg.eig(A)
print eig[0]
print eig[1]
