#en python no hay do while
import numpy as np

def f(x):
    return x**2-1012
def rand():
    max = 1000
    min = -1000
    return np.random.random()*(max-min)+min;
def Biseccion(f):
    a = rand()
    b = rand()
    while f(a)*f(b)>0:
        a = rand()
        b = rand()
    if a > b :
        temp = a
        a = b
        b = temp
    #El intervalo debe ser [a,b]
    m = (a+b)/2
    if f(a)*f(m)<0:
        b = m
    elif f(b)*f(m)<0:
        a = m
    m_new = a
    err = np.abs(m-m_new)
    eps = 10**(-16)
    while err>eps:
        m = (a+b)/2
        if f(a)*f(m)<0:
            b = m
        elif f(b)*f(m)<0:
            a = m
        err = np.abs(m-m_new)
        m_new = m
        # print(m_new)
    print(m_new)

Biseccion(f)
