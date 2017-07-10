# Thorium Poke Script
# Daniel Pullan (https://danielpullan.co.uk)

import requests

# Make pi name equal to it's IP
piCanteenWEST = "nada"
piCanteenEAST = "nada"
piMusic = "nada"
piArt = "nada"
piLester = "nada"
piSixthform = "nada"
piReception = "nada"
piTheatre = "nada"
piTesting = "nada"

# make an array/list of all the pies
pi = [piCanteenWEST, piLester, piSixthform, piMusic, piReception, piArt, piTheatre, piCanteenEAST, piTesting]

piUp = 0
numberOfPis = len(pi)

# for every pi in the pi array
for pi in pi:
    try:
        r = requests.get('http://' + pi)
        piUp = piUp + 1
        print(piUp, "out of", numberOfPis, "are online")
    except requests.exceptions.RequestException as e:
        print(pi + " is down")
        print(piUp, "out of", numberOfPis, "are online")
        pass
