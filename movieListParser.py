import re

class RegExHelper(object):
  def __init__(self, matchstring):
    self.matchstring = matchstring

  def match(self,regexp):
    self.rematch = re.match(regexp, self.matchstring)
    return bool(self.rematch)

  def group(self,i):
    if self.rematch.group(i) is None :
      return ""
    else:
      return self.rematch.group(i)


file = open("/home/destan/Desktop/movies.list")
outputFile = open("/home/destan/Desktop/movies.out", "w")
counter = 0

for line in file:
  matcher = RegExHelper(line)
  isMatch = matcher.match("(.*?) (\(\S{4,}\))( \(.*\))?\s?(\{(\{.*?\})?.*?(\(.*\))?\})?\s*(.*$)")
  if(isMatch):
    outputFile.write(matcher.group(1) + "," + matcher.group(2) + "," + matcher.group(3) + "," + matcher.group(4) + "," + matcher.group(5) + "," + matcher.group(6) + "," + matcher.group(7) + "\n")
  # print "Line " + str(counter) + ": " + line + "\n"
  # counter += 1
  # if(counter > 100):
  #   outputFile.flush()
  #   exit()
