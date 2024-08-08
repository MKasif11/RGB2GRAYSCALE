import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_image(image, title):
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')

image_path = 'gojo.jpeg'

bgr_image = cv2.imread(image_path)

b, g, r = cv2.split(bgr_image)

grayscale = 0.299 * r + 0.587 * g + 0.114 * b

grayscale_image = grayscale.astype(np.uint8)

plot_image(grayscale_image, 'Grayscale')
