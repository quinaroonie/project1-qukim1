import random, json
import requests_oauthlib, requests
import flask
import os


app = flask.Flask(__name__)


url = "https://api.twitter.com/1.1/search/tweets.json?q=outkast"
oauth = requests_oauthlib.OAuth1(
    "C7naPh6NBJhMYBX1JMAnLX67d", 
    "AkZqf5Dq6cnVlpVfMYDuGTaA3y0SLOxjGcS98swGs94ItLH1EL",
    "3846948017-Vsqn57lvX9zmjtslCoA0gENtbs3jJP21OkyPvYQ",
    "EVunEKabWXO69Kqi6uqkgIhxgUkzSwWayk1JsT9y77R1G"
)
  
response = requests.get("https://api.twitter.com/1.1/search/tweets.json?q=outkast", auth=oauth)
json_body = response.json()


print(json_body["statuses"][random.randint(1, 14)]["text"] + "\n")

@app.route("/")  
def index(): 
    r = random.randint(1, 14)
    a = random.randint(1, 14)
    n = random.randint(1, 14)
    tweet1 = json_body["statuses"][r]["text"]
    tweet2 = json_body["statuses"][a]["text"]
    tweet3 = json_body["statuses"][n]["text"]
    
    return flask.render_template(
       "index.html",
        tweet1_src=tweet1, tweet2_src=tweet2, tweet3_src=tweet3) 

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)