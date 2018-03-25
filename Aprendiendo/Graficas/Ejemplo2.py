import numpy as np                  # Cargamos numpy como el alias np
import matplotlib.pyplot as plt     # Crgagamos matplotlib.pyplot como el alias plt

# Definimos el periodo de la funcion
periodo = 0.5

# Definimos el array dimensional
x = np.linspace(0, 2, 1000)

# Definimos la funcion senoidal
y = np.sin(2*np.pi*x/periodo)

# Creamos la figura
plt.figure()

# Dibujamos  en negro discontinuo con etiqueta y1
plt.plot(x, y, 'k--', linewidth = 2, label = 'y1')

# Mantenemos la misma figura parta la siguiente grafica
plt.hold(True)

# Esta vez dibujamos - y en rojo co etiqueta y2
plt.plot(x,-y,'r', linewidth = 2, label = 'y2')

# Anadimos la leyenda
plt.legend(loc = 2)

# Anadimos las etiquetas poniendo en Latex 'm' simbolo de micras
plt.xlabel(r"$x (\mu m)$", fontsize = 24, color = (1,0,0))
plt.ylabel(r"$y (\mu m)$", fontsize = 24, color = 'blue')

# Anadimos texto
plt.text(x = 1, y = 0.0, s = u'T = 0.05', fontsize = 24)

# Anadimos la rejilla
plt.grid(True)
plt.grid(color = '0.5', linestyle = '--', linewidth = 1)

# Anadimos los ejes
plt.axis('tight')

# Anadimos el titulo
plt.title('(a)',fontsize = 28, color = '0.75', verticalalignment = 'baseline', horizontalalignment = 'center')

# Guardamos
plt.savefig('plotCompleta.png')

# Mostramos en pantalla
plt.show()
