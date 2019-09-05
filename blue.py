import random, requests, json
import requests_oauthlib
import flask
import os


app = flask.Flask(__name__)


api_token = '3yEHJrYc03grMh7SUZsRlZKDlQv-3NK0EyJ3iZQquV69HlpaCU9p28OoUejFOLu5'
url = "https://api.genius.com/search?q=Outkast"
my_headers = {
    "Authorization": "Bearer qiICws1IclXFRZmTwrTJI7k4m8vWoOwy2smTaAmQ2RuyiWztfrPPijT9ea2i2nA-"
}

response = requests.get(url, headers=my_headers)
json_body = response.json()


@app.route("/")  
def index(): 
    r = random.randint(1, 10)
    photo = json_body["response"]["hits"][r]["result"]["song_art_image_url"]
    title = json_body["response"]["hits"][r]["result"]["full_title"]
    artist = json_body["response"]["hits"][r]["result"]["primary_artist"]["image_url"]
    
    return flask.render_template(
       "index.html",
        album_src=photo, title_src=title, artist_src=artist) 
  
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)


""" 
url = "https://api.twitter.com/1.1/account/verify_credentials.json"
oauth = requests_oauthlib.OAuth1(
    "C7naPh6NBJhMYBX1JMAnLX67d", 
    "AkZqf5Dq6cnVlpVfMYDuGTaA3y0SLOxjGcS98swGs94ItLH1EL",
    "3846948017-Vsqn57lvX9zmjtslCoA0gENtbs3jJP21OkyPvYQ",
    "EVunEKabWXO69Kqi6uqkgIhxgUkzSwWayk1JsT9y77R1G"
)



response = requests.get(url, auth=oauth)

#print(response.json())

"""
