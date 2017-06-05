import time
import os
import subprocess
import sys


firstBoot = raw_input("Is this the first boot? :")

if "yes" in firstBoot:
    print ("expanding filesystem")
    sudo raspi-config --expand-rootfs
elif "no" in firstBoot:
    print ("carry on my wayward son")
else:
    print (["Your response of ", firstBoot, " was not recognised, restart the script"])

print ("updating")
os.system("sudo apt-get update -y")

print ("upgrading")
os.system("sudo apt-get upgrade -y")

print ("installing php5 and php5-mysql")
os.system("sudo apt-get install php5 php5-mysql -y")

print ("installing git")
os.system("sudo apt-get install git rsync -y")

hostname = os.uname()

if "raspberry" in hostname:
    newHostname = raw_input("What to call this pi?: ")
    subprocess.call(["sudo", "hostnamectl", "set-hostname", newHostname])
else:
    print(["This raspberry pi is called", hostname])
