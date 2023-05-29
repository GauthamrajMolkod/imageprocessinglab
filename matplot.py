#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import os

def load_images_from_folder(images):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images


# In[11]:


import glob
cv_img = []
for img in glob.glob("C:/Users/CCL/Downloads/images/*.jpeg"):
    n= cv2.imread(img)
    cv_img.append(n)


# In[15]:


import cv2
import glob

images = [cv2.imread(file) for file in glob.glob('C:/Users/CCL/Downloads/images/*.jfif')]


# In[19]:


import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
get_ipython().run_line_magic('matplotlib', 'inline')

images = []
for img_path in glob.glob('C:/Users/CCL/Downloads/images/*.png'):
    images.append(mpimg.imread(img_path))

plt.figure(figsize=(20,10))
columns = 5
for i, image in enumerate(images):
    plt.subplot(len(images) / columns + 1, columns, i + 1)
    plt.imshow(image)
    plt.xticks([])
    plt.yticks([])


# In[ ]:




