import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'gojo.jpeg'

bgr_image = cv2.imread(image_path)

rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

r, g, b = cv2.split(rgb_image)

grayscale = 0.299 * r + 0.587 * g + 0.114 * b

grayscale_image = grayscale.astype(np.uint8)

plt.subplot(1,2,1)
plt.imshow(rgb_image)
plt.title('RGB')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(grayscale_image, cmap='gray')
plt.title('GRAYSCALE')
plt.axis('off')
