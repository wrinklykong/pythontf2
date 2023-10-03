import requests
import json

def get_spec_killstreak_kits():
    """
    Function which returns dictionary of specialized killstreak kits
    """
    # https://steamcommunity.com/market/search?q=&category_440_Collection%5B%5D=any&category_440_Type%5B%5D=tag_TF_KillStreakifierToolB&appid=440
    pass

def get_prof_killstreak_kits():
    """
    Returns dictionary results of professional killstreak kits
    """
    page = 0
    params = {
        "query": "",
        "start": 0,
        "sort_dir": "asc",  # Forces the results to be ordered
        "count": 100,  # Max # of API results
        "appid": 440,  # Hard-coded TF2 appid
        "category_440_Collection[]": "any",
        "category_440_Type[]": "tag_TF_KillStreakifierToolC",
        "category_440_Quality[]": "tag_Unique",
        "norender": 1,
    }
    allres = []

    while True:
        data = make_call_with_options(parameters=params)
        params['start'] = params['start']+100
        allres = allres + data['results']
        if len(data['results']) < 100:
            break
    return allres

def make_call(query="", page=0):
    r = requests.get("https://steamcommunity.com/market/search/render",
        params = {
            "query": query,
            "start": page*100,
            "sort_dir": "asc",  # Forces the results to be ordered
            "count": 100,  # Max # of API results
            "appid": 440,  # Hard-coded TF2 appid
            "category_440_Collection[]": "any",
            "category_440_Type[]": "tag_TF_KillStreakifierToolC",
            "category_440_Quality[]": "tag_Unique",
            "norender": 1,
        })
    return r

def make_call_with_options(parameters):
    # Parameter object function call
    r = requests.get("https://steamcommunity.com/market/search/render", params=parameters)
    return json.loads(r.text)

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
