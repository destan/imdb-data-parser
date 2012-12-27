import time
from ..utils.Utils import *

startTime = time.time()

file = open("/home/destan/Desktop/plot.list")
outputFile = open("/home/destan/Desktop/plot.out", "w")
counter = 0
fuckedUpCount = 0

title = ""
plot = ""

for line in file:
  matcher = RegExHelper(line)
  isMatch = matcher.match("(.+): (.*)")
  if(isMatch):
  	if(matcher.group(1) == "MV"): #Title
  		//TODO: reset plot, set title, write previous to file
  	elif(matcher.group(1) == "MV"): #Descriptive text
  		//TODO add to plot
  	else:
  		//ERROR write to console
  else:
  	#just ignore this part, useless
  
  outputFile.write(title + "," + plot + "\n")
  
outputFile.flush()
outputFile.close()
file.close()

print "Finished with " + str(fuckedUpCount) + " fucked up line\n"
print "Duration: " + str(round(time.time() - startTime))