import gzip
import os.path

def openfile(inputDir, inputFileName):

	absPath = inputDir + inputFileName

	print("Trying to find file:", absPath)
	if os.path.isfile(absPath):
		print("File found:", absPath)
		return open(absPath, "r", encoding='iso-8859-1')

	print("File cannot be found:", absPath)

#
#this part removed until python 3.3 becomes available for ubuntu LTS and debian
#
#	print("Trying to find file:", absPath)
#	if os.path.isfile(absPath):
#		print("File found:", absPath)
#		return gzip.open(absPath, 'rt')
#	print("File cannot be found:", absPath)

	print("Trying to find file:", absPath + ".gz")
	if os.path.isfile(absPath + ".gz"):
		print("File found:", absPath + ".gz")
		if extract(inputDir, inputFileName) == 0:
			return open(absPath, "r", encoding='iso-8859-1')
		else:
			raise RuntimeError("Unknown error occured")
	print("File cannot be found:", absPath + ".gz")

	raise FileNotFoundError


def extract(inputDir, inputFileName):

	absPath = inputDir + inputFileName

	try:
		print("Started to extract file:", absPath + ".gz")
		with gzip.open(absPath + ".gz", "rb") as f:
			file_content = f.read()
		file = open(inputDir + inputFileName, "wb")
		file.write(file_content)
		file.close()
		print("File extracted successfully", inputFileName)
	except:
		print("Error when extracting file:", absPath + ".gz")
		return 1
	return 0