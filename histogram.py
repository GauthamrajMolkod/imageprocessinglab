#!/usr/bin/env python
# coding: utf-8

# In[3]:


from PIL import Image
import matplotlib.pyplot as plt
im=Image.open("C:/Users/CCL/Downloads/panda1.jpg")
p1=im.histogram()
plt.bar(range(256),p1[:256],color='r',alpha=0.5)
plt.bar(range(256),p1[256:2*256],color='g',alpha=0.4)
plt.bar(range(256),p1[2*256:],color='b',alpha=0.3)
plt.show()


# In[ ]:




