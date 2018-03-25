from __future__ import division

import numpy as np                  # Cargamos numpy como el alias np
import matplotlib.pyplot as plt     # Crgagamos matplotlib.pyplot como el alias plt

# Definimos el periodo de la grafica senoidal
periodo = 2

# Definimos el array dimensional
x = np.linspace(0, 10, 1000)
# Definimos la funcion senoidal
y = np.sin(2*np.pi*x/periodo)

# Creamos la figura
plt.figure()

# Primera grafica
plt.subplot(3,3,1)
plt.plot(x, y,'r')

 # Segunda grafica
plt.subplot(3,3,2)
plt.plot(x, y,'g')

# Tercera grafica
plt.subplot(3,3,3)
plt.plot(x, y,'b')

# Cuarta grafica
plt.subplot(3,3,4)
plt.plot(x, y,'k')

# Mostramos en pantalla
plt.show()
