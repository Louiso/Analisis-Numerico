import numpy as np
#
# def mostrarMatriz(M):
#     (r,c) = M.shape
#     for i in range(r):
#         out = ''
#         for j in range(c):
#             out = out + str(A[i,j])+' '
#         print(out)

A = np.array([
    [2,1,5],
    [4,4,-4],
    [1,3,1]
], dtype=float)

b = np.array([
    [5],
    [0],
    [6]
])
#print(A)
# print(b)
# print(np.hstack((A,b)))

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

AB = np.hstack((A,b))
x = GaussSimple(AB)

print(x)
