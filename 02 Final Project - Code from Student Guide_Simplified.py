"""
============================================================================
SIMPLIFYING STUDENT CODE GUIDE
============================================================================
"""

import recipe
import requests

recipe_search = input('enter a ingredient: ')
url = 'https://api.edamam.com/api/recipes/v2?type=public&beta=true&q={}&app_id=5ec8b15f&app_key=f872fab13b04a660a923e43c2e9f5654&field=uri&field=label'.format(recipe_search)

result = requests.get(url)
data = result.json()
retun data['hits']

print(data['hits']['recipe'])        
#only works when i add an integer in between. Why is that?. Error List indices must be integers or slices, not str. my objective is to return the sub-value of 'hits'
