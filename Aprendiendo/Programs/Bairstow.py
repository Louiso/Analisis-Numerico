import numpy as np

def intercambio(M,i,j):
    temp = np.empty_like(M[j,:])
    temp[:] = M[j,:]
    M[j,:] = M[i,:]
    M[i,:] = temp

def eliminacionGausseana(A):
    (r,c) = A.shape
    n = r
    P = np.eye(n)
    #Proceso de eliminacion gausseana
    for j in range(n-1):
        #Aplica pivote parcial
        piv = j
        for k in range(j+1,n):
            if np.abs(A[k,j])>np.abs(A[piv,j]):
                piv = k
        intercambio(A,j,piv)
        intercambio(P,j,piv)
        #Fin pivote parcial
        for i in range(j+1,n):
            mij = A[i,j]/A[j,j]
            #eliminar las elementos de la columna j
            A[i,j:n] = A[i,j:n]-mij*A[j,j:n]
            A[i,j] = mij
    return P

def GaussSimple(AB):
    (r,c) = AB.shape
    n = r
    #Proceso de eliminacion gausseana
    for j in range(n-1):
        for i in range(j+1,n):
            mij = AB[i,j]/AB[j,j]
            #eliminar las elementos de la columna j
            AB[i,:] = AB[i,:]-mij*AB[j,:]
    #Proceso de sustitucion hacia atras
    x = np.zeros([n],dtype=float)
    x[n-1] = AB[n-1,n]/AB[n-1,n-1]
    for i in range(n-2,-1,-1):
        sum = np.sum(AB[i,i+1:n]*x[i+1:n])
        x[i] = (AB[i,n]-sum)/AB[i,i]
    return x

#Antes teniamos el sistema Ax=b
#Ahora tenemos el sgt sistema : PAx = Pb ; PA = LU => LUx = Pb
# Para resolver tenemos que hacer lo sgt :
# Lc = Pb; para hallar c
# Ux = c

#Resolviendo Lc = Pb
def relLc(L,Pb):
    (r,c) = L.shape
    n = r
    x = np.zeros([n])
    x[0] = Pb[0]
    for i in range(1,n):
        sum = np.sum(L[i,0:i]*x[0:i])
        x[i] = Pb[i] - sum
    return x

def relUx(Ux,c):
    (r,col) = Ux.shape
    n = r
    x = np.zeros([n],dtype=float)
    x[n-1] = c[n-1]/Ux[n-1,n-1]
    for i in range(n-1,-1,-1):
        sum = np.sum(Ux[i,i+1:n]*x[i+1:n])
        x[i] = (c[i]-sum)/Ux[i,i]
    return x

def mostrarPolinomio(P):
    n = len(P)
    out = ''
    for i in range(n-1,-1,-1):
        out += str(P[i])+'*x^'+str(i)+'+'
    out +='\b '
    print(out)
P = np.array([5.2,1.1,2.1,-3.1,1.0],dtype=float)


def Bairstow(P,r,s):
    n = len(P)
    b = np.empty_like(P)
    c = np.empty_like(P)
    A = np.zeros(([2,2]),dtype=float)
    B = np.zeros(([2,1]),dtype=float)
    x = np.zeros(([n-1]),dtype=complex)
    top = 0
    b[0] = 1
    b[1] = 1
    eps = 10**(-10)
    while len(P)-1>2:
        while np.abs(b[0])>eps or np.abs(b[1])>eps:
            b[n-1] = P[n-1]
            b[n-2] = P[n-2] + r*b[n-1]
            for i in range(n-3,-1,-1):
                b[i] = P[i] + r*b[i+1] + s*b[i+2]
            print('~~~~~~~~')
            print(b)
            c[n-1] = b[n-1]
            c[n-2] = b[n-2] + r*b[n-1]
            for i in range(n-3,-1,-1):
                c[i] = b[i] + r*c[i+1] + s*c[i+2]

            #Ahora nuestro matriz de sistema seria:
            # c1 c2 -b0
            # c2 c3 -b1
            A[0,0] = c[1]
            A[0,1] = c[2]
            A[1,0] = c[2]
            A[1,1] = c[3]
            B[0]= -b[0]
            B[1]= -b[1]
            P_ = eliminacionGausseana(A)
            Pb = P_.dot(B)
            C = relLc(A,Pb)
            (dr,ds) = relUx(A,C)
            r = r + dr
            s = s + ds
        # print(r,s)
        dis = r**2+4*s
        x[top]=((r+np.sqrt(complex(dis)))/2)
        top = top +1
        x[top]=((r-np.sqrt(complex(dis)))/2)
        # print(x)
        top = top +1
        b[n-1] = P[n-1]
        b[n-2] = P[n-2] + r*b[n-1]
        for i in range(n-3,-1,-1):
            b[i] = P[i] + r*b[i+1] + s*b[i+2]
        P = b[2:n]
        n = len(P)
    mostrarPolinomio(P)
    r = -P[1]
    s = -P[0]
    print(r,s)
    dis = r**2+4*s
    x[top]=((r+np.sqrt(complex(dis)))/2)
    top = top +1
    x[top]=((r-np.sqrt(complex(dis)))/2)
    # print(x)
    top = top +1
    print(x)
    #Esto convergera cuando b0 y b1 sean igual a 0
mostrarPolinomio(P)

Bairstow(P,1,1)
