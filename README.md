# Thorium
A replacement for PHS's current Digital Signage Solution
(I wanted a name related to Norse Mythology whilst keeping with the naming conventions at work.)

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

@chromium-browser --incognito --kiosk http://localhost/  # load chromium after boot and point to the localhost webserver in full screen mode (add on the last line)
