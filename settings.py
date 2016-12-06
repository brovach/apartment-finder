import os

## Price

# The minimum rent you want to pay per month.
MIN_PRICE = 4000

# The maximum rent you want to pay per month.
MAX_PRICE = 6400

## Location preferences

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'sfbay'

# What Craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
AREAS = ["sfc"]

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {
    "marina": [
        [37.798984, -122.447573],
        [37.807258, -122.424452],
    ],
    "north_beach": [
        [37.796712, -122.412221],
        [37.808682, -122.399905],
    ],
    "anza_vista": [
        [37.778568, -122.447863],
        [37.782977, -122.439001],
    ],
    "laurel_heights": [
        [37.781892, -122.460759],
        [37.786301, -122.445652],dsa
    ],
    "cow_hollow": [
        [37.792848, -122.447573],
        [37.800576, -122.423594],
    ],
    "pac_heights": [
        [37.79124, -122.42381],
        [37.79850, -122.44784],
    ],
    "lower_pac_heights": [
        [37.78554, -122.42878],
        [37.78873, -122.44544],
    ],
    "russian_hill": [
        [37.796882, -122.422864],
        [37.808682, -122.411449],
    ],
    "nob_hill": [
        [37.787539, -122.424495],
        [37.797204, -122.40999],
    ],
    "lower_height": [
        [37.768255, -122.440953],
        [37.775701, -122.419281],
    ],
    "haight": [
        [37.766194, -122.453796],
        [37.773641, -122.436383],
    ],
    "richmond": [
        [37.77188, -122.47263],
        [37.78029, -122.51005],
    ],
    "presidio": [
        [37.78586, -122.466509],
        [37.791998, -122.445481],
    ],
    "mission": [
        [37.755499, -122.425429],
        [37.768917, -122.408799],
    ],
    "japantown": [
        [37.781756, -122.434924],
        [37.790303, -122.402737],
    ],
    "western_addition": [
        [37.774701, -122.437756],
        [37.784198, -122.416642],
    ],
    "north_of_panhandle": [
        [37.772869, -122.465265],
        [37.782536, -122.433937],
    ],
     "duboce_triangle": [
        [37.760792, -122.435868],
        [37.76795, -122.425826],
    ]
}

# A list of neighborhood names to look for in the Craigslist neighborhood name field. If a listing doesn't fall into
# one of the boxes you defined, it will be checked to see if the neighborhood name it was listed under matches one
# of these.  This is less accurate than the boxes, because it relies on the owner to set the right neighborhood,
# but it also catches listings that don't have coordinates (many listings are missing this info).
NEIGHBORHOODS = ["marina", "north beach", "anza vista", "laurel heights", "lone mountain", "cow hollow", "pac hts", "pacific heights", "lower pac heights", "lower pacific heights", "russian hill", "nob hill", "lower haight", "presidio", "presidio heights", "haight ashbury", "mission district", "japantown", "japan town", "western addition", "north of panhandle", "nopa", "jordan park", "hayes valley", "duboce"]

## Transit preferences

# The farthest you want to live from a transit stop.
MAX_TRANSIT_DIST = 1 # kilometers

# Transit stations you want to check against.  Every coordinate here will be checked against each listing,
# and the closest station name will be added to the result and posted into Slack.

TRANSIT_STATIONS = {}

## Search type preferences

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
CRAIGSLIST_HOUSING_SECTION = 'apa'

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 20 * 60 # 20 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#chateau-search"

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.

# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass