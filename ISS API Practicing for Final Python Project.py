# List and Dictionaries.

### Practicing Lists and Dictionaries Student Slides
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


### Using API and List and Dictionary
## I'm using a test API
import requests

response = requests.get("http://api.open-notify.org/astros")
data = response.json()

crew = data['people']

print(crew['name']) #technically this should work.


