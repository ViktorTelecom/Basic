#!/usr/bin/env python


trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan']
				  
				  
fast_int = {'access':{'0/12':'10','0/14':'11','0/16':'17','0/17':'150'}, 
            'trunk':{'0/1':['add','10','20'],
                     '0/2':['only','11','30'],
                     '0/4':['del','17']} }
					 

for intf, vlan_set in fast_int['trunk'].items():
	strMethod = vlan_set.pop(0)
	strVlans = ','.join(vlan_set)
	print('interface FastEthernet' + intf)
	for command in trunk_template:
		if command.endswith('allowed vlan'):
			if strMethod == 'only':	
				print(' {} {}'.format(command, strVlans))
			elif strMethod == 'add':
				print(' {} add {}'.format(command, strVlans))
			elif strMethod == 'del':
				print(' {} remove {}'.format(command, strVlans))
			else:
				pass
		else:
			print(' {}'.format(command))
			
		