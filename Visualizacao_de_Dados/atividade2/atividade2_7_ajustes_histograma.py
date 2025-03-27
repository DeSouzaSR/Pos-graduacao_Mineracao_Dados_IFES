import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage import exposure
import sys

def ajuste_contraste(img_array, fator=2.0):
    """
        Ajusta o contraste da imagem multiplicando os valores dos pixels pelo fator.
    """
    img_array = np.clip(fator * (img_array - 128) + 128, 0, 255)
    return img_array.astype(np.uint8)


# Carrega a imagem
img = Image.open(sys.argv[1])

# Converter a imagem para um array numpy
img_array = np.array(img)

# Ajuste do contraste
img_contraste = ajuste_contraste(img_array, 1.5)

# Equalização do histograma
img_equalizada = exposure.equalize_hist(img_array / 255.0) # Normaliza de 0 a 1
img_equalizada = (img_equalizada * 255).astype(np.uint8) # Volta para 0 a 255

# Gerar o histograma para a imagem original, ajustada e equalizada
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Histograma da imagem original
axes[0].hist(img_array[..., 0].ravel(), bins=256, color='red', alpha=0.6, label = 'Vermelho')
axes[0].hist(img_array[..., 1].ravel(), bins=256, color='green', alpha=0.6, label = 'Verde')
axes[0].hist(img_array[..., 2].ravel(), bins=256, color='blue', alpha=0.6, label = 'Azul')
axes[0].set_title('Histograma da imagem original')
axes[0].legend()

# Histograma da imagem ajustada
axes[1].hist(img_contraste[..., 0].ravel(), bins=256, color='red', alpha=0.6, label = 'Vermelho')
axes[1].hist(img_contraste[..., 1].ravel(), bins=256, color='green', alpha=0.6, label = 'Verde')
axes[1].hist(img_contraste[..., 2].ravel(), bins=256, color='blue', alpha=0.6, label = 'Azul')
axes[1].set_title('Histograma da imagem de contraste')
axes[1].legend()

# Histograma da imagem equalizada
axes[2].hist(img_equalizada[..., 0].ravel(), bins=256, color='red', alpha=0.6, label = 'Vermelho')
axes[2].hist(img_equalizada[..., 1].ravel(), bins=256, color='green', alpha=0.6, label = 'Verde')
axes[2].hist(img_equalizada[..., 2].ravel(), bins=256, color='blue', alpha=0.6, label = 'Azul')
axes[2].set_title('Histograma da imagem de equalizado')
axes[2].legend()

plt.tight_layout()
plt.show()

# Exibier as imagens
fig2, axes2 = plt.subplots(1, 3, figsize=(15, 5))
axes2[0].imshow(img)
axes2[0].set_title('Imagem original')
axes2[0].axis('off')

# Mostrar imagem com contraste ajustado
axes2[1].imshow(img_contraste)
axes2[1].set_title('Imagem com contraste ajustado')
axes2[1].axis('off')

# Mostrar imagem equalizada
axes2[2].imshow(img_equalizada)
axes2[2].set_title('Imagem equalizada')
axes2[2].axis('off')

plt.tight_layout()
plt.show()


