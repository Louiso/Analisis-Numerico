import numpy as np
from numpy import pi

def Gauss(AB):
    #Obtenemos las dimensiones de la matriz aumentada
    (r,c) = AB.shape
    n=r
    #r = n
    #c = n+1
    for j in range(n-1): #para cada columna,excepto la ultima
        for i in range(j+1,n):
            #print("j : ",j,"=>",AB[j,j])
            # if AB[j,j] == 0 and j == n-2:
			# 	return "Es inconsistente"
			# elif AB[j,j] == 0:
			# 	k=j+1
			# 	#Si se verifica que AB[k,j] es el maximo posible en su columna entonces se
			# 	#podria decir que se esta ejecutando Gauss con pivote
			# 	#El pivote total consiste no solo en buscar en la columna j, sino tambn en las demas columnas
			# 	#y tomar el de mayor valor, para asi evitar errores de redondeo que ocurren en gauss y gauss con pivote
			# 	while AB[k,j]==0:
			# 		#print(AB[k,j])
			# 		if k==n-2:
			# 			return "Es inconsistente"
			# 		k = k + 1
			# 	temp = AB[k,:]
			# 	AB[k,:] = AB[j,:]
			# 	AB[j,:] = temp
            mij=AB[i,j]/AB[j,j]
            print(mij)
            AB[i,:] = AB[i,:] - mij*AB[j,:]
            print(AB)
	#Proceso de transformacion
    print(AB)

    x = np.zeros((n),dtype=float)
	# Solucion segura
    x[n-1]=AB[n-1,n]/AB[n-1,n-1]
	# Es desde n-2 , xq n-1 ya esta resuelto, y es -1 , xq el ultimo numero no se toma
	# es decir la sucesion seria  n-2, .... , 0
    for i in range(n-2,-1,-1):
        Sum = np.sum(AB[i,(i+1):n]*x[(i+1):n])
        x[i] = (AB[i,n] - Sum)/AB[i,i]
    return x

''' AB = np.array([
    [ -2.64575131 , -12.1043122 ,  -79.9893301 ,-1.73274033],
    [  0.0        ,  8.06954150 , 73.8363047 , -0.550051698],
    [  0.0 		  ,  0.0  , 21.3147052,0.0588970086]],dtype = float) '''
AB = np.array([
    [ 1 , 0 , 1 , 1 , 1 , 0 , 0],
    [ 0 , 1 ,-2 ,-3 ,-5 , 1 , 5],
    [ 0 , 0 , 0 , 1 , 8 ,-5 , 2],
    [ -1, 0 ,-1 , 0 ,-4 ,-8 ,-3],
    [  0,-1 , 2 , 4 , 0 ,-4 , 1]
],dtype = float);
print("\n")
print(AB)
print("\n")
x = Gauss(AB)
print(x)
print x[0]+x[1]*10.5+x[2]*(10.5)**2
