import numpy as np

# A = B * T
# A es una matriz cualquiera , la cual se puede descomponer en dos matrices,
# una es matriz tringular superior
# otra es una matriz ortogonal por columna

#Este problema se usa para resolver el problema 12 y 13
# Ax = b ; A es una matriz nxm
# A.T*A*x = A.T*b
# T.T*B.T*B*T*x = T.T*B.T*b
# Tx = inv(B.T*B)*B.T*b

def GSmodificado(A):
    B = np.zeros_like(A)
    B[:] = A[:]
    (r,c) = np.shape(A)
    T = np.zeros((c,c))
    for k in range(c):
        d = sum(abs(B[:,k])**2)
        #La diagonal igual a 1
        T[k,k] = 1
        #T matriz triangular superior
        for j in range(k+1,c):
            T[k,j] = np.dot(B[:,j],B[:,k])/d
            B[:,j] = B[:,j] - T[k,j]*B[:,k]
    return (B,T)

A = np.array([
    [1,0],
    [1,1],
    [1,2],
    [1,3],
    [1,4],
],dtype = 'f')
(B,T) = GSmodificado(A)
print(B)
print(T)
L = 1000.
b = np.array([
    [np.log(L/200-1)],
    [np.log(L/400-1)],
    [np.log(L/650-1)],
    [np.log(L/850-1)],
    [np.log(L/950-1)]
])
print sum(A[:,1]*b[:,0])
new_b = np.linalg.inv(B.T.dot(B)).dot(B.T).dot(b)
print(new_b)
#Problema 12:
#Aqui el truco es despejar los valores que queremos obtener
# P = L/(1+Ce^(At))
# => ln(C) + AT = ln(L/P - 1)
# Nuestras variables son : x0 = ln(C) , x1 = A
