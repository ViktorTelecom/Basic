#!/usr/bin/env python

bIpCorrect = False

while not bIpCorrect:
	bBadOctetDetected = False
	strIpAddr = input ('Enter IP Address: ')
	#print(strIpAddr)
	listIpAddressStr = strIpAddr.split('.')
	listNetworkOctetsDec = [int(octet) for octet in listIpAddressStr if octet.isdigit()]
	print(listNetworkOctetsDec)
	
	for i in range(4):
		try:
			if isinstance(listNetworkOctetsDec[i],int) & listNetworkOctetsDec[i] < 255:
				pass
			else:
				print ('Incorrect IP')
				bBadOctetDetected = True
				break
		except IndexError:
				print ('Incorrect IP')
				bBadOctetDetected = True
				break
				
	if not bBadOctetDetected:
		bIpCorrect = True	
		
iFirstOctet = listNetworkOctetsDec[0]


if iFirstOctet < 128:
	strClassIp = 'A'
elif iFirstOctet < 192:
	strClassIp = 'B'
elif iFirstOctet < 224:
	strClassIp = 'C'
elif iFirstOctet < 240:
	strClassIp = 'D'
else:
	strClassIp = 'Undefined'
	
print('IP Address Class: {}'.format(strClassIp))