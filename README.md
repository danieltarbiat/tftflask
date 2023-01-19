# TeamFlaskTactics

## This is an API for the game Teamfight Tactics.

This project was built with the help of Riots API keys.
* Fetches the latest 20 matches data from the Riot API key when receiving a post request with the desired summoner name and region.
* Sorts through the data and returns the most played traits, augments, units and items that the summoner has played in the latest 20 matches.
* Also adds links to images for every trait, augment, unit and item.


## How to install the project
1. First you need to install the dependencies
```
pip install flask        
pip install -U flask-cors
pip install riotwatcher  
```
2. Run the main.py file
3. Make a post request to the API with the body:
```
{
    "region":"Region here",
    "summonerName":"Summoner name here"
}
```
4. Then you're done and can decide how to represent the data.
