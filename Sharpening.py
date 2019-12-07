import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("Mono-Image2/512X512/Aerial2.bmp", 0)
k = -1.0
sharpening_kernel = np.array([[k, k, k],[k, 9*-k, k],[k, k, k]])

dst = cv2.filter2D(img, -1, sharpening_kernel)
cv2.imwrite('Result/sharpening_img.png', dst)

plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.xticks([]), plt.yticks([])
plt.subplot(122)
plt.imshow(dst, cmap="gray")
plt.title("Sharped")
plt.xticks([]), plt.yticks([])
plt.savefig('Result/sharpening_compare_img', bbox_inches='tight')
