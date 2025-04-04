import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

# 設定 IMDB 網頁 URL 和自訂的 headers (模擬瀏覽器請求)
url = 'https://www.imdb.com/chart/top/'
headers = {"User-Agent": "Mozilla/5.0"}

# 發送 GET 請求來獲取網頁的 HTML 內容
response = requests.get(url, headers=headers)

# 使用 BeautifulSoup 解析網頁 HTML，這會讓我們能夠輕鬆提取需要的資料
soup = BeautifulSoup(response.text, 'html.parser')

# 找到包含電影資料的 <script> 標籤，這裡的資料是 JSON-LD 格式
script_tag = soup.find('script', type='application/ld+json')

# 解析 JSON 資料，將 JSON 字符串轉換成 Python 字典
data = json.loads(script_tag.string)

# 創建一個空列表來儲存電影資料
movies = []

# 循環遍歷每一部電影的資料
for item in data['itemListElement']:
    # 提取電影的名稱
    movie_name = item['item']['name']
    
    # 提取電影的評分
    rating = item['item']['aggregateRating']['ratingValue']
    


    # 提取電影的類型
    genre = item['item']['genre']
    
    # 儲存電影名稱、評分、年份和類型到 movies 列表
    movies.append([movie_name, rating, genre])

# 將電影資料轉換為 pandas DataFrame 格式，這樣可以更方便地進行處理和分析
df = pd.DataFrame(movies, columns=['Movie Title', 'Rating', 'Genre'])

# 儲存資料為 CSV 檔案
df.to_csv('static.csv', index=False)

# 顯示完成訊息，告訴使用者爬取的電影名稱和資料已經儲存為 CSV 檔案
print("爬取的電影名稱、評分、年份和類型已儲存為 static.csv")
