import numpy as np
#
# def mostrarMatriz(M):
#     (r,c) = M.shape
#     for i in range(r):
#         out = ''
#         for j in range(c):
#             out = out + str(A[i,j])+' '
#         print(out)


def intercambioFila(M,f1,f2):
    temp = np.empty_like(M[f1,:])
    temp[:] = M[f1,:]
    M[f1,:] = M[f2,:]
    M[f2,:] = temp[:]
def intercambioColumna(M,c1,c2):
    temp = np.empty_like(M[:,c1])
    temp[:] = M[:,c1]
    M[:,c1] = M[:,c2]
    M[:,c2] = temp[:]

def eliminacionGausseana(A):
    (r,c) = A.shape
    n = r
    P = np.eye(n)
    S = np.eye(n)
    #Proceso de eliminacion gausseana
    for j in range(n-1):
        #Aplica pivote Total
        pivi = j
        pivj = j
        for ii in range(j,n):
            for jj in range(j,n):
                if np.abs(A[ii,jj])>np.abs(A[pivi,pivj]):
                    pivi = ii
                    pivj = jj
        intercambioFila(A,j,pivi)
        intercambioFila(P,j,pivi)
        intercambioColumna(A,j,pivj)
        intercambioColumna(S,j,pivj)
        #Fin pivote parcial
        for i in range(j+1,n):
            mij = A[i,j]/A[j,j]
            #eliminar las elementos de la columna j
            A[i,:] = A[i,:]-mij*A[j,:]
            P[i,:] = P[i,:]-mij*P[j,:]
            #A[i,j] = mij
    #Fin de triangulacionSuperior
    # print(A)
    #Proceso de eliminacion gaussiana inverso
    for j in range(n-1,-1,-1):
        for i in range(j-1,-1,-1):
            mij = A[i,j]/A[j,j]
            #eliminar las elementos de la columna j
            A[i,:] = A[i,:]-mij*A[j,:]
            P[i,:] = P[i,:]-mij*P[j,:]
    #Termina A como una matriz diagonal
    for i in range(n):
        m = A[i,i]
        A[i,:] = A[i,:]/m
        P[i,:] = P[i,:]/m
    return (P,S)

def inv(A):
    temp = np.empty_like(A)
    temp[:,:] = A[:,:]
    (P,S) = eliminacionGausseana(temp)
    I = np.eye(len(temp),dtype=float)
    return S.dot(P)
#Antes teniamos el sistema Ax=b
#Ahora tenemos el sgt sistema : PASx = PbS ; PAS = LU => LUx = PbS
# Para resolver tenemos que hacer lo sgt :
# Lc = PbS; para hallar c
# Ux = c

A = np.array([
    [2,0,0],
    [1,1,2],
    [2,1,1]
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
print(A)
print(inv(A))
print(A.dot(inv(A)))
