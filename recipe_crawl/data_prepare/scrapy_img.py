import pandas as pd
import requests
import os

saveDir = './images/'

# 讀取
recipeList = pd.read_csv('C://ntut//code//web_crawling//recipe_crawl//recipe_list.csv')
List = []

if not os.path.isdir(saveDir):
    os.mkdir(saveDir)

for i in range(len(recipeList.recipeUrl)):
    img = requests.get(recipeList.recipeUrl[i])
    with open(saveDir + recipeList.name[i] + '.jpg', 'wb') as f:
        f.write(img.content)
        List.append(recipeList.name[i])

#######################################################################################
#######################################################################################
# # general method
# url = 'https://lh3.googleusercontent.com/h4TgL1G7B52_wOb_1bkfau-u_HryD6vYR90_3Ml2xIpMDB7Jedh1_2feEJprzovvFaO3WgCFxvB0SchfBzCSkn8'
# img = requests.get(url)
# with open(saveDir + 'test_image.jpg', 'wb') as f:
#     f.write(img.content)
