# Thorium Install Script
# Daniel Pullan (https://danielpullan.co.uk)
# Find out more about this script at https://danielpullan.co.uk/?thorium-install-script
# Instructions on how to use this script are found at https://github.com/DanielPullan/Thorium/wiki/How-to-use-Install.py

import subprocess
from pathlib import Path
import socket
import time

#TODO: Setup Private and Public Keys for login to Pi
#TODO: Look at running chrome with --no-first-run in order to skip the "you can seach from here with google"
#TODO: Change the "welcome to pixel" to the one I made
#TODO: Do the whole add pi user to www-data etc
#TODO: Script to restart only chrome


# Define a function for our config file detection / creation
def filestep():
    # define the file we will use as our config file
    my_file = Path('config.file')
    # if the file exists, we're not on the first boot
    if my_file.is_file():
        # open the file in read mode, write would wipe it
        configfile = open('config.file', 'r')
        # read the value, assign it's content to a value
        configvalue = configfile.read()
        # close the file like a good citizen
        configfile.close()
        # use rstrip to get rid of /n
        theresult = configvalue.rstrip()
        # return the variable that doesn't have /n
        return theresult
    # if the file doesn't exist, this is the first install
    else:
        # open our already defined config file in write mode
        configfile = open('config.file', 'w')
        # write 0, our starting variable
        configfile.write('0')
        # close the file like a good citizen
        configfile.close()
        # open it up again in read mode
        configfile = open('config.file', 'r')
        # set it's content to a variable
        configvalue = configfile.read()
        # close the file yet again, we're such good citizens
        configfile.close()
        # strip out /n, use that as our final variable for the step
        theresult = configvalue.rstrip()
        # return it so we can use it
        return theresult


# Define a function so that we can name our device
def namedevice():
    # get the current hostname, set to a variable
    hostname = socket.gethostname()
    # if raspberry is in hostname, we haven't set the hostname yet
    if "raspberry" in hostname:
        # open our hostname config in read mode, I don't remember doing it this way, it's smarter
        hostnameconfig = open('/boot/hostname.txt', 'r').read()
        # strip the /n, use that as our hostname
        newhostname = hostnameconfig.rstrip()
        # set the /n-free variable as our new hostname
        subprocess.call(["sudo", "hostnamectl", "set-hostname", newhostname])
    # else, raspberry doesn't exist in the name and this pi has already been named
    else:
        # print the name of our device, mainly for logging purposes
        print('this device has been named', hostname)

# I don't think this needs to exist, but it doesn't hurt
filestep()

# Set our bootvalue (the step that the script is in with the install) to the result of our file name function
bootvalue = filestep()

# Print the result, this was for debugging
print("the value of bootvalue is", bootvalue)

# if boot is zero, we haven't ran through the script yet
if bootvalue == "0":
    # enable ssh by creating an SSH file in boot
    subprocess.call(["sudo", "touch", "/boot/ssh"])
    # name our device using the name device function
    namedevice()
    # open our config file in write mode
    f = open('config.file', 'w')
    # write 1, since we've finished step 1 now
    f.write("1")
    # close the file like a good citizen
    f.close()
    # reboot our device, changing the hostname causes issues, this gets us away from that
    subprocess.call(["sudo", "reboot"])
# if boot is 1, we've done all the first setup steps, so we have room to install
# packages
elif bootvalue == "1":
    # Update packages
    print("updating")
    subprocess.call(["sudo", "apt-get", "update", "-y"])
    time.sleep(5)
    # Upgrade Packages
    print("upgrading")
    subprocess.call(["sudo", "apt-get", "upgrade", "-y"])
    time.sleep(5)
    # Clean up
    print("cleaning")
    subprocess.call(["sudo", "apt-get", "clean"])
    time.sleep(5)
    # Install X server
    print("Installing X Server")
    subprocess.call(["sudo", "apt-get", "install", "--no-install-recommends", "xserver-xorg", "-y"])
    # Install a desktop environment
    print("Installing a desktop")
    subprocess.call(["sudo", "apt-get", "install", "raspberrypi-ui-mods", "-y"])
    # Install PHP and PHP Related stuff
    print("installing php5 and friends")
    subprocess.call([
        "sudo", "apt-get", "install", "php5", "php5-common", "libapache2-mod-php5", "php5-mysql", "php5-curl",
        "php5-json", "-y"])
    # Install git and rsync
    print("installing git")
    subprocess.call(["sudo", "apt-get", "install", "git", "rsync", "-y"])
    # Install Apache2
    print("installing webserver")
    subprocess.call(["sudo", "apt-get", "install", "apache2", "-y"])
    # Install a browser
    print("installing browser")
    subprocess.call(["sudo", "apt-get", "install", "chromium-browser", "-y"])
    # Install unclutter and xdotool
    print("installing tools")
    subprocess.call(["sudo", "apt-get", "install", "unclutter", "xdotool", "-y"])
    print("boot order is now 2")
    f = open('config.file', 'w')
    f.write("2")
    f.close()
    subprocess.call(["sudo", "reboot"])
