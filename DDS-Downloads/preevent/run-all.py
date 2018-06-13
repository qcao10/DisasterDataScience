import os

file = open('run-all-pre.sh','w')
file.write('#!/bin/bash')
for filename in os.listdir("/Users/danielcao/Google Drive/0 UW/7Others/DDS/0Git/DDS-Downloads/preevent"):
	if filename.endswith(".sh"):
		file.write('./'+filename+'\n')

file.close()
