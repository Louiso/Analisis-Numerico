#Para el metodo de newton se asume que la funcion sea diferenciable
#Es quiere decir que la grafica no debe presentar ningun pico y que la tangente
#de cada punto x sea unica

import numpy as np

#En el metodo de biseccion, el intervalo inicial debia tener extremos cuyo producto sea negativo
#En el metodo de Regla Falsa,  esa regla no es necesaria

# Para que este metodo funcione , la funcion solo debe tener raices reales
def f(x):
    return (x)**2+2*x+1

def d(f):
    def df(x):
        h = 10**(-4)
        return (f(x+h)-f(x))/h
    return df
#
# print(d(f)(10))

def rand():
    max = 1000
    min = -1000
    return np.random.random()*(max-min)+min;
def InterpolacionDeNewton(f):
    x = rand()
    dfx = d(f)(x)
    x_new = x - f(x)/dfx
    eps = 10**(-16)
    # Se produciria error si x es igual a 0 por champa :v
    err = x-x_new
    x = x_new
    while np.abs(err)>eps:
        dfx = d(f)(x)
        x_new = x - f(x)/dfx
        err = x-x_new
        x = x_new
        # print(x,f(x))
    return x
x = InterpolacionDeNewton(f)
print(x,f(x))
