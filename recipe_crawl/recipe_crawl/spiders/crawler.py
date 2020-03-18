########################################
# test: scrapy shell <website>         #
# try: scrapy runspider crawler.py     #
# work: scrapy crawl recipe_crawl      #
########################################
#########################
## scrapy recipe detail #
#########################
# import scrapy
# import json
#
# class RecipeSpider(scrapy.Spider):
#     name = "recipe_spider"
#     start_urls = ["https://www.yummly.com/recipes"]
#     #start_urls = ["https://mapi.yummly.com/mapi/v17/content/search?solr.seo_boost=new&start=1&maxResult=36&fetchUserCollections=false&allowedContent=single_recipe&allowedContent=suggested_search&allowedContent=related_search&allowedContent=article&allowedContent=video&allowedContent=generic_cta&guided-search=true&solr.view_type=search_internal"]
#
#     def parse(self, response):
#         recipeName = response.css(".font-normal::text").extract()
#         recipeLink = response.css("div.recipe-card-img-wrapper a").xpath("@href").extract()
#
#         yield {"recipeName": recipeName,
#                "recipeLink": recipeLink}
#
#         print("recipeName = ", recipeName)
#         print("recipeLink = ", recipeLink)
#################################################################################################
#################################################################################################
#######################
## scrapy recipeLink  #
#######################
import urllib
import urllib.request
import re
import json
import pandas as pd

htmltext = urllib.request.urlopen(
    "https://mapi.yummly.com/mapi/v17/content/search?solr.seo_boost=new&start=0&maxResult=953&fetchUserCollections=false&allowedContent=single_recipe&allowedContent=suggested_search&allowedContent=related_search&allowedContent=article&allowedContent=video&allowedContent=generic_cta&guided-search=true&solr.view_type=search_internal")

data = json.load(htmltext)
tracking_id_List = []
name_List = []
url_List = []
click_count_List = []
# 不能範圍太大
# # 0~49 test
# for i in range(50):
#     tracking_id = data["feed"][i]["tracking-id"]
#     name = data["feed"][i]["display"]["displayName"]
#     url = data["feed"][i]["display"]["images"][0]
#     click_count = data["feed"][i]["content"]["yums"]["count"]
#
#     tracking_id_List.append(tracking_id)
#     name_List.append(name)
#     url_List.append(url)
#     click_count_List.append(click_count)
#     # print(data["feed"][i]["tracking-id"])

# # 50~100 test1
# for i in range(50, 100):
#     tracking_id = data["feed"][i]["tracking-id"]
#     name = data["feed"][i]["display"]["displayName"]
#     url = data["feed"][i]["display"]["images"][0]
#     click_count= data ["feed"][i]["content"]["yums"]["count"]
#
#     tracking_id_List.append(tracking_id)
#     name_List.append(name)
#     url_List.append(url)
#     click_count_List.append(click_count)
#     # print(data["feed"][i]["tracking-id"])

# # 101~200 test2
# for i in range(101, 200):
#     tracking_id = data["feed"][i]["tracking-id"]
#     name = data["feed"][i]["display"]["displayName"]
#     url = data["feed"][i]["display"]["images"][0]
#     click_count= data ["feed"][i]["content"]["yums"]["count"]
#
#     tracking_id_List.append(tracking_id)
#     name_List.append(name)
#     url_List.append(url)
#     click_count_List.append(click_count)
#     # print(data["feed"][i]["tracking-id"])

# 201~350 test3
# for i in range(201, 350):
#     tracking_id = data["feed"][i]["tracking-id"]
#     name = data["feed"][i]["display"]["displayName"]
#     url = data["feed"][i]["display"]["images"][0]
#     click_count= data["feed"][i]["content"]["yums"]["count"]
#
#     tracking_id_List.append(tracking_id)
#     name_List.append(name)
#     url_List.append(url)
#     click_count_List.append(click_count)
#     # print(data["feed"][i]["tracking-id"])

# 351~420 test4
# for i in range(351, 420):
#     tracking_id = data["feed"][i]["tracking-id"]
#     name = data["feed"][i]["display"]["displayName"]
#     url = data["feed"][i]["display"]["images"][0]  # only get the string
#     click_count= data["feed"][i]["content"]["yums"]["count"]
#
#     tracking_id_List.append(tracking_id)
#     name_List.append(name)
#     url_List.append(url)
#     click_count_List.append(click_count)
#     # print(data["feed"][i]["tracking-id"])

