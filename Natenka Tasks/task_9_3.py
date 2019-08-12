#!/usr/bin/env python

from pprint import pprint

#~~~~~~~~~~~~~~~~~	Function	~~~~~~~~~~~~~~~~~~~~~~~~~~~
			
def get_int_vlan_map(filename):
	"""Task 9_3"""

	filename = 'config_sw1.txt'
	
	bIfConfigInProgress = False
	dictOutput = {}
	
	with open(filename) as file:
		for strLine in file:
			if strLine.startswith('interface Ethernet'):
				bIfConfigInProgress = True
				strNew = strLine.replace('interface ','')
				strIfName = strNew.strip()
				listTrunkVlans = []
				strAccessVlan = '1'
			elif bIfConfigInProgress:
				if strLine.startswith(' switchport trunk allowed vlan'):
					strNew = strLine.replace(' switchport trunk allowed vlan ','').strip()
					listTrunkVlans.append(strNew)
				elif strLine.startswith(' switchport access vlan'):
					strNew = strLine.replace(' switchport access vlan ','')
					strAccessVlan = strNew.strip()
				elif strLine.startswith(' switchport mode'):
					if strLine.endswith('access\n'):
						dictOutput.update({strIfName : strAccessVlan})
					elif strLine.endswith('trunk\n'):
						dictOutput.update({strIfName : listTrunkVlans})
					bIfConfigInProgress = False
				elif strLine.startswith('!'):
					bIfConfigInProgress = False


	return dictOutput	


#---------------------------------------------------------------------------------------------


strResult = get_int_vlan_map('config_sw1.txt')

pprint(strResult)	
