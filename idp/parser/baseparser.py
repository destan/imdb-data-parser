from abc import *
from ..utils.filehandler import *

class BaseParser(metaclass=ABCMeta):
    """Common methods for all parser classes"""

    seperator = "\t"
    mode = "INVALID"

    def start_processing(self, preferencesMap):
        if(preferencesMap["mode"] == "TSV" or preferencesMap["mode"] == "SQL"):
            self.mode = preferencesMap["mode"]
        else:
            raise NotImplemented("Mode: " + preferencesMap["mode"])
        self.__iterate()

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
