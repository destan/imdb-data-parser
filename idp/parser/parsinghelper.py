from idp import settings

class ParsingHelper(object):
    """ParsingHelper manages parsing order"""

    @staticmethod
    def parse_all(preferencesMap):

        def get_parser_class_for( itemName ):
            """
            Thanks to http://stackoverflow.com/a/452981
            """
            kls = "idp.parser." + itemName + "parser." + itemName.title() + "Parser"
            parts = kls.split('.')
            module = ".".join(parts[:-1])
            m = __import__( module )
            for comp in parts[1:]:
                m = getattr(m, comp)            
            return m

        for item in settings.LISTS:
            try:
                ParserClass = get_parser_class_for(item)
            except Exception as e:
                print ("No parser found for: " + item + "\n\tException is: " + e.value)
                continue
            print("Parsing " + item + "...")
            parser = ParserClass(preferencesMap)
            parser.start_processing()
        print("Parsing finished.")