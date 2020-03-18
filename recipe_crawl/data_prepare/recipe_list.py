import pandas as pd
import re
# 讀取
recipe = pd.read_csv('C://ntut//code//web_crawling//recipe_crawl//recipe.csv')
recipe_nutrient = pd.read_csv('C://ntut//code//web_crawling//recipe_crawl//recipe_nutrient.csv')
recipe_list = pd.merge(recipe_nutrient, recipe, left_on='name', right_on='recipeLink', how="left", sort=True)

# data cleaning
recipe_list = recipe_list[(recipe_list['protein'].str.contains("g")) &
                          (recipe_list['carb'].str.contains("g")) &
                          (recipe_list['fat'].str.contains("g"))]

### change type ####
# remove 'g'
recipe_list['fat'] = recipe_list['fat'].apply(lambda x: re.sub('g', '', x))
recipe_list['protein'] = recipe_list['protein'].apply(lambda x: re.sub('g', '', x))
recipe_list['carb'] = recipe_list['carb'].apply(lambda x: re.sub('g', '', x))
# give a number for some items only having a range
recipe_list['fat'] = recipe_list['fat'].apply(lambda x: re.sub('<1', '0.5', x))
recipe_list['protein'] = recipe_list['protein'].apply(lambda x: re.sub('<1', '0.5', x))
recipe_list['carb'] = recipe_list['carb'].apply(lambda x: re.sub('<1', '0.5', x))
# drop problem data
recipe_list = recipe_list.sort_values(['carb'])
recipe_list = recipe_list.drop(index=[450, 122, 688, 803, 120])
# create id
recipe_list['id'] = recipe_list['name'].apply(lambda x: x[::-1])  # 取後7碼，先反轉字串
recipe_list['id'] = recipe_list['id'].apply(lambda x: x[:7])  # 取前7
recipe_list['id'] = recipe_list['id'].apply(lambda x: x[::-1])  # 恢復順序
# organize the name
recipe_list['name'] = recipe_list['name'].apply(lambda x: x[7:])
recipe_list['name'] = recipe_list['name'].apply(lambda x: x[0:-8])

recipe_list = recipe_list.drop_duplicates()  # delete duplicate rows
recipe_list = recipe_list[recipe_list.calories != 0 ]   # remove 0 calories
# change type (str -> float)
recipe_list['fat'] = recipe_list['fat'].astype(float)
recipe_list['protein'] = recipe_list['protein'].astype(float)
recipe_list['carb'] = recipe_list['carb'].astype(float)

# sort
recipe_list = recipe_list.reset_index()
recipe_list = recipe_list.drop(columns=['index'])

recipe_list.to_csv('C://ntut//code//web_crawling//recipe_crawl//recipe_list.csv', encoding='utf_8_sig', index=False)
