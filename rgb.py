#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


img=cv2.imread("C:/Users/CCL/Downloads/panda1.jpg",2)


# In[31]:


cv2.imshow('panda1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[32]:


ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
  
# converting to its binary form
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
  
cv2.imshow("Binary", bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[7]:


img=cv2.imread("C:/Users/CCL/Downloads/panda1.jpg",0)
cv2.imshow('panda1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
  
# converting to its binary form
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
  
cv2.imshow("Binary", bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[6]:


img=cv2.imread("C:/Users/CCL/Downloads/panda1.jpg",2)
cv2.imshow('panda1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
  
# converting to its binary form
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
  
cv2.imshow("Binary", bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[8]:


img=cv2.imread("C:/Users/CCL/Downloads/panda1.jpg",0)

# Displaying the image
cv2.imshow('grayscale', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[27]:


import cv2
  
image = cv2.imread("C:/Users/CCL/Downloads/panda1.jpg")
  
# converting BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  
cv2.imshow('image', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


import cv2
import numpy as np

img = cv2.imread('C:/Users/CCL/Downloads/panda1.jpg')

# Method 1: copy image and set other channels to black
r = img.copy()
r[:,:,0] = r[:,:,1] = 0

g = img.copy()
g[:,:,0] = g[:,:,2] = 0

b = img.copy()
b[:,:,1] = b[:,:,2] = 0

cv2.imshow("red",r)
cv2.imshow("green",g)
cv2.imshow("blue",b)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Method 2: split channels and merge with black channels
b,g,r = cv2.split(img)
k = np.zeros_like(b)
b = cv2.merge([b,k,k])
g = cv2.merge([k,g,k])
r = cv2.merge([k,k,r])

cv2.imshow("red",r)
cv2.imshow("green",g)
cv2.imshow("blue",b)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save results
cv2.imwrite("panda1_red.jpg", r)
cv2.imwrite("panda1_green.jpg", g)
cv2.imwrite("panda1_blue.jpg", b)


# In[12]:



import cv2

image = cv2.imread('C:/Users/CCL/Downloads/panda1.jpg')
cv2.imshow('Original', image)
cv2.waitKey(0)
  
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)  
cv2.destroyAllWindows()


# In[ ]:




