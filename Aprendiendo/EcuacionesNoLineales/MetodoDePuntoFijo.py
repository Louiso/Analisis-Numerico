import numpy as np

def PuntoFijo(g):
    max = 100
    min = 0
    x = np.random.random()*(max-min)+max
    x_new = g(x)
    eps = 10**(-16)
    err = x - x_new
    while np.abs(err) > eps :
        x_new = g(x)
        err = x - x_new
        x = x_new
        # print(x)
    return x

#Sea mi funcion:
# f(x) = x**2 - 2*x - 3
# x(x - 2) - 3 = 0
# x = 3 /x-2
def g1(x):
    return (2*x+3)**(1./2)
def g2(x):
    return 3./(x-2)

#Dependiendo como uno despeje g , se obtendra distinta raiz
print(PuntoFijo(g1))
print(PuntoFijo(g2))
