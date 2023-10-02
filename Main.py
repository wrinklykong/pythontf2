import requests
import json

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

def make_call(query="", page=0):
    r = requests.get("https://steamcommunity.com/market/search/render",
        params = {
            "query": query,
            "start": page*100,
            "count": 100,  # Max # of API results
            "appid": 440,  # Hard-coded TF2 appid
            "category_440_Collection[]": "any",
            # "category_440_Type[]": "tag_TF_KillStreakifierToolC",
            "norender": 1,
            "sort_dir": "asc"  # Forces the results to be ordered
        })
    return r

def make_call(parameters):
    # Parameter object function call
    r = requests.get("https://steamcommunity.com/market/search/render", params=parameters)

def load_results_into_dict(dict, params):
    while True:
        r = make_call(params)
        if len(r["results"]) < 100:
            # Break out
            pass
        for a in r["results"]:
            # Load in the data to the dictionaries
            dict.append("something idk")  # key, value
    pass

data = json.loads(make_call().text)["results"]
for a in data:
    print(a)

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