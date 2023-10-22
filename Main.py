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
    PKF, SKF = get_killstreak_fabs()
except requests.HTTPError as e:
    print(f"Failed to generate due to HTML error: {e}")
# Compare the values and generate a cool looking list highlighting the best ones

## Read file of names
f = open("weaponlist.txt", "r")
weapon_list = []
for i in range(160):
    weapon_list.append(f.readline().strip())
f.close()

## Create file with current date and time
# filename = time.strftime('%m-%d-%y_%H:%M:%S')
# f = open(filename, "a")

# Get values
for weapon_name in weapon_list:
    diff = find_price_difference(SKF, SKK, weapon_name)
    print(f"{weapon_name}: {diff}")

# Save results to a file for later reference (maybe create a cool history?)

# TODO: Add a popularity feature for # of sold items within past week