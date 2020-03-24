#####################
##  console       ###
#####################
import pandas as pd
import requests
import os

saveDir = './images/'

# 讀取
recipeList = pd.read_csv('C://ntut//code//web_crawling//recipe_crawl//recipe_list.csv')
recipeList['image'] = recipeList.imgURL+"=s640-c-rw-v1-e365"
# recipeList1=recipeList[recipeList.calories<=200]
# recipeList2 = recipeList[(recipeList.calories>200)&(recipeList.calories<=400)]
# recipeList3 = recipeList[(recipeList.calories>400)&(recipeList.calories<=600)]
# recipeList4 = recipeList[(recipeList.calories>600)&(recipeList.calories<=800)]
# recipeList5 = recipeList[(recipeList.calories>800)&(recipeList.calories<=1000)]
# recipeList6 = recipeList[recipeList.calories>1000]


if not os.path.isdir(saveDir):
    os.mkdir(saveDir)

for i in range(len(recipeList.image)):
# for i in range(len(recipeList.imgURL)):
    id=recipeList.index[i]
    img = requests.get(recipeList.image[id])
    # img = requests.get(recipeList.imgURL[i])
    with open(saveDir + recipeList.recipeName[id] + '.jpg', 'wb') as f:
        f.write(img.content)

############################ check the list ####################################
###########
# CONSOLE #
###########
import glob

image_list = []
for filename in glob.glob('C:/ntut/code/web_crawling/recipe_crawl/data_prepare/images_1/*.jpg'):
    image_list.append(os.path.split(filename)[-1])

image_list = pd.DataFrame(image_list, columns=['image_list'])
image_list = image_list['image_list'].apply(lambda x: x[:-4])  # remove '.jpg'
image_list = pd.DataFrame(image_list, columns=['image_list'])  #rename column

List = pd.merge(image_list, recipeList, left_on='image_list', right_on='recipeName', how="left", sort=True)
List = List.drop_duplicates()  # delete duplicate rows
#######################################################################################
#######################################################################################
# # general method
# url = 'https://lh3.googleusercontent.com/h4TgL1G7B52_wOb_1bkfau-u_HryD6vYR90_3Ml2xIpMDB7Jedh1_2feEJprzovvFaO3WgCFxvB0SchfBzCSkn8'
# img = requests.get(url)
# with open(saveDir + 'test_image.jpg', 'wb') as f:
#     f.write(img.content)
