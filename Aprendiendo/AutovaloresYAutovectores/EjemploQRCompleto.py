import numpy as np
def factor_QR(A):
  (m,n) = np.shape(A)
  Q = np.eye(m,m)
  R = np.array(A)
  for i in range(n-1):
    A1 = R[i:,i]
    r11 = np.sign(A1[0])*np.linalg.norm(A1)
    e1 = np.zeros((m-i,))
    e1[0] = 1
    v =  A1 + r11*e1
    v = v/np.linalg.norm(v)
    P1 = np.eye(m,m)
    P1[i:,i:] = (np.eye(m-i,m-i)-
                  2*v[:,None].dot(v[:,None].T))
    R = P1.dot(R)
    Q = P1.dot(Q)
  return(Q.T,R)
def Householder(A):
    [n,m] = np.shape(A)
    T=np.zeros((n,m))
    T[:,:]=A[:,:]
    for k in range(n-2):
        print '*'*20
        #toma el elemento derecho de la diagonal y sacamos la norma
        s = np.linalg.norm(T[k+1:,k])
        if T[k+1,k] < 0.0: s = -s #si el elemento es negativo entonces s tambn
        print "s : ",s
        r = np.sqrt(2*s*(T[k+1,k]+s))
        print "r : ",r
        W =np.zeros((n,))
        W[k+1]=(T[k+1,k]+s)/r
        W[k+2:] = T[k+2:,k]/r
        V = np.zeros((n,))
        V[k+1:]=np.dot(T[k+1:,k+1:],W[k+1:])
        print "V = \n",V
        print "W = \n",W
        c = np.dot(W[k+1:],V[k+1:])
        print "c=",c
        Q =np.zeros((n,))
        Q[k+1:]=V[k+1:]-c*W[k+1:]
        print "Q=",Q
        v=W[k+1:]
        u=Q[k+1:]
        T[k,k+1] = T[k+1,k] = -s
        T[k+2:,k] = T[k,k+2:] = 0
        T[k+1:,k+1:] = T[k+1:,k+1:] \
        - 2*v[:,None].dot(u[:,None].T)
        - 2*u[:,None].dot(v[:,None].T)
        print "T = \n", T
    return T
def MetodoQR(A,eps):
    [n,m] = np.shape(A)
    D=np.zeros((m,))
    B=np.zeros((m,m))
    B[:,:]=A[:m,:m]
    while m>0:
        err=eps
        l=B[-1,-1]
        while err>=eps:
            (Q,R) = factor_QR(B)
            B=R.dot(Q)
            err=abs(B[-1,-1]-l)
            l=B[-1,-1]
        D[m-1]=B[-1,-1]
        m=m-1
        B=np.zeros((m,m))
        B[:,:]=A[:m,:m]
    return D
if __name__ == "__main__":
    A=np.array([[4,2,2,1],[2,-3,1,1]
                ,[2,1,3,1],[1,1,1,2]])
    print A
    eps=1E-5
    D = MetodoQR(A,eps)
    print D
    Householder(A)
