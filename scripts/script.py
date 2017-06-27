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

# TODO: AUTOMATICALLY SET UP CRONJOB SO THIS SCRIPT RUNS
# TODO: ADD TO SCRIPT TO ACTUALLY RESTART THE PI'S EACH DAY AT X TIME, LESS CONFIG ON PI IS BETTER

piCanteenWEST = "nada"
piLester = "nada"
piSixthform = "nada"
piMusic = "nada"
piReception = "nada"
piArt = "nada"
piTheatre = "nada"
piCanteenEAST = "nada"
piTesting = "nada"

# define all the clients and the commands to rsync to them
exportpiCanteenWEST = ["rsync", "-a", "/var/www/", "pi@" + piCanteenWEST + ":/var/www/", "--delete"]
exportpiLester = ["rsync", "-a", "/var/www/", "pi@" + piLester + ":/var/www/", "--delete"]
exportpiSixthform = ["rsync", "-a", "/var/www/", "pi@" + piSixthform + ":/var/www/", "--delete"]
exportpiMusic = ["rsync", "-a", "/var/www/", "pi@" + piMusic + "/var/www/", "--delete"]
exportpiReception = ["rsync", "-a", "/var/www/", "pi@" + piReception + ":/var/www/", "--delete"]
exportpiArt = ["rsync", "-a", "/var/www/", "pi@" + piArt + ":/var/www/", "--delete"]
exportpiTheatre = ["rsync", "-a", "/var/www/", "pi@" + piTheatre + ":/var/www/", "--delete"]
exportpiCanteenEAST = ["rsync", "-a", "/var/www/", "pi@" + piCanteenEAST + ":/var/www/", "--delete"]
exportpiTesting = ["rsync", "-a", "/var/www/", "pi@" + piTesting + ":/var/www/", "--delete"]

restartpiCanteenWEST = ["ssh", "pi@" + piCanteenWEST, "sudo", "shutdown", "-r", "now"]
restartpiLester = ["ssh", "pi@" + piLester, "sudo", "shutdown", "-r", "now"]
restartpiSixthform = ["ssh", "pi@" + piSixthform, "sudo", "shutdown", "-r", "now"]
restartpiMusic = ["ssh", "pi@" + piMusic, "sudo", "shutdown", "-r", "now"]
restartpiReception = ["ssh", "pi@" + piReception, "sudo", "shutdown", "-r", "now"]
restartpiArt = ["ssh", "pi@" + piArt, "sudo", "shutdown", "-r", "now"]
restartpiTheatre = ["ssh", "pi@" + piTheatre, "sudo", "shutdown", "-r", "now"]
restartpiCanteenEAST = ["ssh", "pi@" + piCanteenEAST, "sudo", "shutdown", "-r", "now"]
restartpiTesting = ["ssh", "pi@" + piTesting, "sudo", "shutdown", "-r", "now"]

# using apt-get instead of apt as apt's cli is not stable yet
upgradepiCanteenWEST = ["ssh", "pi@" + piCanteenWEST, "sudo", "apt-get", "update", "&&", "sudo", "apt-get", "upgrade",
                        "-y"]
upgradepiLester = ["ssh", "pi@" + piLester, "sudo", "apt-get", "update", "&&", "sudo", "apt-get", "upgrade", "-y"]
upgradepiSixthform = ["ssh", "pi@" + piSixthform, "sudo", "apt-get", "update", "&&", "sudo", "apt-get", "upgrade", "-y"]
upgradepiMusic = ["ssh", "pi@" + piMusic, "sudo", "apt-get", "update", "&&", "sudo", "apt-get", "upgrade", "-y"]
upgradepiReception = ["ssh", "pi@" + piReception, "sudo", "apt-get", "update", "&&", "sudo", "apt-get", "upgrade", "-y"]
upgradepiArt = ["ssh", "pi@" + piArt, "sudo", "apt-get", "update", "&&", "sudo", "apt-get", "upgrade", "-y"]
upgradepiTheatre = ["ssh", "pi@" + piTheatre, "sudo", "apt-get", "update", "&&", "sudo", "apt-get", "upgrade", "-y"]
upgradepiCanteenEAST = ["ssh", "pi@" + piCanteenEAST, "sudo", "apt-get", "update", "&&", "sudo", "apt-get", "upgrade",
                        "-y"]
upgradepiTesting = ["ssh", "pi@" + piTesting, "sudo", "apt-get", "update", "&&", "sudo", "apt-get", "upgrade", "-y"]

# Export

