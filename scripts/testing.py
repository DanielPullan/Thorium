import subprocess
import sys

userCommand = sys.argv[1]

pi = ["hi", "hello", "heyy", "hola"]

if userCommand:
	for x in pi:
		ayy =['pi@', x]
		ooo =  str(ayy).rstrip()
		print(ooo)
		subprocess.call(["rsync", "-a", "/var/www/", ooo, ":/var/www/", "--delete"])
