#!/usr/bin/env python


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def create_db (db_filename,schema_filename):	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	Creating/opening DB file


	db_exists = os.path.exists(db_filename)

	conn = sqlite3.connect(db_filename)
	cursor = conn.cursor()

	if not db_exists:
		print('Creating schema...')
		with open(schema_filename, 'r') as f:
			schema = f.read()
		conn.executescript(schema)
		print('Done')
	else:
		print('Database exists, assume dhcp table does, too.')
	
return

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def add_data_switches(db_filename, yamlInputData):			#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	Read switches info from yaml; add info to DB

	conn = sqlite3.connect(db_filename)
	cursor = conn.cursor()

	with open(yamlInputData) as file:
		dictSwitchData = yaml.load(file)
	listSwitchData = []

	for switchdata in dictSwitchData.values():
		for hostname,address in switchdata.items():
			tupleSwitchItem = (hostname,address)
			listSwitchData.append(tupleSwitchItem)

	query = "replace into switches values (?, ?)"

	cursor.executemany(query, listSwitchData)
	conn.commit()

	conn.close()

return

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def add_data(db_filename,dhcp_snooping_files):						#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	Read DHCP info from show ip dhcp outputs; add info to DB

	dhcp_snooping_list = []
	
	with open(dhcp_snooping_files, 'r') as file:
		for strLine in file:
			dhcp_snooping_list.append(strLine.rstrip())
	
	
	listResult = []

	for strFileName in dhcp_snooping_list:
		strHostname = re.search(regHostname,strFileName).group(1)
		with open(strFileName) as data:
			for line in data:
				match = regex.search(line)
				if match:
					listTempResult = list(match.groups())
					listTempResult.append(strHostname)
					listTempResult.append('1')
					listTempResult.append(now)	
					listResult.append(tuple(listTempResult))


	print('Inserting DHCP Snooping data')

	conn = sqlite3.connect(db_filename)
	cursor = conn.cursor()

	cursor.execute("update dhcp set active = 0")

	for row in listResult:
		try:
			#print(row[0])
			query = '''replace into dhcp (mac, ip, vlan, interface, switch, active, last_active)
						values (?, ?, ?, ?, ?, ?, ?)'''
			cursor.execute(query, row)
		except sqlite3.IntegrityError as e:
			print('Error occured: ', e)


	iterResult = cursor.execute("select * from dhcp where active = 0")

	listLateDates = []

	for row in iterResult:
		#print(row[6])
		if week_ago > datetime.strptime(row[6], '%Y-%m-%d %H:%M:%S'):
			listLateDates.append(row[6])

	for row in listLateDates:
		iterResult = cursor.execute("select * from dhcp where active = 0")
		cursor.execute("delete from dhcp where last_active = ?",(row,))
		
	conn.commit()

	conn.close()

return

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_data(key,value,db_filename):

	
	keys = ['mac', 'ip', 'vlan', 'interface' , 'switch', 'active', 'last_active']
	
	if key in keys:
		keys.remove(key)
	else:
		print('Данный параметр не поддерживается.')
		print('Допустимые значения параметров: mac, ip, vlan, interface, switch, active, last_active')
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

	print('Active Values:')
	print('-' * 60)
	for row in result_active:
		for k in keys:
			print('{:12}: {}'.format(k, row[k]))
		print('-' * 60)


	print('Inactive Values:')
	print('-' * 60)
	for row in result_inactive:
		for k in keys:
			print('{:12}: {}'.format(k, row[k]))
		print('-' * 60)
		
return

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
def get_all_data(db_filename):

	conn = sqlite3.connect(db_filename)
	print('\nВ таблице dhcp такие записи:')
	print('-' * 60)
	
	query_active = 'select * from dhcp where active = 1'
	query_inactive = 'select * from dhcp where active = 0'
	
	result_active = conn.execute(query_active).fetchall()
	result_inactive = conn.execute(query_inactive).fetchall()
	
	print('Active Values:')
	print('-' * 60)
	for row in result_active:
		mac, ip, vlan, interface, switch, active, last_active = row
		print ('{:18}  {:16}  {:6}  {:16}  {:6}  {:3}'.format(mac, ip, vlan, interface, switch, active, last_active))

	print('Inactive Values:')
	print('-' * 60)
	for row in result_inactive:
		mac, ip, vlan, interface, switch, active = row
		print ('{:18}  {:16}  {:6}  {:16}  {:6}  {:3}'.format(mac, ip, vlan, interface, switch, active, last_active))
		
	print()	
	
return

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



