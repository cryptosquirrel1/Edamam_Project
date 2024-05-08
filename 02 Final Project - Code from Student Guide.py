"""
============================================================================
CODE FROM STUDENT GUIDE. COPIED LINE BY LINE
============================================================================
"""
import requests
import json

def recipe_search(ingredient):
Register to get APP ID and KEY https://developer.edamam.com/
    app_id = '5ec8b15f'
    app_key = 'f872fab13b04a660a923e43c2e9f5654'
    result = requests.get(f'https://api.edamam.com/api/recipes/v2?type=public&beta=true&q={ingredient}&app_id={app_id}&app_key={app_key}').format(ingredient,app_id,app_key)
    data = result.json()
    return data['hits']                        ### RETURN DATA SEEMS TO BE AN ERROR

def run()
ingredient = input('Enter an ingredient: ')

results = recipe_search(ingredient)

for result in results:
    recipe = result['recipe']                 ### ASKING TO RETURN A VALUE FROM THE DICTIONARY FROM THE API
    print(recipe['label'])
    print(recipe['uri'])
    print()

run()                                        ### WHY DID WE END WITH RUN?
