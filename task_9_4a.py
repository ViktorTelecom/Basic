#!/usr/bin/env python

from pprint import pprint

ignore = ['duplex', 'alias', 'Current', 'configuration']

def ignore_command(command, ignore):
    return any(word in command for word in ignore)
	

		
def file_to_dictionary(filename):
	"""Task 9_4"""
	
	strMainCommand = ''
	
	listInferiorCommands = []
	listThirdLevelCommands = []
	dictOutput = {}
	bThirdLevel = False
				
				
	with open(filename) as file:
		for strLine in file:
			bFoundIllegal = False
			listWordsInString = strLine.split()
			for strWord in listWordsInString:										# ! or ignored words have been found ---> stop processing the string and go to the next string						
				if strWord.find('!') > -1 or ignore_command(strWord,ignore):
					bFoundIllegal = True
			if 	bFoundIllegal:
				continue	
			if 	strLine.startswith('  '):
				bThirdLevel = True
				listThirdLevelCommands.append(strLine.strip())
			elif strLine.startswith(' '):											# string starts with ' ' ---> subordinate string ---> add the string to the 'subordinate' list
				listInferiorCommands.append(strLine.strip())
			else:																# string start with ordinary command ---> main command ---> push record with earlier recorded 'subordinate' list and 'main' string to the dictionary
				if len(strMainCommand) > 1:
					if bThirdLevel:
						strLastSecondLevelCommand = listInferiorCommands.pop(-1)
						dictSecondLevel = {key : [] for key in listInferiorCommands}
						dictSecondLevel.update({strLastSecondLevelCommand : listThirdLevelCommands})
						dictOutput.update({strMainCommand : dictSecondLevel})
						listThirdLevelCommands = []
						bThirdLevel = False
					else:	
						dictOutput.update({strMainCommand : listInferiorCommands})
				listInferiorCommands = []
				strMainCommand = strLine.strip()								# set this main command to 'main' string
				if strMainCommand == 'end':
					break														# if 'end' is found ---> exit for

	return dictOutput

strResult = file_to_dictionary('config_sw10.txt')

pprint(strResult)
