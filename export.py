## import stuff, can't remember if OS is needed but time and subprocess definately is
import time
import os
import subprocess

## ask the user what they want to sync to, save as a variable
userInput = raw_input("What would you like to sync?: ")
userCommand = raw_input("what would you like to do?: ")
clientsAffected = raw_input("to which clients?: ")


## define all the clients and the commands to rsync to them
exportGyllir = ["rsync", "-a", "/var/www/html", "pi@gyllir:/var/www/", "--delete"]
exportSinir = ["rsync", "-a", "/var/www/html", "pi@sinir:/var/www/", "--delete"]
exportGisl = ["rsync", "-a", "/var/www/html", "pi@gisl:/var/www/", "--delete"]
exportGulltopp = ["rsync", "-a", "/var/www/html", "pi@gulltopp:/var/www/", "--delete"]

restartGyllir = ["SSH", "pi@gyllir", "sudo", "shutdown", "-r", "now"]
resstartSinir = ["SSH", "pi@sinir", "sudo", "shutdown", "-r", "now"]
restartGisl = ["SSH", "pi@gisl", "sudo", "shutdown", "-r", "now"]
restartGulltopp = ["SSH", "pi@gulltopp", "sudo", "shutdown", "-r", "now"]

## if userInput is all, rsync to every pi. have 5 sec's inbetween as a breather for network
## add time for logging
if userInput == ("all"):
        subprocess.call(exportGyllir)
        print("exported to gyllir at "+time.strftime("%H:%M:%S"))
        time.sleep(5)
        subprocess.call(exportSinir)
        print("exported to sinir at "+time.strftime("%H:%M:%S"))
        time.sleep(5)
        subprocess.call(exportGisl)
        print("exported to gisl at "+time.strftime("%H:%M:%S"))
        time.sleep(5)
        subprocess.call(exportGulltopp)
        print("exported to gulltopp at "+time.strftime("%H:%M:%S"))

## only one pi
## add time for logging
elif userInput == ("gyllir"):
        subprocess.call(gyllir)
        print("exported to gyllir "+time.strftime("%H:%M:%S"))
## only one pi
## add time for logging
elif userInput == ("sinir"):
        subprocess.call(sinir)
        print("exported to sinir "+time.strftime("%H:%M:%S"))
## only one pi
## add time for logging
elif userInput == ("gisl"):
        subprocess.call(gisl)
        print("exported to gisl "+time.strftime("%H:%M:%S"))
## only one pi
## add time for logging
elif userInput == ("gulltopp"):
        subprocess.call(gulltopp)
        print("exported to gulltopp "+time.strftime("%H:%M:%S"))
## print what was input, say it wasn't recognised
else:
        print ("Sorry, "+ userInput+" is not recognised")
