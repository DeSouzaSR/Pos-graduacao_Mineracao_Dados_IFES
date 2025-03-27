from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import sys

# Carrega a imagem
img = Image.open(sys.argv[1])

# Converte a imagem para tons de cinza
img_gray = img.convert('L')

# Converte a imagem para um array numpy
img_gray_array = np.array(img_gray)

# Definir o limiar (threshold) para binarização (por exemplo, 128)
threshold = 128
#threshold = sys.argv[3]

# Binariza a imagem
img_binary = (img_gray_array > threshold) * 255 # Pixels acima do limiar são brancos (255) e abaixo são pretos (0)

# Converter o array numpy de volta para uma imagem
img_binary_pil = Image.fromarray(img_binary.astype(np.uint8))

# Salvar a imagem binarizada
img_binary_pil.save(sys.argv[2])

# Mostrar a imagem original e binarizada
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(img_gray, cmap='gray')   # Mostra a imagem original em tons de cinza
axes[0].set_title('Imagem Original')
axes[0].axis('off')

axes[1].imshow(img_binary_pil, cmap='gray')   # Mostra a imagem binarizada
axes[1].set_title('Imagem Binarizada')
axes[1].axis('off')

plt.tight_layout()
plt.show()

