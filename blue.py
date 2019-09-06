import random, json, flask
import requests_oauthlib, requests
import os


app = flask.Flask(__name__)

#https://api.genius.com/search?q=outkast%2C%20generation&src=typed_query&f=top

api_token = '3yEHJrYc03grMh7SUZsRlZKDlQv-3NK0EyJ3iZQquV69HlpaCU9p28OoUejFOLu5'
genius_url = "https://api.genius.com/search?q=Outkast"

twitter_url = "https://api.twitter.com/1.1/search/tweets.json?q=outkast"
twitter_url2 = "https://api.twitter.com/1.1/search/tweets.json?q=andre_3000"
oauth = requests_oauthlib.OAuth1(
    "C7naPh6NBJhMYBX1JMAnLX67d", 
    "AkZqf5Dq6cnVlpVfMYDuGTaA3y0SLOxjGcS98swGs94ItLH1EL",
    "3846948017-Vsqn57lvX9zmjtslCoA0gENtbs3jJP21OkyPvYQ",
    "EVunEKabWXO69Kqi6uqkgIhxgUkzSwWayk1JsT9y77R1G"
)

my_headers = {
    "Authorization": "Bearer qiICws1IclXFRZmTwrTJI7k4m8vWoOwy2smTaAmQ2RuyiWztfrPPijT9ea2i2nA-"
}

genius_response = requests.get(genius_url, headers=my_headers)
genius_json_body = genius_response.json()
twitter_response = requests.get(twitter_url, auth=oauth)
twitter_json_body = twitter_response.json()
twitter2_response = requests.get(twitter_url2, auth=oauth)
twitter2_json_body = twitter2_response.json()


@app.route("/")  
def index(): 
    r = random.randint(0, 9)
    a = random.randint(0, 14)
    n = random.randint(0, 14)
    d = random.randint(0, 14)
    photo = genius_json_body["response"]["hits"][r]["result"]["song_art_image_url"]
    title = genius_json_body["response"]["hits"][r]["result"]["full_title"]
    artist = genius_json_body["response"]["hits"][r]["result"]["primary_artist"]["image_url"]
    tweet1 = twitter_json_body["statuses"][a]["text"]
    tweet2 = twitter_json_body["statuses"][n]["text"]
    tweet3 = twitter2_json_body["statuses"][d]["text"]
    
    return flask.render_template(
       "index.html",
        album_src=photo, title_src=title, artist_src=artist, tweet1_src=tweet1, tweet2_src=tweet2, tweet3_src=tweet3) 
  
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)
