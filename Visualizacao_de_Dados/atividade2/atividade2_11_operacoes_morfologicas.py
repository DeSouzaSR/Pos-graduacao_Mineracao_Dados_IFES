from PIL import Image 
import numpy as np 
import matplotlib.pyplot as plt 
from skimage import morphology 
from skimage import img_as_ubyte
import sys
 
# Carregar a imagem 
img = Image.open(sys.argv[1]) 
 
# Converter a imagem para tons de cinza 
img_gray = img.convert('L') 
 
# Converter a imagem em tons de cinza para um array NumPy
img_gray_array = np.array(img_gray) 
 
# Binarizar a imagem
threshold = 128 
img_binary = (img_gray_array > threshold) * 255 
 
# Realizar operações morfológicas 
# 1. Dilatação
img_dilated = morphology.dilation(img_binary) 
 
# 2. Erosão
img_erosion = morphology.erosion(img_binary) 
 
# 3. Abertura (Erosão seguida de Dilatação) 
img_opening = morphology.opening(img_binary) 
 
# 4. Fechamento (Dilatação seguida de Erosão) 
img_closing = morphology.closing(img_binary) 
 
# Converter os resultados das operações morfológicas de volta para imagens PIL 
img_dilated_pil = Image.fromarray(img_as_ubyte(img_dilated)) 
img_erosion_pil = Image.fromarray(img_as_ubyte(img_erosion)) 
img_opening_pil = Image.fromarray(img_as_ubyte(img_opening)) 
img_closing_pil = Image.fromarray(img_as_ubyte(img_closing))  

# Salvar as imagens morfológicas 
img_dilated_pil.save(sys.argv[2] + '_dilated.png')
img_erosion_pil.save(sys.argv[2] + '_erosion.png')  
img_opening_pil.save(sys.argv[2] + '_opening.png')
img_closing_pil.save(sys.argv[2] + '_closing.png')

# Exibir as imagens originais e morfológicas 
fig, axes = plt.subplots(2, 3, figsize=(15, 10)) 
 
# Exibir imagem original em tons de cinza 
axes[0, 0].imshow(img_gray, cmap='gray') 
axes[0, 0].set_title('Imagem Original (Tons de Cinza)') 
axes[0, 0].axis('off') 
 
# Exibir imagem binarizada 
axes[0, 1].imshow(img_binary, cmap='gray') 
axes[0, 1].set_title('Imagem Binarizada') 
axes[0, 1].axis('off') 
 
# Exibir imagem dilatada 
axes[0, 2].imshow(img_dilated, cmap='gray') 
axes[0, 2].set_title('Dilatação') 
axes[0, 2].axis('off') 
 
# Exibir imagem erodida 
axes[1, 0].imshow(img_erosion, cmap='gray') 
axes[1, 0].set_title('Erosão') 
axes[1, 0].axis('off') 
 
# Exibir imagem após abertura 
axes[1, 1].imshow(img_opening, cmap='gray') 
axes[1, 1].set_title('Abertura') 
axes[1, 1].axis('off') 
 
# Exibir imagem após fechamento 
axes[1, 2].imshow(img_closing, cmap='gray') 
axes[1, 2].set_title('Fechamento') 
axes[1, 2].axis('off') 

plt.tight_layout() 
plt.show() 
