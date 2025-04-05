"""
Este código converte uma imagem colorida para tons de cinza usando três métodos e exibe os resultados. Primeiro, ele carrega a imagem usando a biblioteca PIL e a converte para um array NumPy. No Método 1, a imagem é convertida para tons de cinza utilizando a fórmula ponderada dos canais RGB. Esta fórmula é uma aproximação que leva em consideração a percepção do olho humano usando coeficientes. No método 2, usa o modelo HSL, usando colorsys. O método 3 usa o método convert('L') do PIL.
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import colorsys # Para converter para HSL

def plot_grayscale_methods(image_path):
    """
    Converte uma imagem colorida para tons de cinza usando três métodos: 
    - Método 1: Fórmula ponderada dos canais RGB. 
    - Método 2: Usando o canal Luminância (L) no modelo HSL. 
    - Método 3: Convertendo diretamente para tons de cinza com o método 'L' do PIL.
    """ 
    # Carrega a imagem
    image = Image.open(image_path)

    # Converte a imagem para array numpy
    img_array =  np.array(image)

    # Método 1: Convertendo para tons de cinza usando a fórmula RGB
    gray_rgb =  0.2989 * img_array[:,:,0] + 0.5870 * img_array[:,:,1] + 0.1140 * img_array[:,:,2]

    # Método 2: Convertendo para tons de cinza usando canal L do modelo HSL
    img_hsl = np.array([colorsys.rgb_to_hls(r/255., g/255., b/255.) for r, g, b in img_array.reshape(-1, 3)])
    gray_hsl = img_hsl[:, 1].reshape(img_array.shape[0], img_array.shape[1]) * 255 # Canal L (Luminância)

    # Método 3: Convertendo para tons de cinza com a função 'convert("L")' do PIL
    gray_pil = np.array(image.convert("L"))

    # Plotando as imagens
    fig, axes = plt.subplots(1, 4, figsize = (15, 6))

    # Títulos e imagens
    titles = ['Imagem original', 'Cinza por RGB', 'Cinza por L (HLS)', 'Cinza por PIL (L)']
    channels = [img_array, gray_rgb, gray_hsl, gray_pil]

    for ax, img, title in zip(axes, channels, titles):
        ax.imshow(img, cmap='gray', vmin=0, vmax=255)
        ax.set_title(title)
        ax.axis('off')

    plt.tight_layout()
    plt.show()

def main():
     # image_path = input('Entre com a imagem: ')
    image_path = r'../figuras/frutas.jpg'
    plot_grayscale_methods(image_path)

if __name__ == '__main__':
    main()