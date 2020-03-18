import pandas as pd
import requests
import os

saveDir = './images/'

# 讀取
recipeList = pd.read_csv('C://ntut//code//web_crawling//recipe_crawl//recipe_list.csv')

if not os.path.isdir(saveDir):
    os.mkdir(saveDir)

for i in range(len(recipeList.recipeUrl)):
    img = requests.get(recipeList.recipeUrl[i])
    with open(saveDir + recipeList.name[i] + '.jpg', 'wb') as f:
        f.write(img.content)

### check the list ###
import glob

image_list = []
for filename in glob.glob('C:/ntut/code/web_crawling/recipe_crawl/data_prepare/images/*.jpg'):
    image_list.append(os.path.split(filename)[-1])

image_list = pd.DataFrame(image_list, columns=['image_list'])
image_list = image_list['image_list'].apply(lambda x: x[:-4])  # remove '.jpg'
image_list = pd.DataFrame(image_list, columns=['image_list'])  #rename column

List = pd.merge(image_list, recipeList, left_on='image_list', right_on='name', how="left", sort=True)
List = List.drop_duplicates()  # delete duplicate rows
#######################################################################################
#######################################################################################
# # general method
# url = 'https://lh3.googleusercontent.com/h4TgL1G7B52_wOb_1bkfau-u_HryD6vYR90_3Ml2xIpMDB7Jedh1_2feEJprzovvFaO3WgCFxvB0SchfBzCSkn8'
# img = requests.get(url)
# with open(saveDir + 'test_image.jpg', 'wb') as f:
#     f.write(img.content)
