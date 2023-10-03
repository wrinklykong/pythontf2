import requests
import json

from utils import get_prof_killstreak_kits, get_spec_killstreak_kits

SKK = []
PKK = []
KK = []

SKF = []
PKF = []
KF = []

# OOP

# TODO: Generate a "cost" of generating the kit (using current value of materials from backpack.tf?)

# Grab Kits
## Grab Specialized Killstreak Kits
SKK = get_spec_killstreak_kits()
print(len(SKK))
## Grab Professional Killstreak Kits
PKK = get_prof_killstreak_kits()
print(len(PKK))

# Grab Kit Fabs
## Grab Specialized Killstreak Fabricators
## Grab Professional Killstreak Kits

# Compare the values and generate a cool looking list highlighting the best ones

# Save results to a file for later reference (maybe create a cool history?)

# TODO: Add a popularity feature for # of sold items within past week