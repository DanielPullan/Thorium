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

# Always run this script as true always return as true
if True:
    # Do a subprocess call that uses the array we set with all the information required for the rsync command
    subprocess.call(exportToDevice)
    # Print that it was successful, useful for logging
    print("Exported to " + clientsAffected + " at " + time.strftime("%H:%N:%S"))
# If true doesn't return as true, we have bigger fish to fry
else:
    # Print error, look into what loopy planet we're currently existing on.
    print("Error")
