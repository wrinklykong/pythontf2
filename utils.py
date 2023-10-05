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
    # DEBUG
    # print(results[4]['name'])
    # print(re.search(r"Professional Killstreak.*Fabricator Kit", results[0]['name']))
    # TODO: Functional split of results into two lists
    # SKF = [ result for result in results if re.search(result['name'], r"Professional Killstreak.*Fabricator Kit") ]
    # print(len(SKF))


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
