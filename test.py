import requests
import os
from dotenv import load_dotenv

load_dotenv()

RIOT_ID = "TeZZy"
TAG = "TeZZy"

def get_request(url):
    headers = {
        "X-Riot-Token": os.getenv("API_KEY")
    }
    return requests.get(url, headers=headers).json()

def get_puuid(riot_id, tag):
    url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{riot_id}/{tag}"
    return get_request(url)["puuid"]

puuid = get_puuid(RIOT_ID, TAG)
print(puuid)
def get_tier_rank_lp(puuid):
    url = "https://oc1.api.riotgames.com/tft/league/v1/by-puuid/" + puuid
    rank_info = get_request(url)
    tier = rank_info[0]["tier"]
    rank = rank_info[0]["rank"]
    lp = rank_info[0]["leaguePoints"]
    return {"tier": tier, "rank": rank, "lp": lp}

rank_info = get_tier_rank_lp(puuid)
print(rank_info)