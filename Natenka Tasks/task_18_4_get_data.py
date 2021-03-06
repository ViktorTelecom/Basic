# -*- coding: utf-8 -*-

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import sqlite3
import sys

db_filename = 'dhcp_snooping_upgraded.db'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def NoArguments():

	conn = sqlite3.connect(db_filename)
	print('\nВ таблице dhcp такие записи:')
	print('-' * 60)
	print('-' * 60)
	
	query_active = 'select * from dhcp where active = 1'
	query_inactive = 'select * from dhcp where active = 0'
	
	result_active = conn.execute(query_active).fetchall()
	result_inactive = conn.execute(query_inactive).fetchall()
	
	print('Active Values:')
	print('-' * 60)
	for row in result_active:
		mac, ip, vlan, interface, switch, active = row
		print ('{:18}  {:16}  {:6}  {:16}  {:6}  {:3}'.format(mac, ip, vlan, interface, switch, active))
	print('-' * 60)
	
	
	print('Inactive Values:')
	print('-' * 60)
	for row in result_inactive:
		mac, ip, vlan, interface, switch, active = row
		print ('{:18}  {:16}  {:6}  {:16}  {:6}  {:3}'.format(mac, ip, vlan, interface, switch, active))
	print('-' * 60)
		
	print()	
		
	return

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def TwoArguments():

	key = sys.argv[1]
	value = sys.argv[2]
	
	keys = ['mac', 'ip', 'vlan', 'interface' , 'switch', 'active']
	
	if key in keys:
		keys.remove(key)
	else:
		print('Данный параметр не поддерживается.')
		print('Допустимые значения параметров: mac, ip, vlan, interface, switch, active')
		return
		
	conn = sqlite3.connect(db_filename)

	#Позволяет далее обращаться к данным в колонках, по имени колонки
	conn.row_factory = sqlite3.Row

	print('\nDetailed information for host(s) with', key, '=', value)
	print('-' * 60)


	query_active = 'select * from dhcp where {} = ? and active = 1'.format(key)
	query_inactive = 'select * from dhcp where {} = ? and active = 0'.format(key)
	
	result_active = conn.execute(query_active, (value, ))
	result_inactive = conn.execute(query_inactive, (value, ))

	print('-' * 60)
	print('Active Values:')
	print('-' * 60)
	for row in result_active:
		for k in keys:
			print('{:12}: {}'.format(k, row[k]))
		print('-' * 60)

	print('-' * 60)
	print('Inactive Values:')
	print('-' * 60)
	for row in result_inactive:
		for k in keys:
			print('{:12}: {}'.format(k, row[k]))
		print('-' * 60)
	
	return	

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


if len(sys.argv) == 1:
	NoArguments()
elif len(sys.argv) == 3:
	TwoArguments()
else:
	print ('Надо ноль или два аргумента.')




'''

$ python get_data.py vln 10
Данный параметр не поддерживается.
Допустимые значения параметров: mac, ip, vlan, interface, switch


$ python get_data.py

В таблице dhcp такие записи:
----------------------------------------------------------------------
00:09:BB:3D:D6:58  10.1.10.2         10    FastEthernet0/1      sw1
00:04:A3:3E:5B:69  10.1.5.2          5     FastEthernet0/10     sw1
00:05:B3:7E:9B:60  10.1.5.4          5     FastEthernet0/9      sw1
00:07:BC:3F:A6:50  10.1.10.6         10    FastEthernet0/3      sw1
00:09:BC:3F:A6:50  192.168.1.100     100   FastEthernet0/5      sw1
00:A9:BB:3D:D6:58  10.1.10.20        10    FastEthernet0/7      sw2
00:B4:A3:3E:5B:69  10.1.5.20         5     FastEthernet0/5      sw2
00:C5:B3:7E:9B:60  10.1.5.40         5     FastEthernet0/9      sw2
00:A9:BC:3F:A6:50  100.1.1.6         3     FastEthernet0/20     sw3

$ python get_data.py ip 10.1.10.2

Detailed information for host(s) with ip 10.1.10.2
----------------------------------------
mac         : 00:09:BB:3D:D6:58
vlan        : 10
interface   : FastEthernet0/1
switch      : sw1
----------------------------------------


$ python get_data.py vlan 10

Detailed information for host(s) with vlan 10
----------------------------------------
mac         : 00:09:BB:3D:D6:58
ip          : 10.1.10.2
interface   : FastEthernet0/1
switch      : sw1
----------------------------------------
mac         : 00:07:BC:3F:A6:50
ip          : 10.1.10.6
interface   : FastEthernet0/3
switch      : sw1
----------------------------------------
mac         : 00:A9:BB:3D:D6:58
ip          : 10.1.10.20
interface   : FastEthernet0/7
switch      : sw2
----------------------------------------

$ python get_data.py vlan
Пожалуйста, введите два или ноль аргументов
'''
