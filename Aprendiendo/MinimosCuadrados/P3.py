import numpy as np

def norm(x):
    return np.sqrt(x.T.dot(x))

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

def Mstack(A,B):
    (ra,ca) = A.shape
    (rb,cb) = B.shape
    C = np.zeros([ra+rb,ca+cb])
    C[:ra,:ca] = A[:,:]
    C[ra:,ca:] = B[:,:]
    return C

def sgn(a):
    if a < 0:
        return -1
    else:
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
        v = x-w
        # print R
        # print x
        # print w
        P = v.dot(v.T)/(v.T.dot(v))
        I = np.eye(len(v))
        H = I - 2*P
        I = np.eye(j)
        H = Mstack(I,H)
        Q = Q.dot(H)
        R = H.dot(R)
    return Q,R
print A

Q,R = QR(A)

print "R : "
print R
print "QTb : "
print Q.T.dot(b)
# print "c : "
# print np.linalg.inv(R)#.dot(Q.T).dot(b)
# print "Q : \n", Q
# print "R : \n", R
# print Q.dot(R)
