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

# TODO: SET UP THE NEW PI NAMES
# TODO: LOOK UP WHETHER LOOP HOSTNAMES AND DOING THINGS THAT WAY MAKES MORE SENSE
# TODO: AUTOMATICALLY SET UP CRONJOB SO THIS SCRIPT RUNS
# TODO: ADD TO SCRIPT TO ACTUALLY RESTART THE PI'S EACH DAY AT X TIME, LESS CONFIG ON PI IS BETTER

# define all the clients and the commands to rsync to them
exportpiCanteenWEST = ["rsync", "-a", "/var/www/", "pi@piCanteenWEST:/var/www/", "--delete"]
exportpiLester = ["rsync", "-a", "/var/www/", "pi@piLester:/var/www/", "--delete"]
exportpiSixthform = ["rsync", "-a", "/var/www/", "pi@piSixthform:/var/www/", "--delete"]
exportpiMusic = ["rsync", "-a", "/var/www/", "pi@piMusic:/var/www/", "--delete"]
exportpiSixthform = ["rsync", "-a", "/var/www/", "pi@piSixthform:/var/www/", "--delete"]
exportpiMusic = ["rsync", "-a", "/var/www/", "pi@piMusic:/var/www/", "--delete"]
exportpiMusic = ["rsync", "-a", "/var/www/", "pi@piMusic:/var/www/", "--delete"]

restartpiCanteenWEST = ["ssh", "pi@piCanteenWEST", "sudo", "shutdown", "-r", "now"]
restartpiLester = ["ssh", "pi@piLester", "sudo", "shutdown", "-r", "now"]
restartpiSixthform = ["ssh", "pi@piSixthform", "sudo", "shutdown", "-r", "now"]
restartpiMusic = ["ssh", "pi@piMusic", "sudo", "shutdown", "-r", "now"]
restartpiSixthform = ["ssh", "pi@piSixthform", "sudo", "shutdown", "-r", "now"]
restartpiMusic = ["ssh", "pi@piMusic", "sudo", "shutdown", "-r", "now"]
restartpiMusic = ["ssh", "pi@piMusic", "sudo", "shutdown", "-r", "now"]

# using apt-get instead of apt as apt's cli is not stable yet
upgradepiCanteenWEST = ["ssh", "pi@piCanteenWEST", "sudo", "apt-get", "update", "&&", "sudo", "apt-get", "upgrade", "-y"]
upgradepiLester = ["ssh", "pi@piLester", "sudo", "apt-get", "update", "&&", "sudo", "apt-get", "upgrade", "-y"]
upgradepiSixthform = ["ssh", "pi@piSixthform", "sudo", "apt-get", "update", "&&", "sudo", "apt-get", "upgrade", "-y"]
upgradepiMusic = ["ssh", "pi@piMusic", "sudo", "apt-get", "update", "&&", "sudo", "apt-get", "upgrade", "-y"]
upgradepiSixthform = ["ssh", "pi@piSixthform", "sudo", "apt-get", "update", "&&", "sudo", "apt-get", "upgrade", "-y"]
upgradepiMusic = ["ssh", "pi@piMusic", "sudo", "apt-get", "update", "&&", "sudo", "apt-get", "upgrade", "-y"]
upgradepiMusic = ["ssh", "pi@piMusic", "sudo", "apt-get", "update", "&&", "sudo", "apt-get", "upgrade", "-y"]

# if userInput is all, rsync to every pi. have 5 sec's inbetween as a breather for network
# add time for logging
if clientsAffected == ("all") and userCommand == ("export"):
        subprocess.call(exportpiCanteenWEST)
        print("exported to piCanteenWEST at "+time.strftime("%H:%M:%S"))
        time.sleep(5)
        subprocess.call(exportpiLester)
        print("exported to piLester at "+time.strftime("%H:%M:%S"))
        time.sleep(5)
        subprocess.call(exportpiSixthform)
        print("exported to piSixthform at "+time.strftime("%H:%M:%S"))
        time.sleep(5)
        subprocess.call(exportpiMusic)
        print("exported to piMusic at "+time.strftime("%H:%M:%S"))

# export to nly one pi
# add time for logging
elif clientsAffected == ("piCanteenWEST") and userCommand == ("export"):
        subprocess.call(exportpiCanteenWEST)
        print("exported to piCanteenWEST "+time.strftime("%H:%M:%S"))
