# Thorium
A replacement for PHS's current Digital Signage Solution
(I wanted a name related to Norse Mythology whilst keeping with the naming conventions at work.)

## Requirements
Currently, you need a bunch of linux based clients, I'm using OG Raspberry Pi's.
You'll need a browser, a webserver and rsync installed on all the clients. The clients will need a desktop environment and xserver.
You'll then need a host linux server, again i'm using a pi. This will need a webserver, rsync then whatever i need for the admin stuff.
Then you'll need to be able to login with SSH keys from the master server to all the clients.

I will add more instructions to use once I've finished this thing.

### Versioning explained
Major.Minor.Status
Statuses release, rc (release candidate), beta, dev

For example, 1.0.dev is the development of version 1.0. 1.0.release would be the public version.


files that need editing on the pi's
/etc/sudoers.d/010_pi-nopasswd (add SERVERUSERNAME ALL=(ALL) NOPASSWD: ALL)
/boot/config.txt (hdmi_force_hotplug=1 hdmi_drive=2)
/home/pi/.config/lxsession/LXDE-pi/autostart (add @chromium-browser --incognito --kiosk http://localhost/)


- install chromium browser
- set web directory to /var/www/Thorium
- install lite version of raspbian

sudo apt-get install --no-install-recommends xserver-xorg
sudo apt-get install --no-install-recommends xinit
sudo apt-get install raspberrypi-ui-mods
sudo apt-get install chromium-browser

nano /home/pi/.config/lxsession/LXDE-pi/autostart

edit sudoers so master server can do sudo commands without having to input the command (fixes issue #5)

make sure to pip-install shmetterling (clue, not actual name)

@chromium-browser --incognito --kiosk http://localhost/  # load chromium after boot and point to the localhost webserver in full screen mode (add on the last line)
