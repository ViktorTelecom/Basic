#!/usr/bin/env python

from operator import itemgetter

listCommon = []
with open('CAM_table.txt', 'r') as file_source:
	for strLine in file_source:
		strNoCrLine = strLine.rstrip()			
		if strNoCrLine.find('DYNAMIC') > -1:
			listLine = strNoCrLine.split()
			listLine.remove('DYNAMIC')
			listCommon.append(listLine)

listCommon.sort(key=itemgetter(0))

for x,y,z in listCommon:
	print(x, '   ', y, '   ',z)
	
strVlanChosen = input('Vlan ID: ')

for x,y,z in listCommon:
	if x == strVlanChosen:
			print(x, '   ', y, '   ',z)