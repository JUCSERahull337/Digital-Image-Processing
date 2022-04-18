Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
import matplotlib.pyplot as plt
img
img1= plt.imread("E:\\DIP Lab\\R&D\misc\\house.tiff")
plt.imshow(img1)
<matplotlib.image.AxesImage object at 0x00000230CF31AFB0>
plt.axis('off')
(-0.5, 511.5, 511.5, -0.5)
plt.title('House')
Text(0.5, 1.0, 'House')
plt.show()
