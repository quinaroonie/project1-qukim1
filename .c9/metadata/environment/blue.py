{"filter":false,"title":"blue.py","tooltip":"/blue.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":18,"column":0},"end":{"row":18,"column":2},"action":"insert","lines":["\"\""],"id":151,"ignore":true}],[{"start":{"row":18,"column":2},"end":{"row":18,"column":4},"action":"insert","lines":["\" "],"id":152,"ignore":true}],[{"start":{"row":18,"column":4},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":153,"ignore":true}],[{"start":{"row":34,"column":0},"end":{"row":34,"column":3},"action":"insert","lines":["\"\"\""],"id":154,"ignore":true}],[{"start":{"row":31,"column":0},"end":{"row":32,"column":0},"action":"remove","lines":["",""],"id":155,"ignore":true}],[{"start":{"row":31,"column":0},"end":{"row":32,"column":0},"action":"remove","lines":["",""],"id":156,"ignore":true}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"remove","lines":["#"],"id":157,"ignore":true}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":67},"action":"remove","lines":["url = \"https://api.twitter.com/1.1/account/verify_credentials.json\""],"id":158,"ignore":true}],[{"start":{"row":18,"column":4},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":159,"ignore":true}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":67},"action":"insert","lines":["url = \"https://api.twitter.com/1.1/account/verify_credentials.json\""],"id":160,"ignore":true}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":1},"action":"remove","lines":[""," "],"id":161,"ignore":true}],[{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"remove","lines":["",""],"id":162,"ignore":true}],[{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":163}],[{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"remove","lines":["",""],"id":164}],[{"start":{"row":15,"column":0},"end":{"row":28,"column":0},"action":"insert","lines":["api_token = '3yEHJrYc03grMh7SUZsRlZKDlQv-3NK0EyJ3iZQquV69HlpaCU9p28OoUejFOLu5'","","url = \"https://api.genius.com/search?q=Outkast\"","","my_headers = {","    \"Authorization\": \"Bearer qiICws1IclXFRZmTwrTJI7k4m8vWoOwy2smTaAmQ2RuyiWztfrPPijT9ea2i2nA-\"","}","","response = requests.get(url, headers=my_headers)","json_body = response.json()","print(json_body[\"response\"][\"hits\"][0][\"type\"])","print(json_body[\"response\"][\"hits\"][1][\"result\"][\"song_art_image_url\"])","print(json_body[\"response\"][\"hits\"][2][\"result\"][\"song\"])",""],"id":165}],[{"start":{"row":28,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":166}],[{"start":{"row":28,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":167}],[{"start":{"row":1,"column":14},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":168},{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["i"]},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["m"]},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":["p"]},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["o"]},{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":["r"]},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":[" "],"id":169}],[{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"remove","lines":[" "],"id":170},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"remove","lines":[","]}],[{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":[" "],"id":171},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":["f"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["r"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["o"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":["m"]}],[{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":[" "],"id":172},{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"insert","lines":["F"]},{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"insert","lines":["l"]},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":["a"]},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"insert","lines":["s"]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"insert","lines":["k"]}],[{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"remove","lines":["k"],"id":173},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"remove","lines":["s"]},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"remove","lines":["a"]},{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"remove","lines":["l"]},{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"remove","lines":["F"]},{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"remove","lines":[" "]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"remove","lines":["m"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"remove","lines":["o"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"remove","lines":["r"]},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"remove","lines":["f"]},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"remove","lines":[" "]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"remove","lines":["k"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"remove","lines":["s"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"remove","lines":["a"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"remove","lines":["l"]},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"remove","lines":["f"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"remove","lines":[" "]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"remove","lines":["t"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"remove","lines":["r"]}],[{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"remove","lines":["o"],"id":174},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"remove","lines":["p"]},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"remove","lines":["m"]},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"remove","lines":["i"]}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":21},"action":"insert","lines":["from flask import Flask","app = Flask(__name__)"],"id":175}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":21},"action":"remove","lines":["app = Flask(__name__)"],"id":176}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":27},"action":"remove","lines":["app = flask.Flask(__name__)"],"id":177},{"start":{"row":6,"column":0},"end":{"row":6,"column":21},"action":"insert","lines":["app = Flask(__name__)"]}],[{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"remove","lines":["'"],"id":178}],[{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["\""],"id":179}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"remove","lines":["'"],"id":180}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["\""],"id":181}],[{"start":{"row":15,"column":1},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":182},{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""]},{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["",""]},{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""]},{"start":{"row":19,"column":0},"end":{"row":20,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":17,"column":0},"end":{"row":23,"column":0},"action":"insert","lines":["def index(): ","    r = random.randint(1, 100)","    return flask.render_template(","        \"index.html\", ","        random_num=r # Google search ‘python kwaargs’","    )",""],"id":183}],[{"start":{"row":9,"column":13},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":184},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["p"],"id":185},{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"insert","lines":["h"]},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["t"]},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":["o"]}],[{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"remove","lines":["o"],"id":186},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"remove","lines":["t"]}],[{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["o"],"id":187},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":["t"]},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["o"]}],[{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":[" "],"id":188},{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":["="]}],[{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":[" "],"id":189}],[{"start":{"row":10,"column":12},"end":{"row":10,"column":77},"action":"insert","lines":["json_body[\"response\"][\"hits\"][1][\"result\"][\"song_art_image_url\"])"],"id":190}],[{"start":{"row":10,"column":77},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":191},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":11,"column":4},"end":{"row":12,"column":30},"action":"remove","lines":["","    r = random.randint(1, 100)"],"id":192}],[{"start":{"row":37,"column":0},"end":{"row":41,"column":57},"action":"remove","lines":["response = requests.get(url, headers=my_headers)","json_body = response.json()","print(json_body[\"response\"][\"hits\"][0][\"type\"])","print(json_body[\"response\"][\"hits\"][1][\"result\"][\"song_art_image_url\"])","print(json_body[\"response\"][\"hits\"][2][\"result\"][\"song\"])"],"id":193}],[{"start":{"row":16,"column":1},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":194},{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":196},{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"insert","lines":["",""]},{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":8,"column":0},"end":{"row":12,"column":57},"action":"insert","lines":["response = requests.get(url, headers=my_headers)","json_body = response.json()","print(json_body[\"response\"][\"hits\"][0][\"type\"])","print(json_body[\"response\"][\"hits\"][1][\"result\"][\"song_art_image_url\"])","print(json_body[\"response\"][\"hits\"][2][\"result\"][\"song\"])"],"id":197}],[{"start":{"row":18,"column":1},"end":{"row":18,"column":4},"action":"insert","lines":["   "],"id":198}],[{"start":{"row":18,"column":4},"end":{"row":18,"column":8},"action":"insert","lines":["    "],"id":199}],[{"start":{"row":18,"column":4},"end":{"row":18,"column":8},"action":"remove","lines":["    "],"id":200}],[{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"insert","lines":["r"],"id":201},{"start":{"row":18,"column":5},"end":{"row":18,"column":6},"action":"insert","lines":["e"]},{"start":{"row":18,"column":6},"end":{"row":18,"column":7},"action":"insert","lines":["t"]},{"start":{"row":18,"column":7},"end":{"row":18,"column":8},"action":"insert","lines":["u"]},{"start":{"row":18,"column":8},"end":{"row":18,"column":9},"action":"insert","lines":["r"]},{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":18,"column":10},"end":{"row":18,"column":11},"action":"insert","lines":[" "],"id":202},{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"insert","lines":["f"]},{"start":{"row":18,"column":12},"end":{"row":18,"column":13},"action":"insert","lines":["l"]},{"start":{"row":18,"column":13},"end":{"row":18,"column":14},"action":"insert","lines":["a"]},{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":["s"]},{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"insert","lines":["k"]},{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"insert","lines":[","]},{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"insert","lines":["r"]},{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"insert","lines":["e"]},{"start":{"row":18,"column":19},"end":{"row":18,"column":20},"action":"insert","lines":["n"]}],[{"start":{"row":18,"column":20},"end":{"row":18,"column":21},"action":"insert","lines":["d"],"id":203},{"start":{"row":18,"column":21},"end":{"row":18,"column":22},"action":"insert","lines":["e"]},{"start":{"row":18,"column":22},"end":{"row":18,"column":23},"action":"insert","lines":["r"]}],[{"start":{"row":18,"column":17},"end":{"row":18,"column":23},"action":"remove","lines":["render"],"id":204},{"start":{"row":18,"column":17},"end":{"row":18,"column":32},"action":"insert","lines":["render_template"]}],[{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"remove","lines":[","],"id":205}],[{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"insert","lines":["."],"id":206}],[{"start":{"row":18,"column":34},"end":{"row":18,"column":35},"action":"remove","lines":[" "],"id":207},{"start":{"row":18,"column":33},"end":{"row":18,"column":34},"action":"remove","lines":[" "]},{"start":{"row":18,"column":32},"end":{"row":18,"column":33},"action":"remove","lines":[" "]}],[{"start":{"row":18,"column":32},"end":{"row":18,"column":34},"action":"insert","lines":["()"],"id":208}],[{"start":{"row":18,"column":33},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":209},{"start":{"row":19,"column":0},"end":{"row":19,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":19,"column":8},"end":{"row":19,"column":10},"action":"insert","lines":["''"],"id":210}],[{"start":{"row":19,"column":8},"end":{"row":19,"column":10},"action":"remove","lines":["''"],"id":211}],[{"start":{"row":19,"column":8},"end":{"row":19,"column":10},"action":"insert","lines":["\"\""],"id":212}],[{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"insert","lines":["i"],"id":213},{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":["n"]},{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":["d"]},{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"insert","lines":["e"]},{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"insert","lines":["x"]},{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"insert","lines":["."]}],[{"start":{"row":19,"column":15},"end":{"row":19,"column":16},"action":"insert","lines":["h"],"id":214},{"start":{"row":19,"column":16},"end":{"row":19,"column":17},"action":"insert","lines":["t"]},{"start":{"row":19,"column":17},"end":{"row":19,"column":18},"action":"insert","lines":["m"]},{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"insert","lines":["l"]}],[{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"insert","lines":[","],"id":215}],[{"start":{"row":19,"column":21},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":216},{"start":{"row":20,"column":0},"end":{"row":20,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":20,"column":8},"end":{"row":20,"column":9},"action":"insert","lines":["p"],"id":217},{"start":{"row":20,"column":9},"end":{"row":20,"column":10},"action":"insert","lines":["h"]}],[{"start":{"row":20,"column":9},"end":{"row":20,"column":10},"action":"remove","lines":["h"],"id":218},{"start":{"row":20,"column":8},"end":{"row":20,"column":9},"action":"remove","lines":["p"]}],[{"start":{"row":20,"column":8},"end":{"row":20,"column":9},"action":"insert","lines":["a"],"id":219},{"start":{"row":20,"column":9},"end":{"row":20,"column":10},"action":"insert","lines":["l"]},{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"insert","lines":["b"]},{"start":{"row":20,"column":11},"end":{"row":20,"column":12},"action":"insert","lines":["u"]},{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"insert","lines":["m"]},{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"insert","lines":["_"]}],[{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"insert","lines":["o"],"id":220},{"start":{"row":20,"column":15},"end":{"row":20,"column":16},"action":"insert","lines":["h"]},{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"insert","lines":["o"]},{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"insert","lines":["t"]},{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"insert","lines":["o"]}],[{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"remove","lines":["o"],"id":221},{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"remove","lines":["t"]},{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"remove","lines":["o"]},{"start":{"row":20,"column":15},"end":{"row":20,"column":16},"action":"remove","lines":["h"]},{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"remove","lines":["o"]}],[{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"insert","lines":["p"],"id":222}],[{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"remove","lines":["p"],"id":223},{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"remove","lines":["_"]},{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"remove","lines":["m"]}],[{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"insert","lines":["m"],"id":224},{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"insert","lines":["p"]}],[{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"remove","lines":["p"],"id":225}],[{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"insert","lines":["_"],"id":226},{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"insert","lines":["p"]}],[{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"remove","lines":["p"],"id":227},{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"remove","lines":["_"]}],[{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"insert","lines":["_"],"id":228},{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"insert","lines":["s"]},{"start":{"row":20,"column":15},"end":{"row":20,"column":16},"action":"insert","lines":["o"]},{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"insert","lines":["r"]},{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"insert","lines":["u"]},{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"insert","lines":["c"]},{"start":{"row":20,"column":19},"end":{"row":20,"column":20},"action":"insert","lines":["e"]}],[{"start":{"row":20,"column":19},"end":{"row":20,"column":20},"action":"remove","lines":["e"],"id":229},{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"remove","lines":["c"]},{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"remove","lines":["u"]},{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"remove","lines":["r"]}],[{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"insert","lines":["u"],"id":230},{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"insert","lines":["r"]},{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"insert","lines":["c"]},{"start":{"row":20,"column":19},"end":{"row":20,"column":20},"action":"insert","lines":["e"]}],[{"start":{"row":20,"column":19},"end":{"row":20,"column":20},"action":"remove","lines":["e"],"id":231},{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"remove","lines":["c"]},{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"remove","lines":["r"]},{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"remove","lines":["u"]},{"start":{"row":20,"column":15},"end":{"row":20,"column":16},"action":"remove","lines":["o"]}],[{"start":{"row":20,"column":15},"end":{"row":20,"column":16},"action":"insert","lines":["r"],"id":232},{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"insert","lines":["x"]}],[{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"remove","lines":["x"],"id":233}],[{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"insert","lines":["c"],"id":234}],[{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"insert","lines":[" "],"id":235},{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"insert","lines":["="]}],[{"start":{"row":20,"column":19},"end":{"row":20,"column":20},"action":"insert","lines":[" "],"id":236},{"start":{"row":20,"column":20},"end":{"row":20,"column":21},"action":"insert","lines":["p"]},{"start":{"row":20,"column":21},"end":{"row":20,"column":22},"action":"insert","lines":["h"]}],[{"start":{"row":20,"column":22},"end":{"row":20,"column":23},"action":"insert","lines":["o"],"id":237},{"start":{"row":20,"column":23},"end":{"row":20,"column":24},"action":"insert","lines":["t"]},{"start":{"row":20,"column":24},"end":{"row":20,"column":25},"action":"insert","lines":["o"]}],[{"start":{"row":17,"column":76},"end":{"row":17,"column":77},"action":"remove","lines":[")"],"id":238}],[{"start":{"row":28,"column":0},"end":{"row":35,"column":0},"action":"remove","lines":["","def index(): ","    r = random.randint(1, 100)","    return flask.render_template(","        \"index.html\", ","        random_num=r # Google search ‘python kwaargs’","    )",""],"id":239},{"start":{"row":28,"column":0},"end":{"row":28,"column":1},"action":"insert","lines":["]"]}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":1},"action":"remove","lines":["]"],"id":240}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":21},"action":"remove","lines":["","app = Flask(__name__)"],"id":241},{"start":{"row":5,"column":0},"end":{"row":9,"column":0},"action":"insert","lines":["import flask","import os","","app = flask.Flask(__name__)",""]}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":23},"action":"remove","lines":["from flask import Flask"],"id":242},{"start":{"row":0,"column":8},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"remove","lines":["s"],"id":243},{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"remove","lines":["o"]},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"remove","lines":[" "]},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"remove","lines":[","]}],[{"start":{"row":2,"column":48},"end":{"row":3,"column":0},"action":"remove","lines":["",""],"id":244}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":247},{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"insert","lines":["",""]},{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":10,"column":0},"end":{"row":16,"column":1},"action":"insert","lines":["api_token = '3yEHJrYc03grMh7SUZsRlZKDlQv-3NK0EyJ3iZQquV69HlpaCU9p28OoUejFOLu5'","","url = \"https://api.genius.com/search?q=Outkast\"","","my_headers = {","    \"Authorization\": \"Bearer qiICws1IclXFRZmTwrTJI7k4m8vWoOwy2smTaAmQ2RuyiWztfrPPijT9ea2i2nA-\"","}"],"id":248}],[{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"remove","lines":["",""],"id":249}],[{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"remove","lines":["f"],"id":250}],[{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["F"],"id":251}],[{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"remove","lines":["F"],"id":252}],[{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["f"],"id":253}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":1},"action":"insert","lines":["#"],"id":255}]]},"ace":{"folds":[],"scrolltop":295.5,"scrollleft":0,"selection":{"start":{"row":34,"column":1},"end":{"row":34,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":17,"state":"start","mode":"ace/mode/python"}},"timestamp":1567563570723,"hash":"2596741987d6eca45f3a2b0b9b5d29836f8add23"}