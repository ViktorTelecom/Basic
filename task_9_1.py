#!/usr/bin/env python

from pprint import pprint
			
def generate_access_config(access,psecurity=False):
	dictOutput = {}
	access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']
					   
	port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']


					 
	for key,value in access.items():
		#listOutput.append('interface {}'.format(key))
		#dictOutput.append(key)
		listOutput = []	
		for string in access_template:
			strTemp = ' ' + string
			if string.endswith('vlan'):
				strTemp += ' {}'.format(value)
			listOutput.append(strTemp)
		if psecurity:
			for sec_string in port_security:
				listOutput.append(' ' + sec_string)
		
		dictOutput.update({key : listOutput})
		
	return dictOutput	

		

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }


				
strResult = generate_access_config(access_dict,True)

pprint(strResult)
