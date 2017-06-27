# Thorium Poke Script
# Daniel Pullan (https://danielpullan.co.uk)

# To check if devices have gone down. If they have, send an alert.

import requests
import socket

piCanteenWEST = "nada"
piLester = "nada"
piSixthform = "nada"
piMusic = "nada"
piReception = "nada"
piArt = "nada"
piTheatre = "nada"
piCanteenEAST = "nada"
piTesting = "nada"

pi = [piCanteenWEST, piLester, piSixthform, piMusic, piReception, piArt, piTheatre, piCanteenEAST, piTesting]

for pi in pi:
    try:
        r = requests.get('http://' + pi)
        s = socket.gethostbyaddr(pi)
        print(*s, r.status_code)
    except requests.exceptions.RequestException as e:
        print(pi + " is down")
        pass
