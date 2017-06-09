import os
import subprocess
from pathlib import Path
import socket


def filestep():
    my_file = Path('config.file')
    if my_file.is_file():
        configfile = open('config.file', 'r')
        configvalue = configfile.read()
        configfile.close()
        theresult = configvalue.rstrip()
        return theresult
    else:
        configfile = open('config.file', 'w')
        configfile.write('0')
        configfile.close()
        configfile = open('config.file', 'r')
        configvalue = configfile.read()
        configfile.close()
        theresult = configvalue.rstrip()
        return theresult


def namedevice():
    hostname = socket.gethostname()
    if "raspberry" in hostname:
        hostnameconfig = open('/boot/hostname.txt', 'r').read()
        newhostname = hostnameconfig.rstrip()
        subprocess.call(["sudo", "hostnamectl", "set-hostname", newhostname])
    else:
        print('this device has been named', hostname)

filestep()

bootvalue = filestep()

print("the value of bootvalue is", bootvalue)

# if boot is zero, we haven't ran through the script yet
if bootvalue == "0":
    subprocess.call(["sudo", "touch", "/boot/ssh"])
    namedevice()
    f = open('config.file', 'w')
    f.write("1")
    f.close()
    subprocess.call(["sudo", "reboot"])
# if boot is 1, we've done all the first setup steps, so we have room to install
# packages
elif bootvalue == "1":
    # Update packages
    print("updating")
    subprocess.call(["sudo", "apt-get", "update", "-y"])
    # Upgrade Packages
    print("upgrading")
    subprocess.call(["sudo", "apt-get", "upgrade", "-y"])
    # Clean up
    print("cleaning")
    subprocess.call(["sudo", "apt-get", "clean"])
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
    print("boot order is now 2")
    f = open('config.file', 'w')
    f.write("2")
    f.close()
    subprocess.call(["sudo", "reboot"])
elif bootvalue == "2":
    print("Changing lightdm conf")
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

    # TODO kiosk mode
    # TODO cron job to update content every day at 2am

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
    # set the boot value to 3
    print("boot order is now 3")
    f = open('config.file', 'w')
    f.write("3")
    f.close()
else:
    # once we've done everything... remove the file!
    print("shit don't work")
