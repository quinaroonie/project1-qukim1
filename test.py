import requests
import json

api_token = '3yEHJrYc03grMh7SUZsRlZKDlQv-3NK0EyJ3iZQquV69HlpaCU9p28OoUejFOLu5'

url = "https://api.genius.com/search?q=Outkast"

my_headers = {
    "Authorization": "Bearer qiICws1IclXFRZmTwrTJI7k4m8vWoOwy2smTaAmQ2RuyiWztfrPPijT9ea2i2nA-"
}

response = requests.get(url, headers=my_headers)
json_body = response.json()
print(json_body["response"]["hits"][0]["type"])
print(json_body["response"]["hits"][1]["result"]["song_art_image_url"])
print(json_body["response"]["hits"][2]["result"]["song"])
