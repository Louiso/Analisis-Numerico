#El calculo de los polinomio que interpola los puntos mediante el
#el polinomio de lagendre se calcula mediante el metodo de diferencia de Newton

import numpy as np
import matplotlib.pyplot as plt
x = np.array([0.0, 1.525 , 3.050 ,4.575 , 6.10  , 7.625 ,9.150])
y = np.array([1.0, 0.8617, 0.7385, 0.6292, 0.5328,0.4481,0.3741])
n = len(x)
plt.plot(x,y)
plt.show()

f = {}

for ln in range(n):
    f[ln] = np.zeros([n-ln])

for j in range(n):
    f[0][j] = y[j]

# f[1][0] = (f[0][1]-f[0][0])/(x[0+1]-x[0])
# f[1][1] = (f[0][2]-f[0][1])/(x[1+1]-x[1])
#
# f[2][0] = (f[1][1]-f[1][0])/(x[0+2]-x[0])

#Denotare de otra manera:
#f[ln][k] = (f[ln][k+1] - f[ln-1][k])/(x[k+ln]-x[k])

for ln in range(1,n):
    for k in range(n-ln):
        f[ln][k] = (f[ln-1][k+1] - f[ln-1][k])/(x[k+ln]-x[k])

Coe = []
for ln in range(n):
    Coe.append(f[ln][n-ln-1])
    print f[ln]

#con esto se puede calcular el polinomio de lagendre
print "Los coeficientes para calcular el polinomio de lagendre mas facil es : "
print Coe

def g(m):
    s = 0.0
    n = len(Coe)
    for i in range(n):
        t = 1
        for j in range(i-1):
            t *=(m-x[i])
        s += Coe[i]*t
    return s

print g(10.5)