# export to only one pi
# add time for logging
elif clientsAffected == ("piLester") and userCommand == ("export"):
        subprocess.call(exportpiLester)
        print("exported to piLester "+time.strftime("%H:%M:%S"))
# export to only one pi
# add time for logging
elif clientsAffected == ("piSixthform") and userCommand == ("export"):
        subprocess.call(exportpiSixthform)
        print("exported to piSixthform "+time.strftime("%H:%M:%S"))
# export to only one pi
# add time for logging
elif clientsAffected == ("piMusic") and userCommand == ("export"):
        subprocess.call(exportpiMusic)
        print("exported to piMusic "+time.strftime("%H:%M:%S"))

# restart all the clients
# add time for logging
elif clientsAffected == ("all") and userCommand == ("restart"):
        subprocess.call(restartpiCanteenWEST)
        print("restarted piCanteenWEST at "+time.strftime("%H:%M:%S"))
        subprocess.call(restartpiLester)
        print("restarted piLester at "+time.strftime("%H:%M:%S"))
        subprocess.call(restartpiSixthform)
        print("restarted piSixthform at "+time.strftime("%H:%M:%S"))
        subprocess.call(restartpiMusic)
        print("restarted piMusic at "+time.strftime("%H:%M:%S"))

# restart only one pi
# add time for logging
elif clientsAffected == ("piCanteenWEST") and userCommand == ("restart"):
        subprocess.call(restartpiCanteenWEST)
        print("restarted piCanteenWEST "+time.strftime("%H:%M:%S"))
# restart only one pi
# add time for logging
elif clientsAffected == ("piLester") and userCommand == ("restart"):
        subprocess.call(restartpiLester)
        print("restarted piLester "+time.strftime("%H:%M:%S"))
# restart only one pi
# add time for logging
elif clientsAffected == ("piSixthform") and userCommand == ("restart"):
        subprocess.call(restartpiSixthform)
        print("restarted piSixthform "+time.strftime("%H:%M:%S"))
# restart only one pi
# add time for logging
elif clientsAffected == ("piMusic") and userCommand == ("restart"):
        subprocess.call(restartpiMusic)
        print("restarted piMusic "+time.strftime("%H:%M:%S"))

# upgrade all the clients
# add time for logging
elif clientsAffected == ("all") and userCommand == ("upgrade"):
        print("This process can take a very long time, please be patient")
        subprocess.call(upgradepiCanteenWEST)
        print("upgraded piCanteenWEST at "+time.strftime("%H:%M:%S"))
        subprocess.call(upgradepiLester)
        print("upgraded piLester at "+time.strftime("%H:%M:%S"))
        subprocess.call(upgradepiSixthform)
        print("upgraded piSixthform at "+time.strftime("%H:%M:%S"))
        subprocess.call(upgradepiMusic)
        print("upgraded piMusic at "+time.strftime("%H:%M:%S"))

# upgrade only one pi
# add time for logging
elif clientsAffected == ("piCanteenWEST") and userCommand == ("upgrade"):
        print("This process can take a very long time, please be patient")
        subprocess.call(upgradepiCanteenWEST)
        print("upgraded piCanteenWEST "+time.strftime("%H:%M:%S"))
# upgrade only one pi
# add time for logging
elif clientsAffected == ("piLester") and userCommand == ("upgrade"):
        print("This process can take a very long time, please be patient")
        subprocess.call(upgradepiLester)
        print("upgraded piLester "+time.strftime("%H:%M:%S"))
# upgrade only one pi
# add time for logging
elif clientsAffected == ("piSixthform") and userCommand == ("upgrade"):
        print("This process can take a very long time, please be patient")
        subprocess.call(upgradepiSixthform)
        print("upgraded piSixthform "+time.strftime("%H:%M:%S"))
# upgrade only one pi
# add time for logging
elif clientsAffected == ("piMusic") and userCommand == ("upgrade"):
        print("This process can take a very long time, please be patient")
        subprocess.call(upgradepiMusic)
        print("upgraded piMusic "+time.strftime("%H:%M:%S"))

else:
        print ("Sorry, "+ userCommand + " " + clientsAffected +" is not recognised")
