import numpy as np

def f(x):
	return x - np.sin(x)

def fact(x):
	if x<2:
		return 1
	return x*fact(x-1)

def sgn(x):
	if x%2==0:
		return 1
	else:
		return -1

def f2(x):
	s = 0	
	for i in range(4):
		k=2*(i+1)+1
		s = s + sgn(i)*x**(k)/fact(k)
	return s
	
for i in range(10):
	t=10**(-i);
	print("f : ",f(t))
	print("f2 : ",f2(t))
	
	
#Conclusion la segunda def de x - sin(x) tiene mucho mas estable que la primera

