import json
import requests

# Root endpoint - accessible over HTTPS
# url = 'https://api.punkapi.com/v2/'
url = 'https://api.punkapi.com/v2/beers?page=2&per_page=80'

r = requests.get(url)

# Loading the text that comes back from the url into a python equivilant JSON list - the s on load represents the fact it comes from a string.
data = json.loads(r.text)

# Writing to sample.json
with open("beers.json", "w") as outfile:
    json.dump(data, outfile)