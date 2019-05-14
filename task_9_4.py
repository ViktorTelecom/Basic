#!/usr/bin/env python

from pprint import pprint

ignore = ['duplex', 'alias', 'Current', 'configuration']

def ignore_command(command, ignore):
    return any(word in command for word in ignore)
	

		
def file_to_dictionary(filename):
	"""Task 9_4"""
	
	strMainCommand = ''
	
	listInferiorCommands = []
	dictOutput = {}
	
	with open(filename) as file:
		for strLine in file:
			bFoundIllegal = False
			#strLine.strip()
			listWordsInString = strLine.split()
			for strWord in listWordsInString:										# ! or ignored words have been found ---> stop processing the string and go to the next string						
				if strWord.find('!') > -1 or ignore_command(strWord,ignore):
					bFoundIllegal = True
			if 	bFoundIllegal:
				continue	
			if strLine.startswith(' '):											# string starts with ' ' ---> subordinate string ---> add the string to the 'subordinate' list
				listInferiorCommands.append(strLine.strip())
			else:																# string start with ordinary command ---> main command ---> push record with earlier recorded 'subordinate' list and 'main' string to the dictionary
				if len(strMainCommand) > 1:
					dictOutput.update({strMainCommand : listInferiorCommands})
				listInferiorCommands = []
				#listInferiorCommands.clear()									# clear 'subordinate' list for future use
				strMainCommand = strLine.strip()								# set this main command to 'main' string
				if strMainCommand == 'end':
					break														# if 'end' is found ---> exit for

	return dictOutput

strResult = file_to_dictionary('config_sw10.txt')

pprint(strResult)
