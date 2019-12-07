import numpy as np
import cv2
from matplotlib import pyplot as plt

def change_contrast(img, a):
    lut = [np.uint8(255.0 / (1 + np.exp(-a * (i - 128.) / 255.))) for i in range(256)]
    result_img = np.array([lut[value] for value in img.flat], dtype=np.uint8)
    result_img = result_img.reshape(img.shape)
    return result_img

img = cv2.imread("Mono-Image2/512X512/Aerial2.bmp", 0)

dst_high = change_contrast(img, 20)
cv2.imwrite("Result/high_contrast_img.png", dst_high)

dst_low = change_contrast(img, 1)
cv2.imwrite("Result/low_contrast_img.png", dst_low)

plt.subplot(121)
plt.imshow(dst_high, cmap="gray")
plt.title("High Contrast")
plt.xticks([]), plt.yticks([])
plt.subplot(122)
plt.imshow(dst_low, cmap="gray")
plt.title("Low Contrast")
plt.xticks([]), plt.yticks([])
plt.savefig('Result/contrast_compare_img', bbox_inches='tight')
plt.clf()

plt.subplot(121)
plt.hist(dst_high.ravel(), 256, [0, 256])
plt.title("High Contrast")
plt.subplot(122)
plt.hist(dst_low.ravel(), 256, [0, 256])
plt.title("Low Contrast")
plt.subplots_adjust(wspace=0.4)
plt.savefig('Result/contrast_compare_hist', bbox_inches='tight')
