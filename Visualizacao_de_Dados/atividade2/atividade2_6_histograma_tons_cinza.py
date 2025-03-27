from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import sys

# Carrega a imagem
#img = Image.open('../figuras/cidade_vitoria.jpg')
img = Image.open(sys.argv[1])   


# Converte a imagem para tons de cinza
img_cinza = img.convert('L')

# Converte a imagem para um array numpy
img_array = np.array(img_cinza)

# Gerar histograma para a imagem em tons de cinza
plt.hist(img_array.ravel(), bins=256, color='gray', alpha=0.6)
plt.title('Histograma da imagem em tons de cinza')
plt.xlim([0, 255])
plt.show()