# This is a test of the stapi.com's Star Trek API.
# This will be the basis for much cooler stuff. 

# import the requests module. This will be used to request data from the Star Trek API Service

import requests

# pprint module imported to print out json data in an organized way.

import pprint

# Make the call the Star Trek API Service

r = requests.post('http://stapi.co/api/v1/rest/season/search')

# For fun, I want to just check the status code of the request. I'll add more logic here
# to determine whether the service goes down and quits. Just in case STAPI is shutdown. 

status_code = r.status_code
print(status_code)

# Here's the info. It's raw, 

# Put the JSON data into a variable
startrek_shows_json = r.json()

# Instantiate the Pretty Print Object
pp = pprint.PrettyPrinter(indent=4)

# Let's print out the s
pp.pprint(startrek_shows_json)

# Okay, let's query the starships

# Get the starships
startrek_starships = requests.post('http://stapi.co/api/v1/rest/spacecraftClass/search')

# Get the status code, again just to check to see if the request worked, or if the STAPI site is down. More logic will be placed here later. This script is just a test.
startrek_starships_status_cdoe = startrek_starships.status_code

# For kicks, and I like organizing things into specific variables, you can call the json method directly form the object, but this is just my style.
startrek_starships_json = startrek_starships.json()

# Print the starthips from the search
pp.pprint(startrek_starships_json)

# Need to add an example of an individual query of a specific category.
