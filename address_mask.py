#!/usr/bin/env python3

#Input CIDR
strNetworkAddressMask = input('Network Input: ')

#Split Network & Mask
listNetworkAddressMask = strNetworkAddressMask.split('/')
strNetworkAddress = listNetworkAddressMask[0]
strMask = listNetworkAddressMask[1]

#Make list of host address
listNetworkOctetsString = strNetworkAddress.split('.')
listNetworkOctetsDec = [int(octet) for octet in listNetworkOctetsString]

#Create list for decimal mask
intMaskDec = int(strMask)
listMask = [0,0,0,0]
for i in range(intMaskDec):
	listMask[i//8] = listMask[i//8] + (1 << (7 - i % 8))

# Initialize net and binary and netmask with addr to get network
listNetworkAddress = []
for i in range(4):
	listNetworkAddress.append(int(listNetworkOctetsDec[i]) & listMask[i])

#Print network
network_template = '''
    ...: Network:
    ...: {0:<8} {1:<8} {2:<8} {3:<8}
    ...: {0:08b} {1:08b} {2:08b} {3:08b}
    ...: '''
print(network_template.format(listNetworkAddress[0],listNetworkAddress[1],listNetworkAddress[2],listNetworkAddress[3]))

#Print mask
mask_template = '''
    ...: Mask:
	...: {4}
    ...: {0:<8} {1:<8} {2:<8} {3:<8}
    ...: {0:08b} {1:08b} {2:08b} {3:08b}
    ...: '''	
print(mask_template.format(listMask[0],listMask[1],listMask[2],listMask[3],intMaskDec))	
