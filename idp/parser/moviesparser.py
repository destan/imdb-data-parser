from .baseparser import BaseParser
from ..utils.regexhelper import *
from ..utils.databasehelper import DatabaseHelper
import logging

class MoviesParser(BaseParser):
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
  
    createTableSql = """CREATE TABLE movies
                    (
                      imdb_id character varying,
                      title character varying,
                      type character varying,
                      year character varying,
                      is_suspended character varying,
                      episode_name character varying,
                      episode_session_number character varying,
                      episode_number character varying,
                      imdb_title character varying NOT NULL,
                      CONSTRAINT movies_pkey PRIMARY KEY (imdb_title )
                    )
                    WITH (
                      OIDS=FALSE
                    );
                    ALTER TABLE movies
                      OWNER TO imdbuser;
                    """

    insertSql = """INSERT INTO movies(
                            imdb_title, imdb_id, title, type, year, is_suspended, episode_name, episode_session_number, 
                            episode_number)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, 
                            %s, %s);
                """

    # properties
    baseMatcherPattern = "(.*?) (\(\S{4,}\))\s?(\(.+\))?\s?(\{(.*?)(\(.+?\))\})?\s*(\{\{SUSPENDED\}\})?\s*(.*$)"
    inputFileName = "movies.list"
    numberOfLinesToBeSkipped = 14

    def _BaseParser__iterate(self):
        import time

        startTime = time.time()

        inputFile = self.get_input_file()
        if(self.mode == "TSV"):
            outputFile = self.get_output_file()
        elif(self.mode == "SQL"):
            databaseHelper = DatabaseHelper()
            databaseHelper.execute("DROP TABLE IF EXISTS movies")
            databaseHelper.execute(self.createTableSql)

        counter = 0
        fuckedUpCount = 0
        numberOfProcessedLines = 0

        for line in inputFile :
            if(numberOfProcessedLines > self.numberOfLinesToBeSkipped):
                matcher = RegExHelper(line)
                isMatch = matcher.match(self.baseMatcherPattern)

                if(isMatch):
                    if(self.mode == "TSV"): # write to text file (TSV)
                        outputFile.write(matcher.group(1) + "," + matcher.group(2) + "," + matcher.group(3) + "," + matcher.group(5) + "," + matcher.group(6) + "," + matcher.group(7) + "," + matcher.group(8) + "\n")
                    elif(self.mode == "SQL"): # write to DB
                        databaseHelper.execute_with_params(self.insertSql, (
                            matcher.group(1) + matcher.group(2) + matcher.group(4) + matcher.group(8) ,
                            matcher.group(1),
                            matcher.group(1),
                            matcher.group(1),
                            matcher.group(1),
                            matcher.group(1),
                            matcher.group(1),
                            matcher.group(1),
                            matcher.group(1)
                        ))
                else:
                    logging.critical("This line is fucked up: " + line)
                    fuckedUpCount += 1
            numberOfProcessedLines +=  1

        if 'outputFile' in locals():
            outputFile.flush()
            outputFile.close()
        inputFile .close()

        if 'databaseHelper' in locals():
            databaseHelper.commit()
            databaseHelper.close()

        logging.info("Finished with " + str(fuckedUpCount) + " fucked up line\n")
        logging.info("Duration: " + str(round(time.time() - startTime)))
