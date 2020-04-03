# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 15:57:40 2020

@author: little apple
"""
from PIL import Image
import glob

# display image 
img_path='C:/ntut/code/web_crawling/image/images_1/3-Ingredient-Brownies-_Whole30-_-Paleo_-2306591.jpg'
im = Image.open(img_path)
print('{}'.format(im.format))
print('size: {}'.format(im.size))
print('image mode: {}'.format(im.mode))
im.show()

# empty lists
image_list=[]
resized_images = []
name=[]
# append images to list
for filename in glob.glob('C:/ntut/code/web_crawling/image/images_1/*.jpg'):
    print(filename)
    name.append(filename)
    img =Image.open(filename)
    image_list.append(img)

# append resized images to list
for image in image_list:
    # image.show()
    image = image.resize((100,100))
    resized_images.append(image)

# save resized images to new folder
# could also probably use os to create new folder
for (i, new) in enumerate(resized_images):
    new.save('{}{}{}'.format('C:/ntut/code/web_crawling/image_resize/images_1/', name[i][41:-4], '.jpg'))