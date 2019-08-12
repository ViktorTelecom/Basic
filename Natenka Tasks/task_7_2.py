#!/usr/bin/env python

from sys import argv

filename_source = argv[1]
filename_destination = argv[2]

#print (argv[1])
#print (argv[2])

filename_source = 'config_sw1.txt'
filename_destination = 'config_sw1_new.txt'

ignore = ['duplex', 'alias', 'Current configuration']

with open(filename_source, 'r') as file_source, open(filename_destination, 'w') as file_destination:
	for strLine in file_source:
		strNoCrLine = strLine.rstrip()
		bIgnoredFound = False
		for i in ignore:			
			if strNoCrLine.find(i) > -1:
				bIgnoredFound = True
				break
		if not strNoCrLine.startswith('!') and not bIgnoredFound:
			#print(strNoCrLine)
			file_destination.write(strNoCrLine)
			file_destination.write('\n')
