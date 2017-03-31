import time
import os
import subprocess

userInput = raw_input("What would you like to sync?: ")

gyllir = ["rsync", "-a", "/var/www/html", "pi@gyllir:/var/www/", "--delete"]
sinir = ["rsync", "-a", "/var/www/html", "pi@sinir:/var/www/", "--delete"]
gisl = ["rsync", "-a", "/var/www/html", "pi@gisl:/var/www/", "--delete"]
gulltopp = ["rsync", "-a", "/var/www/html", "pi@gulltopp:/var/www/", "--delete"]

if userInput == ("all"):
        subprocess.call(gyllir)
        print("exported to gyllir")
        time.sleep(5)
        subprocess.call(sinir)
        print("exported to sinir")
        time.sleep(5)
        subprocess.call(gisl)
        print("exported to gisl")
        time.sleep(5)
        subprocess.call(gulltopp)
        print("exported to gulltopp")


elif userInput == ("gyllir"):
        subprocess.call(gyllir)
        print("exported to gyllir")

elif userInput == ("sinir"):
        subprocess.call(sinir)
        print("exported to sinir")

elif userInput == ("gisl"):
        subprocess.call(gisl)
        print("exported to gisl")

elif userInput == ("gulltopp"):
        subprocess.call(gulltopp)
        print("exported to gulltopp")

else:
        print ("sorry, ", userInput, " is not recognised")
