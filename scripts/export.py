# Thorium Export To Device Script
# Daniel Pullan (https://danielpullan.co.uk)

# import stuff
import time
import subprocess
import sys

# The first argument in the commandline will be the IP address of the device to export to
clientsAffected = sys.argv[1]

# Make a thing
exportToDevice = ["rsync", "-a", "/var/www/", "pi@"+clientsAffected, "--delete"]

if True:
    subprocess.call(exportToDevice)
    print("Exported to " + clientsAffected + " at " + time.strftime("%H:%N:%S"))
else:
    print("Error")
