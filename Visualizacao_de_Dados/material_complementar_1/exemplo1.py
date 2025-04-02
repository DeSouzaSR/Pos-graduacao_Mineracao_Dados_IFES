# Material complementar 1

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def plot_image_channels(image_path):
    """
    Carrega a imagem, verifica o número de canais e plota a imagem original
    e os canais RGB ou a imagem em escala de cinza
    """
    # Carregar a imagem
    image = Image.open(image_path)
    
    # Converter para o array numpy
    img_array = np.array(image)

    # Verificar se a imagem é RGB ou escala de cinza
    if len(image.getbands()) == 3: # Imagem RGB
        print("A imagem é RGB")

        # Separar os canais RGB
        r_channel = img_array[:, :, 0] # Canal vermelho
        g_channel = img_array[:, :, 1] # Canal verde 
        b_channel = img_array[:, :, 2] # Canal azul

        # Reconstruir a imagem RGB a partir dos canais.
        reconstructed_image = np.stack((r_channel, g_channel, b_channel), axis=-1)

        # Criar imagens com os canais isolados (para visualização colorida)
        r_image = np.zeros_like(img_array)
        r_image[:,:,0] = r_channel
    
        g_image = np.zeros_like(img_array)
        g_image[:,:,1] = g_channel
    
        b_image = np.zeros_like(img_array)
        b_image[:,:,2] = b_channel
    
        # Plotar a imagem original, os canais e a reconstrução
        fig, axes = plt.subplots(1, 5, figsize = (15, 5))

        # Títulos e imagens
        titles = ['Imagem original', "Canal R", "Canal G", "Canal B", "Imagem reconstruida"]
        channels = [img_array, r_image, g_image, b_image, reconstructed_image]

        # Plotanto as imagens
        for ax, img, title in zip(axes, channels, titles):
            ax.imshow(img)
            ax.set_title(title)
            ax.axis('off') # Remover os eixos
    else: # Imagem em escala de cinza
        print("A imagem está em escala de cinza")

        # Reconstruir a imagem a partir da escala de cinza (duplicando os canais)
        reconstructed_image = np.stack((img_array, img_array, img_array), axis=-1)

        # Plotar a imagem original e a imagem em escala de cinza
        fig, axes = plt.subplots(1, 3, figsize=(15, 6))

        # Títulos e imagens
        titles = ['Imagem Original', 'Imagem em Escala de Cinza', 'Imagem Reconstruida']
        channels = [img_array, img_array, reconstructed_image]

        # Plotando as imagens
        for ax, img, title in zip(axes, channels, titles):
            ax.imshow(img, cmap='gray', vmin=0, vmax=255) # Definir os limites de intensidade do pixel
            ax.set_title(title)
            ax.axis('off')

    plt.tight_layout()
    plt.show()

def main():
    #path_image = r'../figuras/polen.bmp'
    path_image = input("Entre com o caminho da imagem: ").strip().replace("\\", "/")
    plot_image_channels(path_image)

if __name__ == '__main__':
    main()