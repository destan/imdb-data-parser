import time
from ..utils.Utils import *

startTime = time.time()

file = open("/home/destan/Desktop/movies.list")
outputFile = open("/home/destan/Desktop/movies.out", "w")
counter = 0
fuckedUpCount = 0

for line in file:
  matcher = RegExHelper(line)
  isMatch = matcher.match("(.*?) (\(\S{4,}\))( \(.*\))?\s?(\{(\{.*?\})?.*?(\(.*\))?\})?\s*(.*$)")
  if(isMatch):
    outputFile.write(matcher.group(1) + "," + matcher.group(2) + "," + matcher.group(3) + "," + matcher.group(4) + "," + matcher.group(5) + "," + matcher.group(6) + "," + matcher.group(7) + "\n")
  else:
    print "This line is fucked up: " + line
    fuckedUpCount += 1

outputFile.flush()
outputFile.close()
file.close()

print "Finished with " + str(fuckedUpCount) + " fucked up line\n"
print "Duration: " + str(round(time.time() - startTime))