import numpy as np

def sol_elim_gauss(AB):
    sumas = 0
    productos = 0
    (n,m)=np.shape(AB)
    #n es el numero de columnas de la matriz aumentada
    #m es el numero de filas de la matriz aumentada
    for j in range(n-1): #para cada columna
        for i in range(j+1,n):#para cada fila
            #Se calcula la realcion entre la fila i y la fila j
            mij=AB[i,j]/AB[j,j]
            productos = productos + 1
            #Se indica que toda una fila se le reste la fila j
            AB[i,:]-=mij*AB[j,:]
            #Aqui se presencia una operaciom elemental
            #El cual consiste en multiplicar una fila y sumarlca con otra
            #por lo cual se realiza suma y producto
            productos = productos + n
            sumas = sumas + n
    print('Total de sumas necesarios : ',sumas)
    print('Total de productos necesarios : ',productos)
    sumas = 0
    productos = 0
    x = np.zeros((n,),dtype='f')
    x[n-1]=AB[n-1,n]/AB[n-1,n-1]

    #Con el valor final de x ya encontrado solo es cuestion de usarla
    #para hallar el resto de los valores
    for i in range(n-2,-1,-1):
        x[i] = (AB[i,n] - np.sum(x[(i+1):n]*AB[i,i+1:n]))/AB[i,i]
        sumas = sumas + (n-i+1) +1
        productos = productos + (n-i+1) + 1
    print('Total de sumas necesarios para la sustitucion : ',sumas)
    print('Total de productos necesarios para la sustitucion: ',productos)

    return x

AB = np.matrix([[3,1,1,5],[1,3,-1,3],[3,1,-5,-1]])
x=sol_elim_gauss(AB)
