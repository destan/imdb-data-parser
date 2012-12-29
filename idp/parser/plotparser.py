import time
from ..utils.regexhelper import *

startTime = time.time()

file = open("/home/destan/Desktop/plot.list")
outputFile = open("/home/destan/Desktop/plot.out", "w")
counter = 0
fuckedUpCount = 0

matcherPattern = "(.+?): (.*)"
seperator = "\t"

title = ""
plot = ""

for line in file:
    matcher = RegExHelper(line)
    isMatch = matcher.match(matcherPattern)

    if(isMatch):
        if(matcher.group(1) == "MV"): #Title
            if(title != ""):
                outputFile.write(title + seperator + plot + "\n")

            plot = ""
            title = matcher.group(2)

        elif(matcher.group(1) == "PL"): #Descriptive text
            plot += matcher.group(2)
        elif(matcher.group(1) == "BY"):
            continue
        else:
            print("Unhandled abbreviation: " + matcher.group(1) + " in " + line)
    #else:
        #just ignore this part, useless lines
  
# Covers the last item
outputFile.write(title + seperator + plot + "\n")
  
outputFile.flush()
outputFile.close()
file.close()

print("Finished with " + str(fuckedUpCount) + " fucked up line\n")
print("Duration: " + str(round(time.time() - startTime)))