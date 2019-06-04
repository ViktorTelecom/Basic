#!/usr/bin/env python

import yaml
import sys
import csv
import re
import glob
from pprint import pprint

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def parse_sh_cdp_neighbors (strCommandInput):
	
	regexHostname = '(\w+)>.*'
	strLocalHostId = re.search(regexHostname,strCommandInput).group(1)
	
	intTempCoordinate = strCommandInput.find('Port ID')
	strTempBuffer = strCommandInput[intTempCoordinate+8:].strip()	
	regexSplitString = '\s{2,}'
	strTempBuffer2 = strTempBuffer.replace('Eth','        Eth')
	listOutputStrings = strTempBuffer2.split('\n')
	
	listOutputStrings[:] = [re.split(regexSplitString, member) for member in listOutputStrings]
	
	listOutputStringsPop = [member.pop(2) for member in listOutputStrings]
	listOutputStringsPop = [member.pop(2) for member in listOutputStrings]
	listOutputStringsPop = [member.pop(2) for member in listOutputStrings]
	
	dictData = {strLocalHostId : ({member[1] : {member[0] : member[2]} for member in listOutputStrings})}

	return dictData	

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def generate_topology_from_cdp(list_of_files, save_to_file = True, topology_filename = 'topology.yaml'):

	dictCommonOutput = {}

	for strFileName in list_of_files:
		with open(strFileName) as file:
			strCommandInput = file.read()	
		dictCdpOutput = parse_sh_cdp_neighbors(strCommandInput)
		dictCommonOutput.update(dictCdpOutput)
		
	

	if save_to_file:
		with open(topology_filename, 'w') as file:
			yaml.dump(dictCommonOutput, file)
	
	return
	
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


sh_cdp_neigh_files = glob.glob('sh_cdp*')
generate_topology_from_cdp(sh_cdp_neigh_files)



