import requests
import json

from utils import get_prof_killstreak_kits, get_spec_killstreak_kits, get_killstreak_fabs, \
    find_price_difference

SKK = []
PKK = []

SKF = []
PKF = []

# OOP

# TODO: Generate a "cost" of generating the kit (using current value of materials from backpack.tf?)
try:
    # Grab Kits
    ## Grab Specialized Killstreak Kits
    SKK = get_spec_killstreak_kits()
    ## Grab Professional Killstreak Kits
    PKK = get_prof_killstreak_kits()

    # Grab Kit Fabs
    ## Grab Specialized Killstreak Fabricators
    ## Grab Professional Killstreak Fabricator
    SKF, PKF = get_killstreak_fabs()
except requests.HTTPError as e:
    print(f"Failed to generate due to HTML error: {e}")
# Compare the values and generate a cool looking list highlighting the best ones

print(SKF[0]['name'])
diff = find_price_difference(SKF, SKK, SKF[0]['name'])
print(diff)

# Save results to a file for later reference (maybe create a cool history?)

# TODO: Add a popularity feature for # of sold items within past week