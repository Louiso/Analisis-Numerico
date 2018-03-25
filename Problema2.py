import numpy as np

def demostracion(n):
    a = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            a[i,j] = (1. + (i+1))**((j+1)-1)
    x = np.ones((n));
    for i in range(n):
        s = 0
        for p in range(n):
            s = s + a[i,p]*x[p]
        if s != ((1+(i+1))**n-1)/(i+1):
            return False

        return True

if demostracion(14):
    print('Correcto')
else:
    print('Incorrecto')

if demostracion(15):
    print('Correcto')
else:
    print('Incorrecto')

if demostracion(16):
    print('Correcto')
else:
    print('Incorrecto')

if demostracion(17):
    print('Correcto')
else:
    print('Incorrecto')
