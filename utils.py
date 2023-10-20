import requests
import json
import re


DEFAULT_PARAMS = {
    "query": "",
    "start": 0,
    "count": 100,  # Max # of API results
    "appid": 440,  # Hard-coded TF2 appid
    "norender": 1,
    "sort_dir": "asc"  # Forces the results to be ordered
}


def get_spec_killstreak_kits():
    """
    Function which returns dictionary of specialized killstreak kits
    """
    params = {
        "query": "",
        "start": 0,
        "sort_dir": "asc",  # Forces the results to be ordered
        "count": 100,  # Max # of API results
        "appid": 440,  # Hard-coded TF2 appid
        "category_440_Collection[]": "any",
        "category_440_Type[]": "tag_TF_KillStreakifierToolB",
        "category_440_Quality[]": "tag_Unique",
        "norender": 1,
    }
    return grab_all(params)


def get_prof_killstreak_kits():
    """
    Returns dictionary results of professional killstreak kits
    """
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
    return grab_all(params)

def get_killstreak_fabs():
    """
    Returns a tuple of dictionary results of killstreak kits
    """
    params = {
        "query": "Killstreak Kit Fabricator",
        "start": 0,
        "sort_dir": "asc",  # Forces the results to be ordered
        "count": 100,  # Max # of API results
        "appid": 440,  # Hard-coded TF2 appid
        "category_440_Collection[]": "any",
        "category_440_Quality[]": "tag_Unique",
        "norender": 1,
    }
    results = grab_all(params)
    PKF = [ result for result in results if re.search(r"^Professional Killstreak.*Kit Fabricator", result['name']) ]
    SKF = [ result for result in results if re.search(r"^Specialized Killstreak.*Kit Fabricator", result['name']) ]
    return (PKF, SKF)

def grab_all(params):
    allres = []
    page = 0

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
    r.raise_for_status()
    return r

def make_call_with_options(parameters):
    # Parameter object function call
    r = requests.get("https://steamcommunity.com/market/search/render", params=parameters)
    r.raise_for_status()
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

def find_price_difference(fab_list, kit_list, kit_name):
    """
    :param list fab_list: List of kit fabricators
    :param list kit_list: List of kits
    :param String kit_name: Kit name
    """
    if 'Fabricator' in kit_name:
        kit_name = kit_name[:-11]
    print(kit_name)
    kit = None
    fab = None
    for f in fab_list:
        if kit_name in f['name']:
            fab = f
    for k in kit_list:
        if kit_name in k['name']:
            kit = k
    print(kit)
    print(fab)
    if kit is None or fab is None:
        raise Exception("Failed to find values")
    # Sell price listed in cents, convert to dollar amount
    diff = kit['sell_price'] - fab['sell_price'] / 100
    print(diff)
