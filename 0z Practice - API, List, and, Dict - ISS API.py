"""
============================================================================
List and Dictionaries. Example from the Student Slides.
============================================================================
"""
# Example 1: Embeded with 2 levels
# place = {
#     'name': 'The Anchor',
#     'post_code': 'E14 6HY',
#     'street_number': '54',
#     'location': {
#         'longitude': 127,
#         'latitude': 63,
#     }
# }
#
# location = place['location']
#
# print(location['latitude'])
# print(location['longitude'])

"""
============================================================================
Using a Test API to Practice List and Dictionary
============================================================================
"""

import requests

response = requests.get("http://api.open-notify.org/astros")
data = response.json()

crew = data['people']

print(crew['name'])     #technically this should work.


