import numpy as np

def norm(x):
    return np.sqrt(x.T.dot(x))

x = np.array([
    [3],
    [4]
],dtype=float)

w = np.zeros_like(x)
w[0,0] = norm(x)

v = x - w

P = (v.dot(v.T))/(v.T.dot(v))
print v
print P

n = len(x)

I = np.eye(n)

H = I - 2*P

print H

print H.dot(x)

A = np.array([
    [3,1],
    [4,3]
])

print H.dot(A)
