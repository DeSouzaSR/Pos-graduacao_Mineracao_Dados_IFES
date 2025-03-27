import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys

# Carregando as imagens
img1 = Image.open(sys.argv[1])
img2 = Image.open(sys.argv[2])

# Converter as imagens para arrays numpy (no formato RGB)
img1_array = np.array(img1)
img2_array = np.array(img2)

# Verificar se as imagens têm o mesmo tamanho e número de canais
if img1_array.shape != img2_array.shape:
    print("As imagens não têm o mesmo tamanho e número de canais. Ajustando para o mesmo tamanho...")
    img2 = img2.resize(img1.size)
    img2_array = np.array(img2)

# Operações lógicas
# A operação é feita pixel a pixel

# Operação AND
and_result = np.bitwise_and(img1_array, img2_array)

# Operação OR
or_result = np.bitwise_or(img1_array, img2_array)

# Operação XOR
xor_result = np.bitwise_xor(img1_array, img2_array)

# Operação NOT
not_result = np.bitwise_not(img1_array)

# Exibir as imagens
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

# Mostrar as imagens originais
axs[0, 0].imshow(img1_array)
axs[0, 0].set_title("Imagem 1")
axs[0, 0].axis("off")

axs[0, 1].imshow(img2_array)
axs[0, 1].set_title("Imagem 2")
axs[0, 1].axis("off")

# Mostrar as imagens resultantes
axs[0, 2].imshow(and_result)
axs[0, 2].set_title("AND")
axs[0, 2].axis("off")

axs[1, 0].imshow(or_result)
axs[1, 0].set_title("OR")
axs[1, 0].axis("off")

axs[1, 1].imshow(xor_result)
axs[1, 1].set_title("XOR")
axs[1, 1].axis("off")

axs[1, 2].imshow(not_result)
axs[1, 2].set_title("NOT")
axs[1, 2].axis("off")

plt.tight_layout()
plt.show()


