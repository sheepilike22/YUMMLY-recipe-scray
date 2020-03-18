##  use python console   ##
###########################
import pandas as pd

# 讀取
data = pd.read_csv('C://ntut//code//web_crawling//recipe_crawl//test.csv')
data1 = pd.read_csv('C://ntut//code//web_crawling//recipe_crawl//test1.csv')
data2 = pd.read_csv('C://ntut//code//web_crawling//recipe_crawl//test2.csv')
data3 = pd.read_csv('C://ntut//code//web_crawling//recipe_crawl//test3.csv')
data4 = pd.read_csv('C://ntut//code//web_crawling//recipe_crawl//test4.csv')
data5 = pd.read_csv('C://ntut//code//web_crawling//recipe_crawl//test5.csv')
data6 = pd.read_csv('C://ntut//code//web_crawling//recipe_crawl//test6.csv')
data7 = pd.read_csv('C://ntut//code//web_crawling//recipe_crawl//test7.csv')
data8 = pd.read_csv('C://ntut//code//web_crawling//recipe_crawl//test8.csv')
data9 = pd.read_csv('C://ntut//code//web_crawling//recipe_crawl//test9.csv')

# 使用 concat 合併 axis=0 為直向合併
dataSet = pd.concat([data, data1, data2, data3, data4, data5, data6, data7, data8, data9], axis=0)
#print(data)

# 輸出
dataSet.to_csv('C://ntut//code//web_crawling//recipe_crawl//recipe.csv', encoding='utf_8_sig', index=False)