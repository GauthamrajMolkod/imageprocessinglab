#!/usr/bin/env python
# coding: utf-8

# In[3]:


conda install -c conda-forge opencv


# In[1]:


get_ipython().system('pip install opencv-contrib-python')
import cv2

print(cv2.__version__)


# In[4]:


get_ipython().system('pip install numpy scipy matplotlib scikit-learn jupyter')


# In[5]:


import cv2
img=cv2.imread("C:/Users/CCL/Downloads/water.png")


# In[6]:


cv2.imshow('water',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[4]:


import cv2

image = cv2.imread("C:/Users/CCL/Downloads/water.png")
B, G, R = cv2.split(image)
# Corresponding channels are separated

cv2.imshow("original", image)
cv2.waitKey(0)

cv2.imshow("blue", B)
cv2.waitKey(0)

cv2.imshow("Green", G)
cv2.waitKey(0)

cv2.imshow("red", R)
cv2.waitKey(0)

cv2.destroyAllWindows()


# In[1]:



import glob
import cv2
path="C:/Users/CCL/Downloads/image/*.jpg"    
images=[cv2.imread(images) for images in glob.glob(path)]

for i in range(len(images)):
    cv2.imshow("images",images[i])
    cv2.waitKey(1)
    cv2.destroyAllWindows


# In[12]:


import matplotlib.pyplot as plt
import matplotlib.image as img
images= img.imread("C:/Users/CCL/Downloads/water.png" )
plt.imshow(images)


# In[15]:


import cv2
from matplotlib import pyplot as plt
  
# create figure
fig = plt.figure(figsize=(10, 7))
  
# setting values to rows and column variables
rows = 2
columns = 4
  
# reading images
Image1 = cv2.imread("C:/Users/CCL/Downloads/image/CannyFish.jpg")
Image2 = cv2.imread("C:/Users/CCL/Downloads/image/panda.jpg")
Image3 = cv2.imread("C:/Users/CCL/Downloads/image/flower.jpg")
Image4 = cv2.imread("C:/Users/CCL/Downloads/image/polygons.jpg")
  
# Adds a subplot at the 1st position
fig.add_subplot(rows, columns, 1)
  
# showing image
plt.imshow(Image1)
plt.axis('on')
plt.title("Image2")
  
# Adds a subplot at the 2nd position
fig.add_subplot(rows, columns, 2)
  
# showing image
plt.imshow(Image2)
plt.axis('on')
plt.title("Image3")
  
# Adds a subplot at the 3rd position
fig.add_subplot(rows, columns, 3)
  
# showing image
plt.imshow(Image3)
plt.axis('on')
plt.title("Image4")
  
# Adds a subplot at the 4th position
fig.add_subplot(rows,columns,4)
  
# showing image
plt.imshow(Image4)
plt.axis('on')
plt.title("Image5")


# In[ ]:





# In[ ]:





# In[ ]:




