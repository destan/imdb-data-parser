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