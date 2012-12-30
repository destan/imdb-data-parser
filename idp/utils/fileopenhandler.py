import gzip
import os.path

def openfile(inputFileName):

	print("Trying to find file:", inputFileName)
	if os.path.isfile(inputFileName):
		print("File found:", inputFileName)
		return open(inputFileName, "r", encoding='iso-8859-1')
	print("File cannot be found:", inputFileName)

#
#this part removed until python 3.3 becomes available for ubuntu LTS and debian
#
#inputFileName += ".gz"
#print("Trying to find file:", inputFileName)
#if os.path.isfile(inputFileName):
#	print("File found:", inputFileName)
#	return gzip.open(inputFileName, 'rt')
#print("File cannot be found:", inputFileName)

	raise FileNotFoundError