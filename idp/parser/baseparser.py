from abc import *
from ..utils.filehandler import *

class BaseParser(metaclass=ABCMeta):
    """Common methods for all parser classes"""

    @abstractmethod
    def parse_into_tsv(self):
        raise NotImplemented

    @abstractmethod
    def parse_into_db(self):
        raise NotImplemented

    def start_processing(self):
        if(self.preferencesMap["mode"] == "TSV"):
            self.parse_into_tsv()
        elif(self.preferencesMap["mode"] == "SQL"):
            self.parse_into_db()
        else:
            raise NotImplemented("Mode: " + self.preferencesMap["mode"])

    def get_input_file(self):
        return openfile(get_full_path(self.inputFileName))

    def get_output_file(self):
        return open(get_full_path_for_tsv(self.inputFileName), "w")

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