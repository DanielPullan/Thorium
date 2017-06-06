import time
import os
import subprocess
import sys

# if boot is zero, we haven't ran through the script yet
if boot = 0:
    # Enable SSH on First Boot
    subprocess.call("sudo touch /boot/ssh")
    # Find out the hostname
    hostname = os.uname()
    # If there is raspberry in the hostname, it's not been named yet so
    if "raspberry" in hostname:
        # Read the hostname file we created in boot
        linestring = open('/boot/hostname.txt', 'r').read()
        # Set it as new hostname
        linestring = newHostname
        # Then actually make it the new hostname
        subprocess.call(["sudo", "hostnamectl", "set-hostname", newHostname])
        # If there isn't raspberry in name, it has been named
    else:
        # Print this for logging
        print(["This raspberry pi is called", hostname])
    # first boot to 1, so we can count where we are in the process
    firstBoot = 1
        # Expand root filesystem, this requires a restart
        subprocess.call(["sudo", "raspi-config","--expand-rootfs"])
# if boot is 1, we've done all the first setup steps, so we have room to install
# packages
elif boot = 1:
    # Update packages
    print ("updating")
    os.system("sudo apt-get update -y")
    # Upgrade Packages
    print ("upgrading")
    os.system("sudo apt-get upgrade -y")
    # Install PHP and PHP Related stuff
    print ("installing php5 and php5-mysql")
    os.system("sudo apt-get install php5 php5-mysql -y")

    # Install git and rsync
    print ("installing git")
    os.system("sudo apt-get install git rsync -y")

    # Install Apache2
    print ("installing webserver")
    os.system("sudo apt-get install apache2 -y")
