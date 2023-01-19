from flask import Flask, request
from flask_cors import CORS
from riotwatcher import TftWatcher

# Import functions
from funcs.generateSummonerData import generate_summoner_data

# Initialize
riotAPIKey = "RGAPI-0216644f-0c34-4ffd-8eeb-977f873453d2"
watcher = TftWatcher(riotAPIKey)
app = Flask(__name__)
CORS(app)

# Asset paths
json_url = "https://raw.communitydragon.org/latest/cdragon/tft/en_gb.json"
path_url = "https://raw.communitydragon.org/latest/game/"


@app.route('/', methods=["GET","POST"])
def start_api():
    if request.method == "GET":
        return {"status":{"message":"Forbidden","status_code":403}}
    elif request.method == "POST":
        try:
            summoner_name = request.json["summonerName"]
            region = request.json["region"]
            summoner_data = generate_summoner_data(summoner_name, region, riotAPIKey, json_url, path_url)
            return summoner_data
        except Exception as error:
            print(error)
            return error
        
if __name__ == "__main__":
    app.run()
    
