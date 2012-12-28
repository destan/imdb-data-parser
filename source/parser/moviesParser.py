"""
RegExp: /(.*?) (\(\S{4,}\))( \(.*\))?\s?(\{.+?\})?\s*(\{\{SUSPENDED\}\})?\s*(.*$)/gm
pattern: (.*?) (\(\S{4,}\))( \(.*\))?\s?(\{.+?\})?\s*(\{\{SUSPENDED\}\})?\s*(.*$)
flags: gm
6 capturing groups: 
   group 1: (.*?)                               title
   group 2: (\(\S{4,}\))                        year
   group 3: ( \(.*\))                           type ex:(TV)
   group 4: (\{.+?\})                           series info ex: {Ally Abroad (#3.1)}
   group 5: (\{\{SUSPENDED\}\})                 is suspended?
   group 6: (.*$)                               year

"""

import time
from ..utils.Utils import *

startTime = time.time()

file = open("/home/destan/Desktop/movies.list")
outputFile = open("/home/destan/Desktop/movies.out", "w")
counter = 0
fuckedUpCount = 0
matcherPattern = "(.*?) (\(\S{4,}\))( \(.*\))?\s?(\{.+?\})?\s*(\{\{SUSPENDED\}\})?\s*(.*$)"
episodeMatcherPattern = "\{.+?(\(.*\))?\}"

for line in file:
  matcher = RegExHelper(line)
  isMatch = matcher.match(matcherPattern)

  if(isMatch):
    processedType = matcher.group(3)

    # Check if SUSPENDED is correctly placed
    if(matcher.group(3) == "{{SUSPENDED}}"):
        processedType = ""

    outputFile.write(matcher.group(1) + "," + matcher.group(2) + "," + processedType + "," + matcher.group(4) + "," + matcher.group(5) + "," + matcher.group(6) + "\n")
  else:
    print "This line is fucked up: " + line
    fuckedUpCount += 1

outputFile.flush()
outputFile.close()
file.close()

print "Finished with " + str(fuckedUpCount) + " fucked up line\n"
print "Duration: " + str(round(time.time() - startTime))