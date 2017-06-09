# Thorium Device Management Script
# Daniel Pullan (https://danielpullan.co.uk)
# Find out more about this script at https://danielpullan.co.uk/?thorium-device-management-script
# Instructions on how to use this script are found at https://github.com/DanielPullan/Thorium/wiki/How-to-use-manage.py

# import stuff, can't remember if OS is needed but time and subprocess definately is
import time
import subprocess
import sys

# ask the user what they want to sync to, save as a variable
userCommand = sys.argv[1]
clientsAffected = sys.argv[2]

#subprocess.call(exportpiCanteenWEST)
#exportpiSixthform = ["rsync", "-a", "/var/www/", "pi@piSixthform:/var/www/", "--delete"]
#exportpiMusic = ["rsync", "-a", "/var/www/", "pi@piMusic:/var/www/", "--delete"]

# TODO: SET UP THE NEW PI NAMES
# TODO: LOOK UP WHETHER LOOP HOSTNAMES AND DOING THINGS THAT WAY MAKES MORE SENSE
# TODO: AUTOMATICALLY SET UP CRONJOB SO THIS SCRIPT RUNS
# TODO: ADD TO SCRIPT TO ACTUALLY RESTART THE PI'S EACH DAY AT X TIME, LESS CONFIG ON PI IS BETTER

pi = ['piCanteenWest', 'piLester', 'piSixthForm, piMusic', 'piReception', 'piArt', 'piTheatre']

if userCommand:
    for x in pi:
        subproccess.call(["rsync", "-a", "/var/www/", "pi@", x, ":/var/www/", "--delete"])