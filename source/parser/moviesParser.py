"""
RegExp: /(.*?) (\(\S{4,}\))\s?(\(.+\))?\s?(\{(.*?)(\(.+?\))\})?\s*(\{\{SUSPENDED\}\})?\s*(.*$)/gm
pattern: (.*?) (\(\S{4,}\))\s?(\(.+\))?\s?(\{(.*?)(\(.+?\))\})?\s*(\{\{SUSPENDED\}\})?\s*(.*$)
flags: gm
6 capturing groups: 
   group 1: (.*?)                               title
   group 2: (\(\S{4,}\))                        year
   group 3: (\(.+\))                            type ex:(TV)
   group 4: (\{(.*?)(\(.+?\))\})                series info ex: {Ally Abroad (#3.1)}
   group 5: (.*?)                               episode name ex: Ally Abroad
   group 6: (\(.+?\))                           episode number ex: (#3.1)
   group 7: (\{\{SUSPENDED\}\})                 is suspended?
   group 8: (.*$)                               year

"""

import time
from ..utils.Utils import *

startTime = time.time()

file = open("/home/destan/Desktop/movies.list")
outputFile = open("/home/destan/Desktop/movies.out", "w")
counter = 0
fuckedUpCount = 0
matcherPattern = "(.*?) (\(\S{4,}\))\s?(\(.+\))?\s?(\{(.*?)(\(.+?\))\})?\s*(\{\{SUSPENDED\}\})?\s*(.*$)"

for line in file:
  matcher = RegExHelper(line)
  isMatch = matcher.match(matcherPattern)

  if(isMatch):
    outputFile.write(matcher.group(1) + "," + matcher.group(2) + "," + matcher.group(3) + "," + matcher.group(5) + "," + matcher.group(6) + "," + matcher.group(7) + "," + matcher.group(8) + "\n")
  else:
    print "This line is fucked up: " + line
    fuckedUpCount += 1

outputFile.flush()
outputFile.close()
file.close()

print "Finished with " + str(fuckedUpCount) + " fucked up line\n"
print "Duration: " + str(round(time.time() - startTime))
