import requests
import _json

# IDs
APP_ID = '5ec8b15f'
API_KEY = 'f872fab13b04a660a923e43c2e9f5654'
key_word = input("find new recipe ")
url = f'https://api.edamam.com/api/recipes/v2?type=public&beta=true&q={key_word}&app_id={APP_ID}&app_key={API_KEY}'
result = requests.get(url)
data = result.json()
data = data['hits']

print(data['hits']['recipe'])