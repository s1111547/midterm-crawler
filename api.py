import requests
import pandas as pd

"""
api.py

使用 PokeAPI 串接前 100 隻寶可夢的資料，
包括名稱、ID、屬性、身高、體重、基礎能力值，
並儲存為 CSV 檔案（api.csv）。
"""

# 建立空列表儲存每隻寶可夢的資料
pokemon_data = []

# 取得前 100 隻寶可夢
for i in range(1, 101):  # 寶可夢 ID 從 1 開始
    url = f'https://pokeapi.co/api/v2/pokemon/{i}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        name = data['name']
        poke_id = data['id']
        height = data['height']
        weight = data['weight']
        types = ', '.join([t['type']['name'] for t in data['types']])
        
        # 抓取六項基礎能力值：HP、Attack、Defense、Sp. Atk、Sp. Def、Speed
        stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
        
        pokemon_data.append({
            'Name': name,
            'ID': poke_id,
            'Height': height,
            'Weight': weight,
            'Types': types,
            'HP': stats.get('hp', 0),
            'Attack': stats.get('attack', 0),
            'Defense': stats.get('defense', 0),
            'Sp. Atk': stats.get('special-attack', 0),
            'Sp. Def': stats.get('special-defense', 0),
            'Speed': stats.get('speed', 0)
        })
    else:
        print(f"無法取得第 {i} 隻寶可夢的資料")

# 轉換成 DataFrame
df = pd.DataFrame(pokemon_data)

# 儲存為 CSV 檔案
df.to_csv('api.csv', index=False)

print("前 100 隻寶可夢資料已成功儲存為 api.csv！")
