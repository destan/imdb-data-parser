from abc import *

class BaseParser(metaclass=ABCMeta):
    """Common methods for all parser classes"""

    @abstractmethod
    def parseIntoTSV(self):
        raise NotImplemented

    @abstractmethod
    def parseIntoDB(self):
        raise NotImplemented

    def startProcessing(self, preferencesMap):
        if(preferencesMap["type"] == "tsv"):
            self.parseIntoTSV()

    @abstractproperty
    def baseMatcherPattern(self):
        raise NotImplemented

    @abstractproperty
    def inputFileName(self):
        raise NotImplemented

    @abstractproperty
    def numberOfLinesToBeSkipped(self):
        raise NotImplemented