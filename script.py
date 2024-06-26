import re
import interpreter

class Script:
    def __init__(self, file=None):
        self.file = file
        self.variables = {}
        self.redefines = {}

    def run(self, code=None):
        body = ""
        lines = None

        if code is not None:
            lines = code.split("\n")
        elif self.file is not None:
            print()
            print(" $> fangs {}".format(self.file.name))
            print()
            lines = self.file
        else:
            print(" $> No code or file provided")
            return

        for line in lines:
            # Strip and ignore empty lines
            line = line.rstrip("\n")
            if line == "" or line.lstrip().startswith("//"): 
                continue
            elif line == "" or line.lstrip().startswith("##"): 
                continue
            elif line.startswith("#r"):
                # Handle metatags
                self.__handle_metatag(line[1:])
                continue
            # elif line.startswith("#i"):
            #     # Handle metatags
            #     imp, as_imp = self.__handle_import(line[1:])
            #     #print(f"{imp} --> {as_imp}")
            #     continue
            # Continue to form body
            body += line

        for key, value in self.redefines.items():
            body = re.sub(re.escape(key) + '+(?=([^"]*"[^"]*")*[^"]*$)', value, body)

        # From body remove all spaces that aren't between quotes
        body = re.sub(r'\s+(?=([^"]*"[^"]*")*[^"]*$)', '', body)
        return interpreter.parse(self, body)

    def __handle_metatag(self, tag):
        if tag.startswith("redefine"):
            tagArgs = tag.split(' ')

            if tagArgs[1].startswith('"'):
                index = tag.find('"', 1)
                index2 = tag.find('"', index + 1)
                key = tag[index + 1:index2]
                self.redefines[key] = tag[index2 + 2:]
            else:
                self.redefines[tagArgs[1]] = " ".join(tagArgs[2:])           
              
    # def __handle_import(self, tag):
    #     if tag.startswith("import"):
    #         asArgs = tag.split('as')

    #         # Initialize variables
    #         import_value = alias_value = None

    #         # Check if the import statement includes the 'as' keyword
    #         if len(asArgs) > 1:
    #             # Extract parts around 'as'
    #             import_part = asArgs[0].strip()
    #             alias_part = asArgs[1].strip()

    #             if import_part.startswith('import'):
    #                 import_string = import_part.split(' ', 1)[1].strip()
    #                 if import_string.startswith('"') and import_string.endswith('"'):
    #                     import_value = import_string[1:-1]

    #             if alias_part.startswith('"') and alias_part.endswith('"'):
    #                 alias_value = alias_part[1:-1]

    #             # Assuming redefines is a dictionary where you store your import aliases
    #             if import_value is not None and alias_value is not None:
    #                 self.redefines[import_value] = alias_value
    #                 #print(f"importing ({import_value}) ({alias_value})")
    #                 return [import_value, alias_value]
    #             else:
    #                 print("Error: Unable to parse import statement correctly.")
    #                 return []
    #         else:
    #             print("Error: Import statement does not include 'as' keyword.")
    #             return []


