import numpy as np
from numpy import pi

#def Gauss(A,b):
#	print("Sera :'v")

#A = np.array([
#				[1,23,3],
#				[1,2,3],
#				[1,24,4]
#			])

#b = np.array([
#				[1],
#				[2],
#				[3]
#			])

##Es se interpreta como 3 matrices 4x2
#C = np.arange(24).reshape(3,4,2)

#Tipos de datos:
#dtype:
#int, np.int , np.int16 , np.int32 , np.int64
#float , np.float , np.float16 , np.float32 ,np.float64
#complex
#C = np.array([
#				[1,2,3,4]
#			],dtype=complex)

#Matriz de zeros

#C = np.zeros([3,4])

#Matriz de unos

#C = np.ones((3,4),dtype=np.float)

#Matriz creada con una secuencia
# de 10 hasta 19 = 20-1, con incremento de 2 en 2

#C = np.arange(10,20,2)

#Matrix creada por otro tipo de secuencia
# de 0 hasta 2, crear 11 elementos por lo cual debe haber 10 cortes, es por eso que 2/10 = 0.2
#C = np.linspace(0,2,11)
#Da como resultado 0 0.2 0.4 ... 1.8 2.0

#print(A)
#print(b)
#print(C)


A = np.array([2,24,5,1])
B = np.arange(4)

#La suma : es la suma clasica de vectores
print(A+B)

#El producto : ci = ai*bi
print(A*B)

#La potencia es para cada elemento
print(B**2)

#Aplicacion de f para vector de n elementos, retorna otro vector de n elementos
print(np.sin(B))

#operador logico con un vector, retorna un vector booleano
print(B>2)


#Creando una matriz con valores random
#Para que sea dentro del intervalo que uno desea se debe realizar de la sgt forma:
# np.random.random([2,3])*(max-min)+min
B = np.random.random([2,3])*(10-3)+3

#Sumando todos los elementos de una array, sea vector o matriz

print(B.sum())

#Sumar los elementos de cada columna

print(B.sum(axis=0))

#Sumar los elementos de cada fila

print(B.sum(axis=1))

#Sumas acumuladas

print("\n")
print(B)
print("\n")
#Lo retorna en forma de vector, si la matriz es de mxn entonces retorna un vector de tamano mxn
print(B.cumsum())

#Manejando una array

A = np.arange(10)**3
print(A)
#cogiendo el elemento con indice 2
print(A[2])

#manejando los elementos desde el elemento con indice 2 hasta el elemento con indice 5 excluido
print(A[2:5])

#manejando los elementos desde el elemento con indice 2 hasta el elemento con indice 5 excluido
#incrementandose de 2 en dos
print(A[2:5:2])

#manejando los elementos desde el elemento con indice 0 hasta el elemento con indice 0 excluido
#decrementandose de -1 en -1
#Practicamente muestra el array al reves
print(A[::-1])


#como definir una matriz mediante un callback

np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)

#Mediante mi metodo

def matrix(f,A):
	(m,n) = A.shape
	for i in range(m):
		for j in range(n):
			A[i,j]=f(i,j)
	return A

def fun(i,j):
	if i==j:
		return np.sin(i+j)
	else:
		return np.cos(i-j)

print(matrix(fun,np.zeros((3,3))))

#Transpuesta de una matriz

A = np.arange(10).reshape(2,5)
print(A)
print(A.T)

#Transformar una matrix en vector

print(A.ravel())
print(A)

#Como redimensionar
#Metodo 1 : reshape

A = A.reshape(5,2)
print(A)

#Metodo 2: resize

A.resize((2,5))
print(A)


#A veces es dificil calcular por cuenta propia calcular las dos dimensiones
#Claro, antes ya sabiendo una , pues es lo que uno quiere, pero la otra tendrias
#que dividir el numero de elementos entre la primera dimension que ya sabes
#o  pasar como parametro en reshape a la segunda dimension como -1 , para el la
#maquina lo calcule solo

A = A.reshape(-1,2)
print(A)


#Como crear nuevas matrices a partir de otras , util para la matriz aumentada

#sea

a = np.arange(4).reshape((2,2))

b = np.arange(4).reshape((2,2))*2

print("\n")
print(a)
print("\n")
print(b)
print("\n")
#Union vertical
print(np.vstack((a,b)))
print("\n")
#Union horizontal
print(np.hstack((a,b)))
