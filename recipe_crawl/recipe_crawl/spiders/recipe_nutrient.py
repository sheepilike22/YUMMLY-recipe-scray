################################################
# test: scrapy shell <website>                 #
# try: scrapy runspider recipe_nutrient.py     #
# work: scrapy crawl recipe_crawl              #
################################################
#########################
## scrapy recipe detail #
#########################
import scrapy
import json
import pandas as pd
from scrapy import Request

detail = []
step = []
recipe = pd.read_csv('C://ntut//code//web_crawling//recipe_crawl//recipe.csv')

class RecipeItem(scrapy.Item):
    fat = scrapy.Field()
    protein = scrapy.Field()
    carb = scrapy.Field()
    calories = scrapy.Field()
    name = scrapy.Field()

class RecipeSpider(scrapy.Spider):
    name = "recipe_spider"
    start_urls = ["https://www.yummly.com/" + (recipe["recipeLink"][i]) + "#recipeDirections"
                  for i in range(930)]

    def parse(self, response):
        step.append(1)
        item = RecipeItem()  # Creating a new Item object
        item['name'] = recipe["recipeLink"][sum(step)]
        item['fat'] = response.css(".micro-text ::text").extract()[16]
        item['protein'] = response.css(".micro-text ::text").extract()[18]
        item['carb'] = response.css(".micro-text ::text").extract()[20]
        item['calories'] = response.css(".nutrition-bubble-flat-value .font-light ::text").extract()[0]
        # print(sum(step))
        yield item

        detail.append(item)

        if sum(step) == 929:
            print("Detail=" + str(detail))
            Detail = pd.DataFrame(detail, columns=['name', 'fat', 'protein', 'carb', 'calories'])
            Detail.to_csv('C://ntut//code//web_crawling//recipe_crawl//recipe_nutrient.csv', encoding='utf_8_sig', index=False)
#################################################################################################
