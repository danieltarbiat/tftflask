# TeamFlaskTactics

## This is an API for the game Teamfight Tactics.

This project was built with the help of Riots API keys.
* Fetches the latest 20 matches data from the Riot API key when receiving a post request with the desired summoner name and region.
* Sorts through the data and returns the most played traits, augments, units and items that the summoner has played in the latest 20 matches.
* Also adds links to images for every trait, augment, unit and item.

```diff
- This project was made during the set 7.5, but still works as of set 8.0. Though this might change in the future.
```



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


An example of the recieved data from the API:

For augments,
```
        "TFT6_Augment_BandOfThieves2": {
            "augmentImage": "https://raw.communitydragon.org/latest/game/assets/maps/tft/icons/augments/choiceui/bandthieves3.png",
            "augmentName": "TFT6_Augment_BandOfThieves2",
            "averagePlacement": "#2.0",
            "playrate": "1.7%",
            "timesPlayed": 1
        }
 ```
 For traits,
 ```
         "Set8_Ace": {
            "averagePlacement": "#5",
            "timesPlayed": 17,
            "traitImage": "https://raw.communitydragon.org/latest/game/assets/ux/traiticons/trait_icon_8_forecaster.png",
            "traitName": "Set8_Ace",
            "traitStyles": {
                "Bronze": 0,
                "Gold": 0,
                "Platinum": 7,
                "Silver": 10
            }
 ```
 For units and items,
  ```
  "TFT8_Alistar": {
            "averagePlacement": "#4.9",
            "playrate": "6.5%",
            "timesPlayed": 12,
            "unitImage": "https://raw.communitydragon.org/latest/game/assets/ux/tft/championsplashes/tft8_alistar.tft_set8.png",
            "unitItems": {
                "TFT8_Item_InterPolarisEmblemItem": {
                    "https://raw.communitydragon.org/latest/game/assets/maps/particles/tft/item_icons/traits/spatula/set8/lasercorps.tft_set8.png": 1
                },
                "TFT_Item_BrambleVest": {
                    "https://raw.communitydragon.org/latest/game/assets/maps/particles/tft/item_icons/standard/bramble_vest.png": 1
                },
                "TFT_Item_DragonsClaw": {
                    "https://raw.communitydragon.org/latest/game/assets/maps/particles/tft/item_icons/standard/dragons_claw.png": 3
                },
                "TFT_Item_FrozenHeart": {
                    "https://raw.communitydragon.org/latest/game/assets/maps/particles/tft/item_icons/standard/winters_approach.png": 2
                },
                "TFT_Item_GiantsBelt": {
                    "https://raw.communitydragon.org/latest/game/assets/maps/particles/tft/item_icons/standard/gaints_belt.png": 1
                },
                "TFT_Item_RabadonsDeathcap": {
                    "https://raw.communitydragon.org/latest/game/assets/maps/particles/tft/item_icons/standard/rabadons_deathcap.png": 1
                },
                "TFT_Item_RedBuff": {
                    "https://raw.communitydragon.org/latest/game/assets/maps/particles/tft/item_icons/standard/sunfire_cape.png": 1
                },
                "TFT_Item_SparringGloves": {
                    "https://raw.communitydragon.org/latest/game/assets/maps/particles/tft/item_icons/standard/sparring_gloves.png": 1
                },
                "TFT_Item_TitansResolve": {
                    "https://raw.communitydragon.org/latest/game/assets/maps/particles/tft/item_icons/standard/titans_resolve.png": 1
                },
                "TFT_Item_WarmogsArmor": {
                    "https://raw.communitydragon.org/latest/game/assets/maps/particles/tft/item_icons/standard/warmogs_armor.png": 2
                }
            },
            "unitName": "TFT8_Alistar"
        }
 ```
