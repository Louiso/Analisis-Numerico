#en python no hay do while
import numpy as np

#En el metodo de biseccion, el intervalo inicial debia tener extremos cuyo producto sea negativo
#En el metodo de Regla Falsa,  esa regla no es necesaria

def f(x):
    return x**2-1012
def rand():
    max = 1000
    min = -1000
    return np.random.random()*(max-min)+min;
def ReglaFalsa(f):
    a = rand()
    b = rand()
    if f(a)*f(b)<0:
        m = (a*f(b)-2*b*f(a))/(f(b)-2*f(a))
    else:
        m = (2*a*f(b)-b*f(a))/(2*f(b)-f(a))
    if f(a)*f(m)<0:
        b = m
    elif f(b)*f(m)<0:
        a = m
    eps = 10**(-10)
    while f(m)>eps:
        if f(a)*f(b)<0:
            m = (a*f(b)-2*b*f(a))/(f(b)-2*f(a))
        else:
            m = (2*a*f(b)-b*f(a))/(2*f(b)-f(a))
        if f(a)*f(m)>0:
            a = m
        elif f(b)*f(m)<0:
            b = m
    return m

print(ReglaFalsa(f))
