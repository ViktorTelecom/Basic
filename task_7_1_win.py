#!/usr/bin/env python

listKeys = ['Protocol:', 'Prefix:', 'AD/Metric:', 'Next-Hop:', 'Last update:', 'Outbound Interface:']

with open('ospf.txt', 'r') as file:
	for strLine in file:
		strLineCorrected = strLine.replace(',','').replace('[','').replace(']','').replace('via','').replace('O','OSPF')
		#strLineCorrected = strLine.strip(',')
		listLine = strLineCorrected.split()
		dictResult = dict(zip(listKeys,listLine))
		print('-----------------------\n')
		
		for strKey, strValue in dictResult.items():
			print('{:<20}  {:<20} '.format(strKey, strValue))
			#print('{}  {} \n').format(strKey, strValue)
		