# 421~500 test5
# for i in range(421, 500):
#     tracking_id = data["feed"][i]["tracking-id"]
#     name = data["feed"][i]["display"]["displayName"]
#     url = data["feed"][i]["display"]["images"][0]  # only get the string
#     click_count = data["feed"][i]["content"]["yums"]["count"]
#
#     tracking_id_List.append(tracking_id)
#     name_List.append(name)
#     url_List.append(url)
#     click_count_List.append(click_count)
#     # print(data["feed"][i]["tracking-id"])

# 501~600 test6
# for i in range(501, 600):
#     tracking_id = data["feed"][i]["tracking-id"]
#     name = data["feed"][i]["display"]["displayName"]
#     url = data["feed"][i]["display"]["images"][0]  # only get the string
#     click_count= data["feed"][i]["content"]["yums"]["count"]
#
#     tracking_id_List.append(tracking_id)
#     name_List.append(name)
#     url_List.append(url)
#     click_count_List.append(click_count)
#     # print(data["feed"][i]["tracking-id"])

# 601~700 test7
# for i in range(601, 700):
#     tracking_id = data["feed"][i]["tracking-id"]
#     name = data["feed"][i]["display"]["displayName"]
#     url = data["feed"][i]["display"]["images"][0]  # only get the string
#     click_count= data["feed"][i]["content"]["yums"]["count"]
#
#     tracking_id_List.append(tracking_id)
#     name_List.append(name)
#     url_List.append(url)
#     click_count_List.append(click_count)
#     # print(data["feed"][i]["tracking-id"])

# 701~800 test8
# for i in range(701, 800):
#     tracking_id = data["feed"][i]["tracking-id"]
#     name = data["feed"][i]["display"]["displayName"]
#     url = data["feed"][i]["display"]["images"][0]  # only get the string
#     click_count = data["feed"][i]["content"]["yums"]["count"]
#
#     tracking_id_List.append(tracking_id)
#     name_List.append(name)
#     url_List.append(url)
#     click_count_List.append(click_count)
#     # print(data["feed"][i]["tracking-id"])

# 801~938 test9
for i in range(801, 938):
    tracking_id = data["feed"][i]["tracking-id"]
    name = data["feed"][i]["display"]["displayName"]
    url = data["feed"][i]["display"]["images"][0]  # only get the string
    click_count = data["feed"][i]["content"]["yums"]["count"]

    tracking_id_List.append(tracking_id)
    name_List.append(name)
    url_List.append(url)
    click_count_List.append(click_count)
    # print(data["feed"][i]["tracking-id"])

# print(tracking_id_List)
# print(name_List)
# print(url_List)
# print(click_count)

# 資料匯出
Data = {'recipeLink': tracking_id_List,
        'recipeName': name_List,
        'recipeUrl': url_List,
        'click_count': click_count_List}
recipe_Data = pd.DataFrame(Data)
recipe_Data.to_csv('C://ntut//code//web_crawling//recipe_crawl//test9.csv', encoding='utf_8_sig', index=False)

#################################################################################################
#################################################################################################
# (code only work on the scrapy shell)
# # other example

# import scrapy
# import json
# from scrapy.utils import response

# scrapy shell="https://mapi.yummly.com/mapi/v17/content/search?solr.seo_boost=new&start=1&maxResult=500&fetchUserCollections=false&allowedContent=single_recipe&allowedContent=suggested_search&allowedContent=related_search&allowedContent=article&allowedContent=video&allowedContent=generic_cta&guided-search=true&solr.view_type=search_internal"

# js = json.loads(response.body)

# # test 1
#click_count=js["feed"][0]['content']['yums']['count']
# recipe_link=js["feed"][0]["tracking-id"]
# yield {"recipe_link" : recipe_link}
# print(recipe_link)


# # test 2 (array cannot store string)
# for i in range(10):
#   recipe_link = js["feed"][i]["tracking-id"]
#   yield {"recipe_link": recipe_link}
# print(recipe_link)



