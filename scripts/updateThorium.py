# Thorium Update Script
# Daniel Pullan (https://danielpullan.co.uk)

# Find out more about Thorium at https://danielpullan.co.uk/?thorium
# Instructions on how to use this script are found at https://github.com/DanielPullan/Thorium/wiki/how-to-update

# This script is only for use on the server, so when you set up your server, ensure that you move it to the root of
# the administrator user. If your user on server is called something else, this script won't work.
# Really I should do some sort of check to check what the current user is, then change /home/administrator to
# /home/<currentuser> instead, but this is how this one is going to go. I can update this later. Maybe.

import subprocess
import time

print("You are about to update Thorium. Be careful as this script will cause you to need to set things up again")
time.sleep(4)
print("We will move your database file and your images folder, as well as your logo, but everything else will be gone")
time.sleep(4)
print("You will now have 10 seconds to cancel, CTRL+Z to cancel update")
time.sleep(10)
print("Okay, now strap in, keep all arms and legs inside the vehicle at all times and enjoy the ride.")

# move database file to safe place
print("Moving database file")
subprocess.call(["sudo", "mv", "/var/www/html/thorium/scripts/password.php", "/home/administrator"])
# move images to safe place
print("Moving images")
subprocess.call(["sudo", "mv", "/var/www/html/thorium/images", "/home/administrator"])
# move logo
print("Moving logo")
subprocess.call(["sudo", "mv", "/var/www/html/thorium/assets/logo.png", "/home/administrator"])

# remove current thorium
print("Removing thorium")
subprocess.call(["sudo", "rm", "-rf", "/var/www/html/thorium"])
# download latest version of Thorium from Github
print("downloading thorium")
subprocess.call(["git", "clone", "https://github.com/danielpullan/thorium"])
# rm the default index.html file
print("goodbye default index")
subprocess.call(["sudo", "rm", "/var/www/html/index.html"])
# mv the thorium folder to the html folder
print("moving folder")
subprocess.call(["sudo", "mv", "thorium/", "/var/www/html"])

# move database file back to thorium
print("Moving database file")
subprocess.call(["sudo", "mv", "/home/administrator/password.php", "/var/www/html/thorium/scripts/password.php"])
# move images back to thorium
print("Moving images")
subprocess.call(["sudo", "mv", "/home/administrator/images", "/var/www/html/thorium/images"])
# move logo back to thorium
print("Moving logo")
subprocess.call(["sudo", "mv", "/home/administrator/logo.png", "/var/www/html/thorium/assets/logo.png"])

print("All done, I hope not much broke.")
