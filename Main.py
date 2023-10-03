import requests
import json

from utils import get_prof_killstreak_kits

SKK = []
PKK = []
KK = []

SKF = []
PKF = []
KF = []


DEFAULT_PARAMS = {
    "query": "",
    "start": 0,
    "count": 100,  # Max # of API results
    "appid": 440,  # Hard-coded TF2 appid
    "norender": 1,
    "sort_dir": "asc"  # Forces the results to be ordered
}

BASEURL = "https://steamcommunity.com/market/appfilters/200"
url = "https://steamcommunity.com/market/search/render/search?q=&category_440_Collection%5B%5D=any&category_440_Type%5B%5D=tag_TF_KillStreakifierToolC&category_440_Quality%5B%5D=tag_Unique&appid=440&norender=1&count=100&sort_column=name&sort_dir=asc";
Fabs = url = "https://steamcommunity.com/market/search/render/search?q=professional+killstreak+kit+fabricator&category_440_Collection%5B0%5D=any&category_440_Type%5B0%5D=tag_TF_ItemDynamicRecipeTool&appid=440&norender=1&count=100&sort_column=name&sort_dir=asc&start=";

data = get_prof_killstreak_kits()
print(len(data))
for a in data:
    print(a['name'])

# OOP

# TODO: Generate a "cost" of generating the kit (using current value of materials from backpack.tf?)

# Grab Kits
## Grab Specialized Killstreak Kits
## Grab Professional Killstreak Kits

# Grab Kit Fabs
## Grab Specialized Killstreak Fabricators
## Grab Professional Killstreak Kits

# Compare the values and generate a cool looking list highlighting the best ones

# Save results to a file for later reference (maybe create a cool history?)

# TODO: Add a popularity feature for # of sold items within past week