def f(v):
    v[0]=5./3-v[1]/3-v[2]/3
    v[1]=1-v[0]/3+v[2]/3
    v[2]=1./5+3.*v[0]/5+v[1]/5
    return v

v = [0.0,0.0,0.0]
for i in range(4):
    v = f(v)
    print('Despues de la iteracion : ',(i+1))
    print(v)
