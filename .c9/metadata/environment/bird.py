{"changed":true,"filter":false,"title":"bird.py","tooltip":"/bird.py","value":"\"\"\"\ntwitter_url = \"https://api.twitter.com/1.1/search/tweets.json?q=outkast\"\noauth = requests_oauthlib.OAuth1(\n    \"C7naPh6NBJhMYBX1JMAnLX67d\", \n    \"AkZqf5Dq6cnVlpVfMYDuGTaA3y0SLOxjGcS98swGs94ItLH1EL\",\n    \"3846948017-Vsqn57lvX9zmjtslCoA0gENtbs3jJP21OkyPvYQ\",\n    \"EVunEKabWXO69Kqi6uqkgIhxgUkzSwWayk1JsT9y77R1G\"\n)\n  \ntwitter_response = requests.get(\"https://api.twitter.com/1.1/search/tweets.json?q=outkast\", auth=oauth)\ntwitter_responsejson_body = response.json()\n\n\nprint(twitter_json_body[\"statuses\"][random.randint(1, 14)][\"text\"] + \"\\n\")\n\n@app.route(\"/\")  \ndef index(): \n    r = random.randint(1, 14)\n    a = random.randint(1, 14)\n    n = random.randint(1, 14)\n    tweet1 = twitter_json_body[\"statuses\"][r][\"text\"]\n    tweet2 = twitter_json_body[\"statuses\"][a][\"text\"]\n    tweet3 = twitter_json_body[\"statuses\"][n][\"text\"]\n    \n    return flask.render_template(\n       \"index.html\",\n        tweet1_src=tweet1, tweet2_src=tweet2, tweet3_src=tweet3) \n\"\"\"","undoManager":{"mark":-6,"position":100,"stack":[[{"start":{"row":32,"column":20},"end":{"row":32,"column":21},"action":"remove","lines":["`"],"id":181}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":1},"action":"insert","lines":["p"],"id":182},{"start":{"row":20,"column":1},"end":{"row":20,"column":2},"action":"insert","lines":["r"]},{"start":{"row":20,"column":2},"end":{"row":20,"column":3},"action":"insert","lines":["i"]},{"start":{"row":20,"column":3},"end":{"row":20,"column":4},"action":"insert","lines":["n"]},{"start":{"row":20,"column":4},"end":{"row":20,"column":5},"action":"insert","lines":["t"]}],[{"start":{"row":20,"column":5},"end":{"row":20,"column":7},"action":"insert","lines":["()"],"id":183}],[{"start":{"row":20,"column":6},"end":{"row":20,"column":7},"action":"insert","lines":["1"],"id":184}],[{"start":{"row":20,"column":6},"end":{"row":20,"column":7},"action":"remove","lines":["1"],"id":185}],[{"start":{"row":20,"column":6},"end":{"row":20,"column":38},"action":"insert","lines":["json_body[\"statuses\"][r][\"text\"]"],"id":186}],[{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"remove","lines":["r"],"id":187}],[{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"insert","lines":["1"],"id":188}],[{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"remove","lines":["1"],"id":189}],[{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"insert","lines":["0"],"id":190}],[{"start":{"row":20,"column":39},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":191}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":39},"action":"insert","lines":["print(json_body[\"statuses\"][0][\"text\"])"],"id":192}],[{"start":{"row":21,"column":39},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":193}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":39},"action":"insert","lines":["print(json_body[\"statuses\"][0][\"text\"])"],"id":194}],[{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"remove","lines":["0"],"id":195}],[{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"insert","lines":["2"],"id":196}],[{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"remove","lines":["2"],"id":197}],[{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"insert","lines":["1"],"id":198}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"remove","lines":["0"],"id":199}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"insert","lines":["2"],"id":200}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"remove","lines":["2"],"id":201}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"insert","lines":["3"],"id":202}],[{"start":{"row":20,"column":38},"end":{"row":20,"column":39},"action":"insert","lines":[" "],"id":203},{"start":{"row":20,"column":39},"end":{"row":20,"column":40},"action":"insert","lines":["+"]}],[{"start":{"row":20,"column":40},"end":{"row":20,"column":41},"action":"insert","lines":[" "],"id":204}],[{"start":{"row":20,"column":41},"end":{"row":20,"column":43},"action":"insert","lines":["\"\""],"id":205}],[{"start":{"row":20,"column":42},"end":{"row":20,"column":43},"action":"insert","lines":["\\"],"id":206},{"start":{"row":20,"column":43},"end":{"row":20,"column":44},"action":"insert","lines":["n"]}],[{"start":{"row":21,"column":38},"end":{"row":21,"column":44},"action":"insert","lines":["+ \"\\n\""],"id":207}],[{"start":{"row":22,"column":38},"end":{"row":22,"column":44},"action":"insert","lines":["+ \"\\n\""],"id":208}],[{"start":{"row":21,"column":38},"end":{"row":21,"column":39},"action":"insert","lines":[" "],"id":209}],[{"start":{"row":22,"column":38},"end":{"row":22,"column":39},"action":"insert","lines":[" "],"id":210}],[{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"remove","lines":["0"],"id":211}],[{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"insert","lines":["4"],"id":212}],[{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"remove","lines":["1"],"id":213}],[{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"insert","lines":["9"],"id":214},{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"insert","lines":["2"]}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"remove","lines":["3"],"id":215}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"insert","lines":["2"],"id":216}],[{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"remove","lines":["2"],"id":217},{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"remove","lines":["9"]}],[{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"insert","lines":["2"],"id":218},{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"insert","lines":["0"]}],[{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"remove","lines":["0"],"id":219},{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"remove","lines":["2"]}],[{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"insert","lines":["1"],"id":220},{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"insert","lines":["0"]}],[{"start":{"row":26,"column":28},"end":{"row":26,"column":29},"action":"remove","lines":["0"],"id":221},{"start":{"row":26,"column":27},"end":{"row":26,"column":28},"action":"remove","lines":["0"]},{"start":{"row":26,"column":26},"end":{"row":26,"column":27},"action":"remove","lines":["2"]}],[{"start":{"row":26,"column":26},"end":{"row":26,"column":27},"action":"insert","lines":["1"],"id":222},{"start":{"row":26,"column":27},"end":{"row":26,"column":28},"action":"insert","lines":["0"]}],[{"start":{"row":27,"column":28},"end":{"row":27,"column":29},"action":"remove","lines":["0"],"id":223},{"start":{"row":27,"column":27},"end":{"row":27,"column":28},"action":"remove","lines":["0"]},{"start":{"row":27,"column":26},"end":{"row":27,"column":27},"action":"remove","lines":["2"]}],[{"start":{"row":27,"column":26},"end":{"row":27,"column":27},"action":"insert","lines":["1"],"id":224},{"start":{"row":27,"column":27},"end":{"row":27,"column":28},"action":"insert","lines":["9"]}],[{"start":{"row":27,"column":27},"end":{"row":27,"column":28},"action":"remove","lines":["9"],"id":225}],[{"start":{"row":27,"column":27},"end":{"row":27,"column":28},"action":"insert","lines":["0"],"id":226}],[{"start":{"row":28,"column":28},"end":{"row":28,"column":29},"action":"remove","lines":["0"],"id":227},{"start":{"row":28,"column":27},"end":{"row":28,"column":28},"action":"remove","lines":["0"]},{"start":{"row":28,"column":26},"end":{"row":28,"column":27},"action":"remove","lines":["2"]}],[{"start":{"row":28,"column":26},"end":{"row":28,"column":27},"action":"insert","lines":["1"],"id":228},{"start":{"row":28,"column":27},"end":{"row":28,"column":28},"action":"insert","lines":["0"]}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"remove","lines":["2"],"id":229}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"insert","lines":["1"],"id":230},{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"insert","lines":["1"]}],[{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"remove","lines":["4"],"id":231}],[{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"insert","lines":["1"],"id":232},{"start":{"row":20,"column":29},"end":{"row":20,"column":30},"action":"insert","lines":["0"]}],[{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"remove","lines":["0"],"id":233},{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"remove","lines":["1"]}],[{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"insert","lines":["9"],"id":234}],[{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"remove","lines":["9"],"id":235}],[{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"insert","lines":["1"],"id":236},{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"insert","lines":["1"]}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"remove","lines":["1"],"id":237}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"insert","lines":["2"],"id":238}],[{"start":{"row":20,"column":29},"end":{"row":20,"column":30},"action":"remove","lines":["0"],"id":239}],[{"start":{"row":20,"column":29},"end":{"row":20,"column":30},"action":"insert","lines":["3"],"id":240}],[{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"remove","lines":["1"],"id":241}],[{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"insert","lines":["4"],"id":242}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"remove","lines":["2"],"id":243}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"insert","lines":["5"],"id":244}],[{"start":{"row":28,"column":27},"end":{"row":28,"column":28},"action":"remove","lines":["0"],"id":245}],[{"start":{"row":28,"column":27},"end":{"row":28,"column":28},"action":"insert","lines":["4"],"id":246}],[{"start":{"row":27,"column":27},"end":{"row":27,"column":28},"action":"remove","lines":["0"],"id":247}],[{"start":{"row":27,"column":27},"end":{"row":27,"column":28},"action":"insert","lines":["4"],"id":248}],[{"start":{"row":26,"column":27},"end":{"row":26,"column":28},"action":"remove","lines":["0"],"id":249}],[{"start":{"row":26,"column":27},"end":{"row":26,"column":28},"action":"insert","lines":["4"],"id":250}],[{"start":{"row":20,"column":0},"end":{"row":21,"column":47},"action":"remove","lines":["print(json_body[\"statuses\"][13][\"text\"] + \"\\n\")","print(json_body[\"statuses\"][14][\"text\"] + \"\\n\")"],"id":253}],[{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"remove","lines":["5"],"id":254}],[{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"insert","lines":["3"],"id":255}],[{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"remove","lines":["3"],"id":256}],[{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"insert","lines":["4"],"id":257}],[{"start":{"row":21,"column":28},"end":{"row":21,"column":30},"action":"remove","lines":["14"],"id":258},{"start":{"row":21,"column":28},"end":{"row":21,"column":49},"action":"insert","lines":["random.randint(1, 14)"]}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":1},"action":"insert","lines":["#"],"id":259}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":1},"action":"remove","lines":["#"],"id":260}],[{"start":{"row":36,"column":0},"end":{"row":39,"column":1},"action":"insert","lines":["app.run(","    port=int(os.getenv('PORT', 8080)),","    host=os.getenv('IP', '0.0.0.0')",")"],"id":261}],[{"start":{"row":35,"column":0},"end":{"row":39,"column":1},"action":"remove","lines":["","app.run(","    port=int(os.getenv('PORT', 8080)),","    host=os.getenv('IP', '0.0.0.0')",")"],"id":262}],[{"start":{"row":0,"column":0},"end":{"row":5,"column":0},"action":"remove","lines":["import random, json","import requests_oauthlib, requests","import flask","import os","",""],"id":263}],[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["","app = flask.Flask(__name__)","",""],"id":264}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["t"],"id":265},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["w"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["i"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["t"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["t"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["e"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["r"]}],[{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["_"],"id":266}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":1},"action":"insert","lines":["t"],"id":267},{"start":{"row":9,"column":1},"end":{"row":9,"column":2},"action":"insert","lines":["w"]},{"start":{"row":9,"column":2},"end":{"row":9,"column":3},"action":"insert","lines":["i"]},{"start":{"row":9,"column":3},"end":{"row":9,"column":4},"action":"insert","lines":["t"]},{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":["t"]},{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"insert","lines":["e"]},{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"insert","lines":["r"]}],[{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"insert","lines":["_"],"id":268}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["t"],"id":269},{"start":{"row":10,"column":1},"end":{"row":10,"column":2},"action":"insert","lines":["w"]},{"start":{"row":10,"column":2},"end":{"row":10,"column":3},"action":"insert","lines":["i"]},{"start":{"row":10,"column":3},"end":{"row":10,"column":4},"action":"insert","lines":["i"]}],[{"start":{"row":10,"column":3},"end":{"row":10,"column":4},"action":"remove","lines":["i"],"id":270}],[{"start":{"row":10,"column":3},"end":{"row":10,"column":4},"action":"insert","lines":["t"],"id":271},{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["t"]},{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"insert","lines":["e"]},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["r"]},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":["_"]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":8},"action":"remove","lines":["twitter_"],"id":272},{"start":{"row":10,"column":0},"end":{"row":10,"column":16},"action":"insert","lines":["twitter_response"]}],[{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["t"],"id":273},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["w"]},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["i"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["t"]},{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"insert","lines":["t"]},{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"insert","lines":["e"]},{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["r"]},{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["_"]}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"insert","lines":["t"],"id":274},{"start":{"row":16,"column":5},"end":{"row":16,"column":6},"action":"insert","lines":["w"]},{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"insert","lines":["i"]},{"start":{"row":16,"column":7},"end":{"row":16,"column":8},"action":"insert","lines":["t"]},{"start":{"row":16,"column":8},"end":{"row":16,"column":9},"action":"insert","lines":["t"]},{"start":{"row":16,"column":9},"end":{"row":16,"column":10},"action":"insert","lines":["e"]},{"start":{"row":16,"column":10},"end":{"row":16,"column":11},"action":"insert","lines":["r"]}],[{"start":{"row":16,"column":11},"end":{"row":16,"column":12},"action":"insert","lines":["_"],"id":275}],[{"start":{"row":16,"column":11},"end":{"row":16,"column":12},"action":"remove","lines":["_"],"id":276},{"start":{"row":16,"column":10},"end":{"row":16,"column":11},"action":"remove","lines":["r"]},{"start":{"row":16,"column":9},"end":{"row":16,"column":10},"action":"remove","lines":["e"]},{"start":{"row":16,"column":8},"end":{"row":16,"column":9},"action":"remove","lines":["t"]},{"start":{"row":16,"column":7},"end":{"row":16,"column":8},"action":"remove","lines":["t"]},{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"remove","lines":["i"]},{"start":{"row":16,"column":5},"end":{"row":16,"column":6},"action":"remove","lines":["w"]},{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"remove","lines":["t"]}],[{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"insert","lines":["t"],"id":277},{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"insert","lines":["w"]},{"start":{"row":20,"column":15},"end":{"row":20,"column":16},"action":"insert","lines":["i"]},{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"insert","lines":["t"]},{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"insert","lines":["t"]},{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"insert","lines":["e"]},{"start":{"row":20,"column":19},"end":{"row":20,"column":20},"action":"insert","lines":["r"]},{"start":{"row":20,"column":20},"end":{"row":20,"column":21},"action":"insert","lines":["_"]}],[{"start":{"row":21,"column":13},"end":{"row":21,"column":21},"action":"insert","lines":["twitter_"],"id":278}],[{"start":{"row":22,"column":13},"end":{"row":22,"column":21},"action":"insert","lines":["twitter_"],"id":279}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"insert","lines":["\"\""],"id":280}],[{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["\""],"id":281}],[{"start":{"row":27,"column":0},"end":{"row":27,"column":2},"action":"insert","lines":["\"\""],"id":282}],[{"start":{"row":27,"column":2},"end":{"row":27,"column":3},"action":"insert","lines":["\""],"id":283}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":27,"column":3},"end":{"row":27,"column":3},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":22,"state":"qqstring3","mode":"ace/mode/python"}},"timestamp":1567716755437}