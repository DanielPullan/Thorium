import subprocess
import sys

userCommand = sys.argv[1]

pi = ["hi", "hello", "heyy", "hola"]

if userCommand:
	for x in pi:
		ayy =('pi@', x)
		ooo =  ayy.rstrip()
		print(ooo)
		subprocess.call(["rsync", "-a", "/var/www/", str(ayy), ":/var/www/", "--delete"])
