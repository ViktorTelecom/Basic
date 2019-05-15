#!/usr/bin/env python

from pprint import pprint
from tabulate import tabulate

import sys

def parse_cdp_neighbors(strUserInput):
########### Parse CDP Neighbours ################
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	intTempCoordinate = strUserInput.find('>')
	strLocalHostId = strUserInput[:intTempCoordinate].strip()

	intTempCoordinate = strUserInput.find('Port ID') + 8
	strTempString = strUserInput[intTempCoordinate:].strip()

	listOutputStrings = strTempString.split('\n')

	listOutputStrings[:] = [member.split('       ') for member in listOutputStrings]
	listOutputStrings[:] = [[member.lstrip() for member in listString] for listString in listOutputStrings]

	listOutputStringsPop = [member.pop(2) for member in listOutputStrings]
	listOutputStringsPop = [member.pop(2) for member in listOutputStrings]
	listOutputStringsPop = [member.pop(2) for member in listOutputStrings]

	dictData = dict([[(strLocalHostId,member[1]),(member[0],member[2])] for member in listOutputStrings])

	return dictData

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

strUserInput = sys.stdin.read()
dictCdpOutput = parse_cdp_neighbors(strUserInput)

print()
pprint(dictCdpOutput)
