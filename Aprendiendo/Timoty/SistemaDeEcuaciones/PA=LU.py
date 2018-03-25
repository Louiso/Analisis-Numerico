import numpy as np
#
# def mostrarMatriz(M):
#     (r,c) = M.shape
#     for i in range(r):
#         out = ''
#         for j in range(c):
#             out = out + str(A[i,j])+' '
#         print(out)


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
A = np.array([
    [2,1,5],
    [4,4,-4],
    [1,3,1]
], dtype=float)

b = np.array([
    [5],
    [0],
    [6]
], dtype=float)
#print(A)
# print(b)
# print(np.hstack((A,b)))
# print(A)
P = eliminacionGausseana(A)
#A ya es  : A = AP
# print(P)
print(A)
#Calculando : Pb
Pb = P.dot(b)
print(Pb)
c = relLc(A,Pb)
print(c)


x = relUx(A,c)

print(x)

AB = np.hstack((A,b))
x = GaussSimple(AB)

# print(x)
