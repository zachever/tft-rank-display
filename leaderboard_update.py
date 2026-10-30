from lcu_manager import get, post 

leaderboard_endpoint = "/lol-ranked/v1/apex-leagues/RANKED_TFT/MASTER"
result = get(leaderboard_endpoint)

leaderboard = result["divisions"]
puuids = [player["puuid"] for division in leaderboard for player in division["standings"]]
puuids = puuids[:200]
print(puuids)

username_endpoint = "/lol-summoner/v1/summoner-aliases-by-puuids"
username_result = post(username_endpoint, body=puuids)
print(username_result)
