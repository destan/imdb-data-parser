from abc import *

class BaseParser(metaclass=ABCMeta):
    """Common methods for all parser classes"""

    @abstractmethod
    def parseIntoTSV(self):
        raise NotImplemented

    @abstractmethod
    def parseIntoDB(self):
        raise NotImplemented

    def startProcessing(self):
        if(self.preferencesMap["mode"] == "TSV"):
            self.parseIntoTSV()
        elif(self.preferencesMap["mode"] == "SQL"):
            self.parseIntoDB()
        else:
            raise NotImplemented("Mode: " + self.preferencesMap["mode"])

    @abstractproperty
    def baseMatcherPattern(self):
        raise NotImplemented

    @abstractproperty
    def inputFileName(self):
        raise NotImplemented

    @abstractproperty
    def numberOfLinesToBeSkipped(self):
        raise NotImplemented

    @abstractproperty
    def preferencesMap(self):
        raise NotImplemented