elif bootvalue == "2":
    print("Creating startup script")
    f = open('start_chromium.sh', 'w')
    f.write("""
    # Run browser after boot to desktop
    /bin/sleep 3
    sudo -u pi chromium-browser --kiosk --incognito http://localhost &
    # End of script
    """)
    f.close()
    print("Creating refresh script")
    f = open('start_URLrefresh.sh', 'w')
    f.write("""
    # Start a goofy command loop to refresh the browser every 90 seconds
    /bin/sleep 6
    /usr/bin/lxterminal --command watch -n 986400 xdotool key ctrl+F5 &
    # End of goofy script
    """)
    f.close()
    print("Making scripts powerful.. excecutable?")
    subprocess.call(['sudo', 'chmod', '755', 'start_URLrefresh.sh'])
    subprocess.call(['sudo', 'chmod', '755', 'start_chromium.sh'])
    subprocess.call(['sudo', 'chmod', '+x', 'start_URLrefresh.sh'])
    subprocess.call(['sudo', 'chmod', '+x', 'start_URLrefresh.sh'])
    print("Changing lightdm conf")
    f = open('/etc/lightdm/lightdm.conf', 'w')  # to clear the file
    f.write("""#
# General configuration
#
# start-default-seat = True to always start one seat if none are defined in the configuration
# greeter-user = User to run greeter as
# minimum-display-number = Minimum display number to use for X servers
# minimum-vt = First VT to run displays on
# lock-memory = True to prevent memory from being paged to disk
# user-authority-in-system-dir = True if session authority should be in the system location
# guest-account-script = Script to be run to setup guest account
# logind-load-seats = True to automatically set up multi-seat configuration from logind
# logind-check-graphical = True to on start seats that are marked as graphical by logind
# log-directory = Directory to log information to
# run-directory = Directory to put running state in
# cache-directory = Directory to cache to
# sessions-directory = Directory to find sessions
# remote-sessions-directory = Directory to find remote sessions
# greeters-directory = Directory to find greeters
#
[LightDM]
# start-default-seat=true
# greeter-user=lightdm
# minimum-display-number=0
# minimum-vt=7
# lock-memory=true
# user-authority-in-system-dir=false
# guest-account-script=guest-account
# logind-load-seats=false
# logind-check-graphical=false
# log-directory=/var/log/lightdm
# run-directory=/var/run/lightdm
# cache-directory=/var/cache/lightdm
# sessions-directory=/usr/share/lightdm/sessions:/usr/share/xsessions
# remote-sessions-directory=/usr/share/lightdm/remote-sessions
# greeters-directory=/usr/share/lightdm/greeters:/usr/share/xgreeters

#
# Seat defaults
#
# type = Seat type (xlocal, xremote)
# xdg-seat = Seat name to set pam_systemd XDG_SEAT variable and name to pass to X server
# pam-service = PAM service to use for login
# pam-autologin-service = PAM service to use for autologin
# pam-greeter-service = PAM service to use for greeters
# xserver-command = X server command to run (can also contain arguments e.g. X -special-option)
# xserver-layout = Layout to pass to X server
# xserver-config = Config file to pass to X server
# xserver-allow-tcp = True if TCP/IP connections are allowed to this X server
# xserver-share = True if the X server is shared for both greeter and session
# xserver-hostname = Hostname of X server (only for type=xremote)
# xserver-display-number = Display number of X server (only for type=xremote)
# xdmcp-manager = XDMCP manager to connect to (implies xserver-allow-tcp=true)
# xdmcp-port = XDMCP UDP/IP port to communicate on
# xdmcp-key = Authentication key to use for XDM-AUTHENTICATION-1 (stored in keys.conf)
# unity-compositor-command = Unity compositor command to run
# unity-compositor-timeout = Number of seconds to wait for compositor to start
# greeter-session = Session to load for greeter
# greeter-hide-users = True to hide the user list
# greeter-allow-guest = True if the greeter should show a guest login option
# greeter-show-manual-login = True if the greeter should offer a manual login option
# greeter-show-remote-login = True if the greeter should offer a remote login option
# user-session = Session to load for users
# allow-user-switching = True if allowed to switch users
# allow-guest = True if guest login is allowed
# guest-session = Session to load for guests (overrides user-session)
# session-wrapper = Wrapper script to run session with
# greeter-wrapper = Wrapper script to run greeter with
# guest-wrapper = Wrapper script to run guest sessions with
# display-setup-script = Script to run when starting a greeter session (runs as root)
# display-stopped-script = Script to run after stopping the display server (runs as root)
# greeter-setup-script = Script to run when starting a greeter (runs as root)
# session-setup-script = Script to run when starting a user session (runs as root)
# session-cleanup-script = Script to run when quitting a user session (runs as root)
# autologin-guest = True to log in as guest by default
autologin-user=pi
autologin-user-timeout=0
# autologin-session = Session to load for automatic login (overrides user-session)
# autologin-in-background = True if autologin session should not be immediately activated
# exit-on-failure = True if the daemon should exit if this seat fails
#
[SeatDefaults]
# type=xlocal
# xdg-seat=seat0
# pam-service=lightdm
# pam-autologin-service=lightdm-autologin
# pam-greeter-service=lightdm-greeter
# xserver-command=X
# xserver-layout=
# xserver-config=
# xserver-allow-tcp=false
# xserver-share=true
# xserver-hostname=
# xserver-display-number=
# xdmcp-manager=
# xdmcp-port=177
# xdmcp-key=
# unity-compositor-command=unity-system-compositor
# unity-compositor-timeout=60
# greeter-session=example-gtk-gnome
greeter - hide - users = false
# greeter-allow-guest=true
# greeter-show-manual-login=false
# greeter-show-remote-login=true
# user-session=default
# allow-user-switching=true
# allow-guest=true
# guest-session=
# session-wrapper=lightdm-session
# greeter-wrapper=
# guest-wrapper=
# display-setup-script=
# display-stopped-script=
# greeter-setup-script=
# session-setup-script=
# session-cleanup-script=
# autologin-guest=false
autologin-user=pi
autologin-user-timeout=0
# autologin-in-background=false
# autologin-session=UNIMPLEMENTED
# exit-on-failure=false
# don't sleep the screen
xserver - command = X - s 0 dpms

#
# Seat configuration
#
# Each seat must start with "Seat:".
# Uses settings from [SeatDefaults], any of these can be overriden by setting them in this section.
#
#[Seat:0]

#
# XDMCP Server configuration
#
# enabled = True if XDMCP connections should be allowed
# port = UDP/IP port to listen for connections on
# key = Authentication key to use for XDM-AUTHENTICATION-1 or blank to not use authentication (stored in keys.conf)
#
# The authentication key is a 56 bit DES key specified in hex as 0xnnnnnnnnnnnnnn.  Alternatively
# it can be a word and the first 7 characters are used as the key.
#
[XDMCPServer]
# enabled=false
# port=177
# key=

#
# VNC Server configuration
#
# enabled = True if VNC connections should be allowed
# command = Command to run Xvnc server with
# port = TCP/IP port to listen for connections on
# width = Width of display to use
# height = Height of display to use
# depth = Color depth of display to use
#
[VNCServer]
# enabled=false
# command=Xvnc
# port=5900
# width=1024
# height=768
# depth=8

""")
    f.close()
    subprocess.call(['sudo', 'dpkg-reconfigure', 'lightdm'])

    # removing thorium folders in case it already exists (it shouldn't)
    print("removing folders just in case")
    subprocess.call(["sudo", "rm", "-rf", "thorium"])
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
    # wipe the default 000-default file
    print("goodbye contents of default apache file")
    f = open('/etc/apache2/sites-available/000-default.conf', 'w')  # to clear the file
    # write the new config in to direct to thorium folder
    print("hello new contents of default apache file")
    f.write("""
    <VirtualHost *:80>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        #ServerName www.example.com

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/thorium

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
    </VirtualHost>

    # vim: syntax=apache ts=4 sw=4 sts=4 sr noet

    """)
    # close the file like a good citizen
    f.close()
    # autostart stuff
    print("out autostart")
    f = open('/home/pi/.config/lxsession/LXDE-pi/autostart', 'w')
    f.write("""@lxpanel --profile LXDE - pi
@pcmanfm --desktop - -profile LXDE - pi
# @xscreensaver -no - splash
@point-rpi
@xset s off
@xset s noblank
@xset -dpms
@unclutter -idle 5 -root
@/home/pi/start_URLrefresh.sh
@/home/pi/start_chromium.sh
""")
    f.close()
    print("Set up the database connection stuff")
    subprocess.call(['sudo', 'touch', '/var/www/html/thorium/scripts/password.php'])
    f = open('/var/www/html/thorium/scripts/password.php', 'w')
    f.write("""<?php
    $servername = "<insert server name>";
    $username = "<insert username for mysql>";
    $password = "<insert mysql password>";
    $dbname = "<insert database name>";
?>
""")
    f.close()
    # add pi user to www-data group
    subprocess.call(['sudo', 'gpasswd', '-a', 'pi', 'www-data'])
    # chown /var/www -R to pi:www-data
    subprocess.call(['sudo', 'chown', '-R', 'pi:www-data', '/var/www'])
    # copy restart script to home
    subprocess.call(['sudo', 'chown', '-R', 'pi:www-data', '/var/www'])
    # hotpluggy stuff now
    f = open('/boot/config.txt', 'w')
    f.write("""# For more options and information see
# http://rpf.io/configtxtreadme
# Some settings may impact device functionality. See link above for details

# uncomment if you get no picture on HDMI for a default "safe" mode
#hdmi_safe=1

# uncomment this if your display has a black border of unused pixels visible
# and your display can output without overscan
disable_overscan=1

# uncomment the following to adjust overscan. Use positive numbers if console
# goes off screen, and negative if there is too much border
#overscan_left=16
#overscan_right=16
#overscan_top=16
#overscan_bottom=16

# uncomment to force a console size. By default it will be display's size minus
# overscan.
#framebuffer_width=1280
#framebuffer_height=720

# uncomment if hdmi display is not detected and composite is being output
#hdmi_force_hotplug=1

# uncomment to force a specific HDMI mode (this will force VGA)
hdmi_group=1
hdmi_mode=4

# uncomment to force a HDMI mode rather than DVI. This can make audio work in
# DMT (computer monitor) modes
#hdmi_drive=2

# uncomment to increase signal to HDMI, if you have interference, blanking, or
# no display
#config_hdmi_boost=4

# uncomment for composite PAL
#sdtv_mode=2

#uncomment to overclock the arm. 700 MHz is the default.
#arm_freq=800

# Uncomment some or all of these to enable the optional hardware interfaces
#dtparam=i2c_arm=on
#dtparam=i2s=on
#dtparam=spi=on

# Uncomment this to enable the lirc-rpi module
#dtoverlay=lirc-rpi

# Additional overlays and parameters are documented /boot/overlays/README

# Enable audio (loads snd_bcm2835)
dtparam=audio=on""")
    f.close()
    # set the boot value to 3
    print("boot order is now 3")
    f = open('config.file', 'w')
    f.write("3")
    f.close()
else:
    # once we've done everything... remove the file!
    subprocess.call(['sudo', 'rm', 'install.py'])
    print("install.py has been removed")
    subprocess.call(['sudo', 'rm', 'config.file'])
    print("config.file removed, last state was ", bootvalue)
