import numpy as np                  # Cargamos numpy como el alias np
import matplotlib.pyplot as plt     # Crgagamos matplotlib.pyplot como el alias plt

# Creamos una figura
plt.figure()

# Creamos los arrays dimensionales
# crea una sucesion donde el incremento es de 0.01
x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)

# Obtenemos las corrdenadas resultantes de esos arrays
# Creamos nuestro eje de coordenadas
X, Y = np.meshgrid(x, y)
print(X)
print(Y)

# Definimos la grafica sen (x^2 + y^2)
fxy = np.sin(X**2+Y**2)

# Representamos
plt.imshow(fxy);

# Anadimos una colorbar
plt.colorbar();

# Mostramos en pantalla
plt.show()
