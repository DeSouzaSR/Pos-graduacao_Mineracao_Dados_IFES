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
    return Image.fromarray(cv2.equalizeHist(np.array(image, dtype=np.uint8)))


def apply_clahe(image, clip_limit=2.0, tile_grid_size=(8,8)):
    """
    Applies CLAHE (Contrast Limited Adaptive Histogram Equalization)
    """
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    return Image.fromarray(clahe.apply(np.array(image, dtype=np.uint8)))


def normalize_image(image):
    """
    Normalizes the image to the range [0, 255].
    """
    img_array =  np.array(image, dtype=np.float32)
    img_normalized = 255 * (img_array - np.min(img_array)) / (np.max(img_array) - np.min(img_array))
    return Image.fromarray(np.uint8(img_normalized))


def plot_results(original_image, original_gray, equalized, clahe, normalized):
    """
    Plots the original loaded image, original grayscale image and the transformed versions with their hitograms.
    """
    fig, axes = plt.subplots(2, 5, figsize=(20, 10))
    titles = ['Original Image (Loaded)', 'Gray Image', 'Histogram Equalization', 'CLAHE', 'Normalization']
    images = [original_image, original_gray, equalized, clahe, normalized]

    # Plots
    for i, (ax, img, title) in enumerate(zip(axes[0], images, titles)):
        ax.imshow(img, cmap='gray', vmin=0, vmax=255) # Ensure brightness is in the correct range
        ax.set_title(title)
        ax.axis('off')

    # Plotting the histograms of the transformed images
    for i, (ax, img) in enumerate(zip(axes[0], images[1:])): # Deleting the original
        ax.hist(np.array(img).ravel(), bins=256, range=[0, 256], color='black')
        ax.set_title(f'Histogram - {titles[i + 1]}') # Adjustment for correct title
        ax.set_xlim([0, 256])

    # Remove axes that are not needed
    for ax in axes.flat:
        if not ax.has_data(): # Check if the axis has no data
            ax.axis('off') # Disables the empty axis.

    plt.tight_layout()
    plt.show()


def main(image_path):
    """
    Main function to load the image, apply histogram equalization methods and
    display the results.
    """

    # Load the original image
    image = Image.open(image_path)

    # Display the image dimensions and number of channels
    print(f'Dimensions of the uploaded image: {image.size} (width, height)')
    print(f'Number of channels: {len(image.getbands())}') # Display the numbers of channels

    # Check if the image is RGB, otherwise it is already in grayscale
    if is_rgb(image):
        print('The image is RGB')
        original_gray = image.convert('L') # Convert to grayscale
    else: 
        print('The image it is already in grayscale') 
        original_gray = image # Already in grayscale

    # Applying the transformations
    equalized = apply_histogram_equalization(original_gray)
    clahe = apply_clahe(original_gray)
    normalized = normalize_image(original_gray)

    # Plot the transformations results
    plot_results(image, original_gray, equalized, clahe, normalized)

if __name__ == '__main__':
    main('../figuras/frutas.jpg')


    