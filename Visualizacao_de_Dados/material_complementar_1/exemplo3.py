"""
No seguinte exemplo, uma imagem é carregada, verificando-se se a mesma é de
tipo RGB ou escala de cinza e aplica três técnicas de melhoria de contraste:
equalização de histograma, CLAHE (equalização adaptativa) e normalização.
"""

# Importação
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

# Funções
def is_rgb(image):
    """
    Check if image is RGB
    """
    return len(image.getbands()) == 3


def apply_histogram_equalization(image):
    """
    Applies histogram equalization to the image.
    """
    return Image.from