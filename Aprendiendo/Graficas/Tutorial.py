import matplotlib.pyplot as plt
import numpy as np

#Creo una secuencia de -2 hasta 2 , donde se mostrara 100 numeros
x = np.linspace(-2,2,100)
# plt.figure()

#Cargo en el buffer la primera grafica
y = x**2
plt.plot(x,y)

#Cargo en el buffer la segunda grafica
y = np.sin(x)
plt.plot(x,y)

#Agregamos las leyendas , las cuales se autoasignaran segun el orden de carga en el buffer
#Se observa que es necesario usar $...$ para que el contenido tenga estilo latex
plt.legend(('$f(x) = x^{2}$','$f(x)=sin(y)$'),loc = 'upper left')

#Agregando Etiquetas de los ejes
plt.xlabel(r'$\lambda (\AA)$')
# plt.xlabel('Eje X',fontsize = 20)

plt.ylabel('Eje Y',fontsize = 20)

#Agregando Titulo
plt.title("Mi primera grafica :'3")

#Manejando los ejes

#Retornar los limites de los ejes [xmin,xmax,ymin,ymax]
#plt.axis()

#Si se le pone un parametro a dicha funcion entonces estarias cambiando los limites de los ejes
#plt.axis(vector);

#Elimina las lineas de ejes
#plt.axis('off')

#Ejes Iguales
#plt.axis('equal')

#Eje Escalado
#plt.axis('scaled')

#Eje, cambiar ejes para q se muestren todos los datos
#plt.axis('tight')
# Haciendo una pequena linea en la linea
# y respecto a las coordenadas y x segun el eje
plt.axhline(y =2 , xmin=0.25,xmax=0.75)

#Agregando un texto arbitrario en alguna parte de la grafica
#plt.text(x,y,string,fontsize); x, y son las coordenadas de la grafica.
                                #no son coordenadas respecto la ventana
plt.text(1,1,'Hola mi Helmano',fontsize = 12)

#Agregando grid
plt.grid(True)
#configurando el grid
plt.grid( color = 'r' , linestyle = '-' , linewidth = 2)

#Guardando la grafica en un archivo:
#Guardar en la misma ubicacion que mi archivo actual
plt.savefig('./grafica', dpi = 300)
#configurando opciones de Guardando
# ruta: ruta y nombre de archivo. Los tipos de datos pueden ser .png, .eps, .pdf, .ps, .svg.
# dpi = None: resolucion de la imagen en puntos por pulgada
# facecolor = 'w': color del rectangulo de la figura
# edgecolor = 'w': color del perimetro de la figura
# orientation = 'portrait': orientacinn del papel (landscape)
# format = None : (png, pdf, ps, eps y svg).
# transparent = False, si es True, creara una grafica de fondo transparente.

#Muestro la grafica
plt.show()
plt.close()