if clientsAffected == "all" and userCommand == "export":
    subprocess.call(exportpiCanteenWEST)
    print("exported to piCanteenWEST at " + time.strftime("%H:%M:%S"))
    time.sleep(5)
    subprocess.call(exportpiLester)
    print("exported to piLester at " + time.strftime("%H:%M:%S"))
    time.sleep(5)
    subprocess.call(exportpiSixthform)
    print("exported to piSixthform at " + time.strftime("%H:%M:%S"))
    time.sleep(5)
    subprocess.call(exportpiMusic)
    print("exported to piMusic at " + time.strftime("%H:%M:%S"))
    time.sleep(5)
    subprocess.call(exportpiReception)
    print("exported to piReception at " + time.strftime("%H:%M:%S"))
    time.sleep(5)
    subprocess.call(exportpiArt)
    print("exported to piArt at " + time.strftime("%H:%M:%S"))
    time.sleep(5)
    subprocess.call(exportpiTheatre)
    print("exported to piTheatre at " + time.strftime("%H:%M:%S"))
    time.sleep(5)
    subprocess.call(exportpiCanteenEAST)
    print("exported to piCanteenEAST at " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piCanteenWEST" and userCommand == "export":
    subprocess.call(exportpiCanteenWEST)
    print("exported to piCanteenWEST " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piLester" and userCommand == "export":
    subprocess.call(exportpiLester)
    print("exported to piLester " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piSixthform" and userCommand == "export":
    subprocess.call(exportpiSixthform)
    print("exported to piSixthform " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piMusic" and userCommand == "export":
    subprocess.call(exportpiMusic)
    print("exported to piMusic " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piReception" and userCommand == "export":
    subprocess.call(exportpiReception)
    print("exported to piReception " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piArt" and userCommand == "export":
    subprocess.call(exportpiArt)
    print("exported to piArt " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piTheatre" and userCommand == "export":
    subprocess.call(exportpiTheatre)
    print("exported to piTheatre " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piCanteenEAST" and userCommand == "export":
    subprocess.call(exportpiCanteenEAST)
    print("exported to piCanteenEAST " + time.strftime("%H:%M:%S"))

# Restart

elif clientsAffected == "all" and userCommand == "restart":
    subprocess.call(restartpiCanteenWEST)
    print("restarted piCanteenWEST at " + time.strftime("%H:%M:%S"))
    subprocess.call(restartpiLester)
    print("restarted piLester at " + time.strftime("%H:%M:%S"))
    subprocess.call(restartpiSixthform)
    print("restarted piSixthform at " + time.strftime("%H:%M:%S"))
    subprocess.call(restartpiMusic)
    print("restarted piMusic at " + time.strftime("%H:%M:%S"))
    subprocess.call(restartpiReception)
    print("restarted piReception at " + time.strftime("%H:%M:%S"))
    subprocess.call(restartpiArt)
    print("restarted piArt at " + time.strftime("%H:%M:%S"))
    subprocess.call(restartpiTheatre)
    print("restarted piTheatre at " + time.strftime("%H:%M:%S"))
    subprocess.call(restartpiCanteenEAST)
    print("restarted piCanteenEAST at " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piCanteenWEST" and userCommand == "restart":
    subprocess.call(restartpiCanteenWEST)
    print("restarted piCanteenWEST " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piLester" and userCommand == "restart":
    subprocess.call(restartpiLester)
    print("restarted piLester " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piSixthform" and userCommand == "restart":
    subprocess.call(restartpiSixthform)
    print("restarted piSixthform " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piMusic" and userCommand == "restart":
    subprocess.call(restartpiMusic)
    print("restarted piMusic " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piReception" and userCommand == "restart":
    subprocess.call(restartpiReception)
    print("restarted piReception " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piArt" and userCommand == "restart":
    subprocess.call(restartpiArt)
    print("restarted piArt " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piTheatre" and userCommand == "restart":
    subprocess.call(restartpiTheatre)
    print("restarted piTheatre " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piCanteenEAST" and userCommand == "restart":
    subprocess.call(restartpiCanteenEAST)
    print("restarted piCanteenEAST " + time.strftime("%H:%M:%S"))

# Upgrade

elif clientsAffected == "all" and userCommand == "upgrade":
    print("This process can take a very long time, please be patient")
    subprocess.call(upgradepiCanteenWEST)
    print("upgraded piCanteenWEST at " + time.strftime("%H:%M:%S"))
    subprocess.call(upgradepiLester)
    print("upgraded piLester at " + time.strftime("%H:%M:%S"))
    subprocess.call(upgradepiSixthform)
    print("upgraded piSixthform at " + time.strftime("%H:%M:%S"))
    subprocess.call(upgradepiMusic)
    print("upgraded piMusic at " + time.strftime("%H:%M:%S"))
    subprocess.call(upgradepiReception)
    print("upgraded piReception at " + time.strftime("%H:%M:%S"))
    subprocess.call(upgradepiArt)
    print("upgraded piArt at " + time.strftime("%H:%M:%S"))
    subprocess.call(upgradepiTheatre)
    print("upgraded piTheatre at " + time.strftime("%H:%M:%S"))
    subprocess.call(upgradepiCanteenEAST)
    print("upgraded piCanteenEAST at " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piCanteenWEST" and userCommand == "upgrade":
    print("This process can take a very long time, please be patient")
    subprocess.call(upgradepiCanteenWEST)
    print("upgraded piCanteenWEST " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piLester" and userCommand == "upgrade":
    print("This process can take a very long time, please be patient")
    subprocess.call(upgradepiLester)
    print("upgraded piLester " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piSixthform" and userCommand == "upgrade":
    print("This process can take a very long time, please be patient")
    subprocess.call(upgradepiSixthform)
    print("upgraded piSixthform " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piMusic" and userCommand == "upgrade":
    print("This process can take a very long time, please be patient")
    subprocess.call(upgradepiMusic)
    print("upgraded piMusic " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piReception" and userCommand == "upgrade":
    print("This process can take a very long time, please be patient")
    subprocess.call(upgradepiReception)
    print("upgraded piReception " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piArt" and userCommand == "upgrade":
    print("This process can take a very long time, please be patient")
    subprocess.call(upgradepiArt)
    print("upgraded piArt " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piTheatre" and userCommand == "upgrade":
    print("This process can take a very long time, please be patient")
    subprocess.call(upgradepiTheatre)
    print("upgraded piTheatre " + time.strftime("%H:%M:%S"))
elif clientsAffected == "piCanteenEAST" and userCommand == "upgrade":
    print("This process can take a very long time, please be patient")
    subprocess.call(upgradepiCanteenEAST)
    print("upgraded piCanteenEAST " + time.strftime("%H:%M:%S"))
# Else

else:
    print("Sorry, " + userCommand + " " + clientsAffected + " is not recognised")
