#!/usr/bin/env python
# coding: utf-8

# In[20]:



# import OS module
import os
 
# Get the list of all files and directories
path = "C:/Users/CCL/Downloads"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files

for dir_list in os.listdir(path):
    print(dir_list)


# In[2]:



# import the modules
import os
from os import listdir
 
# get the path/directory
folder_dir = "C:/Users/CCL/Downloads"
for images in os.listdir(folder_dir):
 
    # check if the image ends with png
    if (images.endswith(".png")):
        print(images)


# In[3]:


# import the modules
import os
from os import listdir
 
# get the path/directory
folder_dir = "C:/Users/CCL/Downloads"
for images in os.listdir(folder_dir):
 
    # check if the image ends with png
    if (images.endswith(".jpg")):
        print(images)


# In[12]:


# import the modules
import os
from os import listdir
 
# get the path/directory
folder_dir = "C:/Users/CCL/Downloads"
for images in os.listdir(folder_dir):
 
    # check if the image ends with png
    if (images.endswith(".mp4")):
        print(images)


# In[ ]:




