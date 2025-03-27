from PIL import Image
import matplotlib.pyplot as plt

# Carrega a imagem
img = Image.open('../figuras/cidade_vitoria.jpg')

# Rotacionar a imagem em 45 e 90 graus. 
img_45 = img.rotate(45, expand=True) # Rotaciona em 45 graus e expande a imagem
img_90 = img.rotate(90, expand=True) # Rotaciona em 90 graus e expande a imagem

# Salvar as imagens
img_45.save('../figuras/cidade_vitoria_rotacionada_45.png')
img_90.save('../figuras/cidade_vitoria_rotacionada_90.png')

# Exibir as imagens
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Exibir a imagem original
axes[0].imshow(img)
axes[0].set_title('Imagem Original')
axes[0].axis('off')

# Exibir a imagem rotacionada em 45 graus
axes[1].imshow(img_45) 
axes[1].set_title('Imagem Rotacionada em 45 graus')
axes[1].axis('off')

# Exibir a imagem rotacionada em 90 graus
axes[2].imshow(img_90)
axes[2].set_title('Imagem Rotacionada em 90 graus')
axes[2].axis('off')

plt.show()
