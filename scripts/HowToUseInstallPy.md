# How to use install.py

### if using a not-blank sd card:
	- delete all the partitions
	- create a NTFS partition that fills the entire sd card
	- use pi bakery, import the recipe
	- write to sd card

### if using a blank sd card:
	use pibakery, import the recipe
	write to sd card

### then in file explorer, open the boot sd card:
	- create a file called "hostname.txt"
	- in hostname.txt, write what you want to call the pi
	- if it doesn't already exist create another file called "ssh" (no extensions)
	- eject the sd card, put it in the pi

### ensure the pi has power and network:
	- use your ssh client of choice, connect to pi@theHostnameYouChose
	- login is "pi" and "calcium"
	- on first boot, run "sudo python3 install.py"
	- when running the script the first time, say "0"
	- on the second, say "1"
	- carry on until you hit "2"

### deploy pi where you need to deploy it