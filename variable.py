from enum import Enum

class Modifier(Enum):
    NONE = 0
    OWO = 1
    ONO = 2
    Fixed = 3
    ReadOnly = 4

    List = 14
    Dict = 15
    
    string = 5   # "hallo i is a string"
    integer = 6  # 79934555

    num    = 7   # 3   (only one number)
    char   = 8   # d   (only one character)
    
    VARf    = 8  # float
    VARd    = 9  # double
    
    vbool   = 10 #bool value [TRUE , FALSE]  
    vyon    = 11 #yes or no value [YES,NO]  
    vzoo    = 12 #zero or one value [0,1]  
    
    var     = 13

class Variable:
    def __init__(self, name, value, modifier):
        self.name = name
        self.value = value
        self.modifier = modifier

