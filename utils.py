import requests
import json
import re
import time


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
    time_sleep = 4
    while True:
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
        result_text = json.loads(r.text)
        if 'results' in result_text and len(result_text['results']) > 0:
            break
        time.sleep(time_sleep)
        time_sleep=time_sleep*2

    r.raise_for_status()
    return r

def make_call_with_options(parameters):
    # Parameter object function call
    time_sleep = 4
    while True:
        print("request2")
        r = requests.get("https://steamcommunity.com/market/search/render", params=parameters)
        result_text = json.loads(r.text)
        if 'results' in result_text and len(result_text['results']) > 0:
            break
        time.sleep(time_sleep)
        time_sleep=time_sleep*2

    r.raise_for_status()
    return result_text

def find_price_difference(fab_list, kit_list, weapon_name, specialized=True):
    """
    :param list fab_list: List of kit fabricators
    :param list kit_list: List of kits
    :param String weapon_name: Kit name
    """
    kit_type = "Specialized" if specialized else "Professional"
    search = f"{kit_type} Killstreak {weapon_name} Kit" if weapon_name else f"{kit_type} Killstreak Kit"

    # Attempt to grab values, raise exception if not found
    try:
        fab = [f for f in fab_list if f['name'] == f"{search} Fabricator"][0]
        kit = [k for k in kit_list if k['name'] == search][0]
    except IndexError as e:
        print(f"Failed to find values for Weapon: '{weapon_name}'")
        return
    # Sell price listed in cents, convert to dollar amount
    diff = (kit['sell_price'] - fab['sell_price']) / 100
    return diff
