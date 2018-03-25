import numpy as np

def norm(x):
    return np.sqrt(x.T.dot(x))

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
            R[i,j] = np.dot(Q[:,i],y)
            y -= Q[:,i]*R[i,j]
        R[j,j] = np.sqrt(np.dot(y,y))
        Q[:,j] = y/R[j,j]
    return Q,R
x = np.linspace(1,3,20)
print x
A = np.ones([20,3])

A[:,1] = x[:]
A[:,2] = x[:]**2
# A = np.array([
#     [1.0 ,0.0  ,0.0],
#     [1.0 ,1.525,2.3256249999999996],
#     [1.0 ,3.050,9.302499999999998 ],
#     [1.0 ,4.575,20.930625000000003],
#     [1.0 ,6.10 ,37.209999999999994],
#     [1.0 ,7.625,58.140625         ],
#     [1.0 ,9.150,83.72250000000001]
#
# ],dtype=float)

f = lambda x: x*np.log(x)

b = np.zeros([20,1])
b[:,0] = f(x[:])
# b = np.array([
#     [1.0],
#     [0.8617],
#     [0.7385],
#     [0.6292],
#     [0.5328],
#     [0.4481],
#     [0.3741]
# ])
#

(Q,R) = FactorizacionQR(A)

print "R : "
print R
print "QTb : "
print Q.T.dot(b)
print "c : "
c = np.linalg.inv(R).dot(Q.T).dot(b)
print  c
print norm(A.dot(c)-b)

#
