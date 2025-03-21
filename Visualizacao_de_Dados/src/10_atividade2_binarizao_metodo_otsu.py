from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage import filters
from skimage import img_as_ubyte
from skimage.color import rgb2gray
from skimage import io
from skimage.filters import threshold_local 
import sys

# Carrega a imagem
#img = io.imread(sys.argv[1])
img = Image.open(sys.argv[1])

# Converter a image para tons de cinza
# img_gray = rgb2gray(img)
img_gray = img.convert('L')

# Converter a imagem em tons de cinza para um array NumPy 
img_gray_array = np.array(img_gray)

# 1. Binarização adaptativa
# utilizando a função 'adapt_threshold' do módulo 'threshold_local' do pacote 'skimage.filters'
# Calcular o limiar adaptativo
block_size = 35 # Tamanho do bloco de pixels para calcular o limiar adaptativo
local_thresh = threshold_local(img_gray_array, block_size, offset=10)
img_bin_adapt = img_gray_array > local_thresh
img_bin_adapt = img_as_ubyte(img_bin_adapt) # converter para 8 bits para salvar

# 2. Binarização de Otsu
# Calcular o limiar de Otsu
otsu_thresh = filters.threshold_otsu(img_gray_array)
img_bin_otsu = img_gray_array > otsu_thresh
img_bin_otsu = img_as_ubyte(img_bin_otsu) # converter para 8 bits para salvar

# Converter os arrays binarizados de volta para imagens PIL
img_bin_adapt_pil = Image.fromarray(img_bin_adapt)
img_bin_otsu_pil = Image.fromarray(img_bin_otsu)

# Salvar as imagens binarizadas
img_bin_adapt_pil.save(sys.argv[2])
img_bin_otsu_pil.save(sys.argv[3])  

# Exibir as imagens originais e binarizadas
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
ax[0].imshow(img, cmap='gray')  
ax[0].set_title('Imagem Original')
ax[0].axis('off')

ax[1].imshow(img_bin_adapt_pil, cmap='gray')
ax[1].set_title('Binarização Adaptativa')
ax[1].axis('off')

ax[2].imshow(img_bin_otsu_pil, cmap='gray')
ax[2].set_title('Binarização de Otsu')
ax[2].axis('off')

plt.tight_layout()
plt.show()


