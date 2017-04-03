## import stuff, can't remember if OS is needed but time and subprocess definately is
import time
import os
import subprocess

## ask the user what they want to sync to, save as a variable
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
if clientsAffected == ("all") and userCommand == ("export"):
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

## export to nly one pi
## add time for logging
elif clientsAffected == ("gyllir") and userCommand == ("export"):
        subprocess.call(gyllir)
        print("exported to gyllir "+time.strftime("%H:%M:%S"))
## export to only one pi
## add time for logging
elif clientsAffected == ("sinir") and userCommand == ("export"):
        subprocess.call(sinir)
        print("exported to sinir "+time.strftime("%H:%M:%S"))
## export to only one pi
## add time for logging
elif clientsAffected == ("gisl") and userCommand == ("export"):
        subprocess.call(gisl)
        print("exported to gisl "+time.strftime("%H:%M:%S"))
## export to only one pi
## add time for logging
elif clientsAffected == ("gulltopp") and userCommand == ("export"):
        subprocess.call(gulltopp)
        print("exported to gulltopp "+time.strftime("%H:%M:%S"))

elif clientsAffected == ("all") and userCommand == ("restart"):
        subprocess.call(restartGyllir)
        print("exported to gyllir at "+time.strftime("%H:%M:%S"))
        time.sleep(5)
        subprocess.call(restartSinir)
        print("exported to sinir at "+time.strftime("%H:%M:%S"))
        time.sleep(5)
        subprocess.call(restartGisl)
        print("exported to gisl at "+time.strftime("%H:%M:%S"))
        time.sleep(5)
        subprocess.call(restartGulltopp)
        print("exported to gulltopp at "+time.strftime("%H:%M:%S"))

## restart only one pi
## add time for logging
elif clientsAffected == ("gyllir") and userCommand == ("restart"):
        subprocess.call(gyllir)
        print("restarted gyllir "+time.strftime("%H:%M:%S"))
## restart only one pi
## add time for logging
elif clientsAffected == ("sinir") and userCommand == ("restart"):
        subprocess.call(sinir)
        print("restarted sinir "+time.strftime("%H:%M:%S"))
## restart only one pi
## add time for logging
elif clientsAffected == ("gisl") and userCommand == ("restart"):
        subprocess.call(gisl)
        print("restarted gisl "+time.strftime("%H:%M:%S"))
## restart only one pi
## add time for logging
elif clientsAffected == ("gulltopp") and userCommand == ("restart"):
        subprocess.call(gulltopp)
        print("restarted gulltopp "+time.strftime("%H:%M:%S"))

else:
        print ("Sorry, "+ userInput+" is not recognised")
