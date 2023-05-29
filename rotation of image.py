#!/usr/bin/env python
# coding: utf-8

# In[1]:



from PIL import Image

Original_Image = Image.open("C:/Users/CCL/Downloads/panda1.jpg")





rotated_image1 = Original_Image.rotate(180)

rotated_image2 = Original_Image.transpose(Image.ROTATE_90)

rotated_image3 = Original_Image.rotate(90-45)

rotated_image4 = Original_Image.rotate(60)

rotated_image5 = Original_Image.rotate(-45)

rotated_image6 = Original_Image.rotate(270)

rotated_image7 = Original_Image.rotate(90)

rotated_image1.show()
rotated_image2.show()
rotated_image3.show()
rotated_image4.show()
rotated_image5.show()
rotated_image6.show()
rotated_image7.show()


# In[ ]:




