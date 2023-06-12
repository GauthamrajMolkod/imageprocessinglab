#!/usr/bin/env python
# coding: utf-8

# In[33]:


# import required library
import cv2

# read input image
img = cv2.imread('C:/Users/CCL/Downloads/bitwise/beye.jfif')

# flip the image by vertically
img_v = cv2.flip(img, 0)

# display the rotated image
cv2.imshow("Vertical Flip", img_v)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_h = cv2.flip(img, 1)

# display the rotated image
cv2.imshow("Horizontal Flip", img_h)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_vh = cv2.flip(img, -1)

# display the rotated image
cv2.imshow("Both vertical and horizontal flip", img_vh)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[30]:





# In[ ]:




