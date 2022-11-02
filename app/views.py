from flask import Blueprint, render_template, request, flash
from funcs.fetchPuuid import fetch_puuid
from funcs.fetchLast20Matches import fetch_last_20_matches

views = Blueprint('views', __name__)

@views.route('/', methods=["GET"])
def load_page():
    return render_template("index.html")

@views.route('/', methods=["POST"])
def search():
    if request.method == 'POST':
        summoner_name = request.form.get("summonerName")
        region = request.form.get("region")
        puuid = fetch_puuid(region,summoner_name)
        last_20_matches = fetch_last_20_matches(region,puuid)
        print(last_20_matches)
    return render_template("index.html")
