# Metodos Iterativos

En la casos reales los sistemas de ecuaciones en si ya tienen varios ceros,
que lamentablemente con los metodos directos con el proceso de eliminacion
muchos de estos coeficientes nulos dejan de serlo, llevando a un desgaste de
memoria innecesaria y es por ello que se hace uso de los metodos Iterativos como
solucion a este problema.

## Funcionamientos de los metodos Iterativos

Practicamente se basan en un vector inicial x_0 arbitrario , y una sucesion de
vectores { x_k }; k pertenece a N  destinada a converger a la solucion del sistema.


## Generalidades :

Los metodos iterativos se basan de la sgt forma :

* x_0 arbitrario
* x_{k+1} = B*x_k+c ; k = 0 , 1 , 2 , ....

B : matriz del metodo
c : vector del metodo

Estos valores se eligen a partir de los datos A y b

### Definiciones Preliminares

***Metodo Convergente*** si para cualquier x_0 arbitrario se cumple :

Existe k / lim_{k->inf}x_k = x

Ahora ....

Supongamos que el metodo sea convergente entonces :

lim_{k->inf}x_k = x => x = lim_{k->inf}x_{k+1} = lim_{k->inf}B*x_k+c

=> x = Bx+c => (I-B)x=c

:: B y c deben elegirse de tal manera que (I-B)x = c  tenga solucion
Ademas que los sistemas (I-B)x = c y Ax=b sean equivalentes

Ahora ...

Tratemos de calcular el error para un k arbitrario

x_k - x = (Bx_{k-1}+c) - (Bx+c) = B(x_{k-1}-x) ... => x-k - x = B^k(x0-x)

:: Dependiendo del valor de la matriz B , dependera la convergencia del metodo

## Caracterizacion de la convergencia de un metodo :

1.  El metodo lineal es Convergente
2.  p(B)  <  1
3.  ||B|| <  1, para al menos alguna norma de matriz subordinada

## Calificando la eficacia de un metodo:

1.  Metodo bien construido : (I-B)x=c y Ax=b deben ser equivalentes
2.  Metodo Convergente : p(B)<1 || ||B||<1
3.  Velocidad de convergencia : Mientras mas menor sea p(B) mejor















s
