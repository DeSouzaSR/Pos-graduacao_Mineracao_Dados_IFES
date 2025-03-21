import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Carrega a imagem
img = Image.open('../figuras/cidade_vitoria.jpg')

# Converter a imagem para um array numpy
img_array = np.array(img)

# Gerar o histograma para cada canal RGB
plt.figure(figsize=(12, 6))

# Histograma do canal R
plt.subplot(1, 3, 1)
plt.hist(img_array[..., 0].ravel(), bins=256, color='red', alpha=0.6)
plt.title('Histograma do Canal Vermelho')
plt.xlim(0, 255)

# Histograma do canal G
plt.subplot(1, 3, 2)
plt.hist(img_array[..., 0].ravel(), bins=256, color='green', alpha=0.6)
plt.title('Histograma do Canal Verde')
plt.xlim(0, 255)

# Histograma do canal B
plt.subplot(1, 3, 3)
plt.hist(img_array[..., 0].ravel(), bins=256, color='blue', alpha=0.6)
plt.title('Histograma do Canal Azul')
plt.xlim(0, 255)

# Mostrar os histogramas
plt.tight_layout()
plt.show()