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
        print("exported to gyllir at "+time.strftime("%H:%M:%S"))
        time.sleep(5)
        subprocess.call(sinir)
        print("exported to sinir at "+time.strftime("%H:%M:%S"))
        time.sleep(5)
        subprocess.call(gisl)
        print("exported to gisl at "+time.strftime("%H:%M:%S"))
        time.sleep(5)
        subprocess.call(gulltopp)
        print("exported to gulltopp at "+time.strftime("%H:%M:%S"))


elif userInput == ("gyllir"):
        subprocess.call(gyllir)
        print("exported to gyllir "+time.strftime("%H:%M:%S"))

elif userInput == ("sinir"):
        subprocess.call(sinir)
        print("exported to sinir "+time.strftime("%H:%M:%S"))

elif userInput == ("gisl"):
        subprocess.call(gisl)
        print("exported to gisl "+time.strftime("%H:%M:%S"))

elif userInput == ("gulltopp"):
        subprocess.call(gulltopp)
        print("exported to gulltopp "+time.strftime("%H:%M:%S"))

else:
        print ("Sorry, "+ userInput+" is not recognised").
