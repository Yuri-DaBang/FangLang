from time import sleep
import json
import interpreter
import requests
import os
import random
from colors import Colors
import string

class IMPORT:
    def success(script, args):
        import_statement = args[0]
    
        if type(import_statement) is str:
            import_statement = interpreter.resolveString(script, import_statement)
        else:
            import_statement = str(import_statement)

        
        asArgs = import_statement.split('as')

        # Initialize variables
        import_value = alias_value = None

        # Check if the import statement includes the 'as' keyword
        if len(asArgs) > 1:
            # Extract parts around 'as'
            import_part = asArgs[0].strip()
            alias_part = asArgs[1].strip()

            if import_part.startswith('import'):
                import_string = import_part.split(' ', 1)[1].strip()
                if import_string.startswith('"') and import_string.endswith('"'):
                    import_value = import_string[1:-1]

            if alias_part.startswith('"') and alias_part.endswith('"'):
                alias_value = alias_part[1:-1]

            # Assuming redefines is a dictionary where you store your import aliases
            if import_value is not None and alias_value is not None:
                self.redefines[import_value] = alias_value
                #print(f"importing ({import_value}) ({alias_value})")
                return [import_value, alias_value]
            else:
                print("Error: Unable to parse import statement correctly.")
                return []
        else:
            print("Error: Import statement does not include 'as' keyword.")
            return []