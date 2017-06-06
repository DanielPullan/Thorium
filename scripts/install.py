import time
import os
import subprocess
import sys

boot = raw_input("what boot are you on: ")

# if boot is zero, we haven't ran through the script yet
if boot == 0:
    # Enable SSH on First Boot
    subprocess.call(["sudo", "touch", "/boot/ssh"])
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
        # first boot to 1, so we can count where we are in the process
        boot = 1
        # Expand root filesystem, this requires a restart
        subprocess.call(["sudo", "raspi-config", "--expand-rootfs"])
# if boot is 1, we've done all the first setup steps, so we have room to install
# packages
elif boot == 1:
    # Update packages
    print("updating")
    os.system("sudo apt-get update -y")
    # Upgrade Packages
    print("upgrading")
    os.system("sudo apt-get upgrade -y")
    # Clean up
    print("cleaning")
    os.system("sudo apt-get clean")
    # Install X server
    print("Installing X Server")
    os.system("sudo apt-get install --no-install-recommends xserver-xorg -y")
    # Install a desktop environment
    print("Installing a desktop")
    os.system("sudo apt-get install raspberrypi-ui-mods")
    # Install PHP and PHP Related stuff
    print("installing php5 and friends")
    os.system(
        "sudo apt-get install libapache2-mod-php5 php5-mysql php5-curl php5-json -y")
    # Install git and rsync
    print("installing git")
    os.system("sudo apt-get install git rsync -y")
    # Install Apache2
    print("installing webserver")
    os.system("sudo apt-get install apache2 -y")
    # Install a browser
    print("installing browser")
    os.system("sudo apt-get install chromium-browser")
    boot = 2
    os.system("sudo reboot -y")
elif boot == 2:
    f = open('/etc/lightdm/lightdm.conf', 'w')  # to clear the file
    f.write("""
    #
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
    # unity-compositor-command = Unity compositor command to run (can also contain arguments e.g. unity-system-compositor -special-option)
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
    # autologin-user = User to log in with by default (overrides autologin-guest)
    # autologin-user-timeout = Number of seconds to wait before loading default user
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
    autologin - user = pi
    # autologin-user-timeout=0
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

    boot = 3
else:
	print("shit don't work")
