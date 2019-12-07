import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("Result/impulse_noise.png", 0)

dst = cv2.blur(img, (5, 5))
cv2.imwrite('Result/smoothing_img.png', dst)

plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.xticks([]), plt.yticks([])
plt.subplot(122)
plt.imshow(dst, cmap="gray")
plt.title("Smoothed")
plt.xticks([]), plt.yticks([])
plt.savefig('Result/smoothing_compare_img', bbox_inches='tight')
