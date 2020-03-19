import pandas as pd
import re
# 讀取
recipe_unique = pd.read_csv('C://ntut//code//web_crawling//recipe_crawl//recipe_unique.csv')
recipe_repeat = pd.read_csv('C://ntut//code//web_crawling//recipe_crawl//recipe_repeat.csv')
recipe_nutrient = pd.read_csv('C://ntut//code//web_crawling//recipe_crawl//recipe_nutrient.csv')

recipe_nutrient_unique = recipe_nutrient[~recipe_nutrient.name.isin(recipe_repeat.recipeName)]
recipe_nutrient_repeat = recipe_nutrient[recipe_nutrient.name.isin(recipe_repeat.recipeName)]

recipe_unique_list = pd.merge(recipe_nutrient_unique, recipe_unique, left_on='name', right_on='recipeName', how="left", sort=True)
recipe_repeat['calories'] = [380, 80, 650, 220, 330, 440, 210, 130, 110, 170, 140, 250, 220, 830, 360]   # add the calories from website
recipe_repeat_list = pd.merge(recipe_nutrient_repeat, recipe_repeat,
                              left_on=['name', 'calories'], right_on=['recipeName', 'calories'],
                              how="left", sort=True)

recipe_list = pd.concat([recipe_unique_list, recipe_repeat_list], axis=0)

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
# delete (by index)
recipe_list = recipe_list.drop(index=[739, 265, 393, 776])
recipe_list = recipe_list[recipe_list.calories != 0 ]   # remove 0 calories
# # create id
# recipe_list['id'] = recipe_list['name'].apply(lambda x: x[::-1])  # 取後7碼，先反轉字串
# recipe_list['id'] = recipe_list['id'].apply(lambda x: x[:7])  # 取前7
# recipe_list['id'] = recipe_list['id'].apply(lambda x: x[::-1])  # 恢復順序

# change type (str -> float)
recipe_list['fat'] = recipe_list['fat'].astype(float)
recipe_list['protein'] = recipe_list['protein'].astype(float)
recipe_list['carb'] = recipe_list['carb'].astype(float)

# sort
recipe_list = recipe_list.reset_index()
recipe_list = recipe_list.drop(columns=['index'])

# recipeNAME
recipe_list['recipeName'] = recipe_list['recipeLink'].apply(lambda x: x[7:])


recipe_list = pd.DataFrame({'recipeName': recipe_list.recipeName,
                            'recipeLink': recipe_list.recipeLink,
                            'name': recipe_list.name,
                            'calories': recipe_list.calories,
                            'fat': recipe_list.fat,
                            'protein': recipe_list.protein,
                            'carb': recipe_list.carb,
                            'imgURL': recipe_list.recipeUrl,
                            'click_count': recipe_list.click_count})

recipe_list = recipe_list.drop_duplicates()
recipe_list.to_csv('C://ntut//code//web_crawling//recipe_crawl//recipe_list.csv', encoding='utf_8_sig', index=False)
