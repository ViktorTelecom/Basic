#!/usr/bin/env python

from pprint import pprint

#~~~~~~~~~~~~~~~~~	Function	~~~~~~~~~~~~~~~~~~~~~~~~~~~
			
def generate_trunk_config(trunk):
	dictOutput = {}
	
	
	trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']
					  
					 
	for key,value in trunk.items():
		listOutput = []	
		for string in trunk_template:
			strTemp = ' ' + string
			if string.endswith('vlan'):
				for vlan in value:
					strTemp += ' ' + str(vlan)
			listOutput.append(strTemp)
		
		dictOutput.update({key : listOutput})
		
	return dictOutput	




#---------------------------------------------------------------------------------------------

trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }
			   
				
strResult = generate_trunk_config(trunk_dict)

pprint(strResult)
