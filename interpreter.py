from turtle import left
from variable import Variable, Modifier
import re
import methods
import json
import numexpr as ne

methodMap = {
    #"bark": methods.bark,
    #"paw": methods.paw,
    #"sweep": methods.sweep,
    "eat": methods.bite,
    "prompt": methods.pwompt,
    "fetch": methods.fetch,
    "fetchjson": methods.fetchjson,
    "stash": methods.stash,
    "wandom": methods.wandom,

    "panic.error": methods.panic.error,
    "panic.warning": methods.panic.warning,    

    "type": methods.type,    

    "add": methods.paw,

    "thread.sleep": methods.sweep,

    "console.input": methods.pwompt,
    "console.println": methods.console.println,
    "console.raise.success": methods.console.output.success,
    "console.raise.error": methods.console.output.error,
    "console.raise.warn": methods.console.output.warning,
    "console.raise.output": methods.console.output.output,

    # MathPhysics Calculations
    "math.add": methods.MathPhysics.Calculations.add,
    "math.subtract": methods.MathPhysics.Calculations.subtract,
    "math.multiply": methods.MathPhysics.Calculations.multiply,
    "math.divide": methods.MathPhysics.Calculations.divide,
    "math.power": methods.MathPhysics.Calculations.power,
    "math.sqrt": methods.MathPhysics.Calculations.sqrt,
    "math.factorial": methods.MathPhysics.Calculations.factorial,

    "math.sine": methods.MathPhysics.Calculations.sine,
    "math.cosine": methods.MathPhysics.Calculations.cosine,
    "math.tangent": methods.MathPhysics.Calculations.tangent,
    "math.arcsine": methods.MathPhysics.Calculations.arcsine,
    "math.arccosine": methods.MathPhysics.Calculations.arccosine,
    "math.arctangent": methods.MathPhysics.Calculations.arctangent,
    "math.sinh": methods.MathPhysics.Calculations.sinh,
    "math.cosh": methods.MathPhysics.Calculations.cosh,
    "math.tanh": methods.MathPhysics.Calculations.tanh,

    "math.log": methods.MathPhysics.Calculations.log,
    "math.log10": methods.MathPhysics.Calculations.log10,
    "math.log2": methods.MathPhysics.Calculations.log2,
    "math.exp": methods.MathPhysics.Calculations.exp,

    "math.distance": methods.MathPhysics.Calculations.distance,
    "math.circle_area": methods.MathPhysics.Calculations.circle_area,
    "math.rectangle_area": methods.MathPhysics.Calculations.rectangle_area,
    "math.triangle_area": methods.MathPhysics.Calculations.triangle_area,
    "math.sphere_volume": methods.MathPhysics.Calculations.sphere_volume,
    "math.cylinder_volume": methods.MathPhysics.Calculations.cylinder_volume,
    "math.cone_volume": methods.MathPhysics.Calculations.cone_volume,

    "math.mean": methods.MathPhysics.Calculations.mean,
    "math.median": methods.MathPhysics.Calculations.median,
    "math.mode": methods.MathPhysics.Calculations.mode,
    "math.variance": methods.MathPhysics.Calculations.variance,
    "math.standard_deviation": methods.MathPhysics.Calculations.standard_deviation,
    "math.correlation": methods.MathPhysics.Calculations.correlation,

    "math.derivative": methods.MathPhysics.Calculations.derivative,
    "math.integral": methods.MathPhysics.Calculations.integral,

    "physics.velocity": methods.MathPhysics.Calculations.velocity,
    "physics.acceleration": methods.MathPhysics.Calculations.acceleration,
    "physics.force": methods.MathPhysics.Calculations.force,
    "physics.kinetic_energy": methods.MathPhysics.Calculations.kinetic_energy,
    "physics.potential_energy": methods.MathPhysics.Calculations.potential_energy,
    "physics.momentum": methods.MathPhysics.Calculations.momentum,
    "physics.work": methods.MathPhysics.Calculations.work,
    "physics.power": methods.MathPhysics.Calculations.power_physics,
    "physics.pressure": methods.MathPhysics.Calculations.pressure,
    "physics.density": methods.MathPhysics.Calculations.density,
    "physics.circular_motion": methods.MathPhysics.Calculations.circular_motion,
    "physics.gravitational_force": methods.MathPhysics.Calculations.gravitational_force,
    "physics.ohms_law": methods.MathPhysics.Calculations.ohms_law,
    "physics.coulombs_law": methods.MathPhysics.Calculations.coulombs_law,
    "physics.buoyant_force": methods.MathPhysics.Calculations.buoyant_force,
    "physics.refraction": methods.MathPhysics.Calculations.refraction,
    "physics.doppler_effect": methods.MathPhysics.Calculations.doppler_effect,
    "physics.planck_energy": methods.MathPhysics.Calculations.planck_energy,
    "physics.einstein_mass_energy": methods.MathPhysics.Calculations.einstein_mass_energy,

    # Built-in math functions
    "math.fabs": methods.MathPhysics.Calculations.fabs,
    "math.ceil": methods.MathPhysics.Calculations.ceil,
    "math.floor": methods.MathPhysics.Calculations.floor,
    "math.fmod": methods.MathPhysics.Calculations.fmod,
    "math.gcd": methods.MathPhysics.Calculations.gcd,
    "math.isfinite": methods.MathPhysics.Calculations.isfinite,
    "math.isinf": methods.MathPhysics.Calculations.isinf,
    "math.isnan": methods.MathPhysics.Calculations.isnan,
    "math.degrees": methods.MathPhysics.Calculations.degrees,
    "math.radians": methods.MathPhysics.Calculations.radians,
    "math.copysign": methods.MathPhysics.Calculations.copysign,
    "math.comb": methods.MathPhysics.Calculations.comb,
    "math.perm": methods.MathPhysics.Calculations.perm,
    "math.ldexp": methods.MathPhysics.Calculations.ldexp,
    "math.frexp": methods.MathPhysics.Calculations.frexp,
    "math.modf": methods.MathPhysics.Calculations.modf,
    "math.trunc": methods.MathPhysics.Calculations.trunc,
    
    ################
    ### GRAPHICS ###
    ################

    "graphics.plot_3d": methods.GraphicsLibrary.plot_3d,
    "graphics.imshow": methods.GraphicsLibrary.imshow,
    "graphics.quiver": methods.GraphicsLibrary.quiver,
    "graphics.contour": methods.GraphicsLibrary.contour,
    "graphics.boxplot": methods.GraphicsLibrary.boxplot,
    "graphics.violinplot": methods.GraphicsLibrary.violinplot,
    "graphics.errorbar": methods.GraphicsLibrary.errorbar,
    "graphics.stem": methods.GraphicsLibrary.stem,
    "graphics.hexbin": methods.GraphicsLibrary.hexbin,
    "graphics.polar": methods.GraphicsLibrary.polar,
    "graphics.streamplot": methods.GraphicsLibrary.streamplot,
    "graphics.plot_date": methods.GraphicsLibrary.plot_date,
    "graphics.eventplot": methods.GraphicsLibrary.eventplot,
    "graphics.step": methods.GraphicsLibrary.step,
    "graphics.fill": methods.GraphicsLibrary.fill,
    "graphics.stackplot": methods.GraphicsLibrary.stackplot,
    "graphics.imshow_extent": methods.GraphicsLibrary.imshow_extent,
}


keyWords = ["try",   "if","else","elif",    "for","foreach","do",   "}", "fn"]

def parse(script, body):
    parsing = True

    while parsing:
        # Check for if statement
        if body.startswith('if'):
            index = findEndingIndex(body, 5)
            substring = body[:index]
            body = body[index:]

            # Parse condition and contents
            rightParenIndex = substring.find(')')
            leftContentIndex = substring.find('{')
            rightContentIndex = substring.find('}')

            condition = substring[substring.find('(') + 1:rightParenIndex]
            contents = substring[substring.find('{') + 1:rightContentIndex]

            # Define a helper function to evaluate a condition
            def evaluate_condition(condition, script):
                if "==" in condition:
                    splitCondition = condition.split('==')
                    leftSide = typeFromString(script, splitCondition[0])
                    rightSide = typeFromString(script, splitCondition[1])
                    return leftSide == rightSide

                elif "!=" in condition:
                    splitCondition = condition.split('!=')
                    leftSide = typeFromString(script, splitCondition[0])
                    rightSide = typeFromString(script, splitCondition[1])
                    return leftSide != rightSide

                elif ":=" in condition:
                    splitCondition = condition.split(':=')
                    leftSide = typeFromString(script, splitCondition[0])
                    rightSide = typeFromString(script, splitCondition[1])
                    return leftSide == rightSide

                elif ">=" in condition:
                    splitCondition = condition.split('>=')
                    leftSide = typeFromString(script, splitCondition[0])
                    rightSide = typeFromString(script, splitCondition[1])
                    return leftSide >= rightSide

                elif "<=" in condition:
                    splitCondition = condition.split('<=')
                    leftSide = typeFromString(script, splitCondition[0])
                    rightSide = typeFromString(script, splitCondition[1])
                    return leftSide <= rightSide

                elif ">" in condition:
                    splitCondition = condition.split('>')
                    leftSide = typeFromString(script, splitCondition[0])
                    rightSide = typeFromString(script, splitCondition[1])
                    return leftSide > rightSide

                elif "<" in condition:
                    splitCondition = condition.split('<')
                    leftSide = typeFromString(script, splitCondition[0])
                    rightSide = typeFromString(script, splitCondition[1])
                    return leftSide < rightSide

                elif " is " in condition:
                    splitCondition = condition.split(' is ')
                    leftSide = typeFromString(script, splitCondition[0])
                    rightSide = typeFromString(script, splitCondition[1])
                    return leftSide is rightSide

                elif " is not " in condition:
                    splitCondition = condition.split(' is not ')
                    leftSide = typeFromString(script, splitCondition[0])
                    rightSide = typeFromString(script, splitCondition[1])
                    return leftSide is not rightSide

                elif " in " in condition:
                    splitCondition = condition.split(' in ')
                    leftSide = typeFromString(script, splitCondition[0])
                    rightSide = resolveValue(script, splitCondition[1])
                    if isinstance(rightSide, list):
                        return leftSide in rightSide
                    else:
                        raise Exception(f"The second item must be a list, and {rightSide} is not a list")

                elif " not in " in condition:
                    splitCondition = condition.split(' not in ')
                    leftSide = typeFromString(script, splitCondition[0])
                    rightSide = resolveValue(script, splitCondition[1])
                    if isinstance(rightSide, list):
                        return leftSide not in rightSide
                    else:
                        raise Exception(f"The second item must be a list, and {rightSide} is not a list")

                else:
                    raise Exception("Invalid if statement")

            if evaluate_condition(condition, script):
                response = parse(script, contents)
                if response is not None:
                    return response

            # Handle elif and else statements
            while body.startswith('elif') or body.startswith('else'):
                if body.startswith('elif'):
                    index = findEndingIndex(body, 5)
                    substring = body[:index]
                    body = body[index:]

                    # Parse elif condition and contents
                    rightParenIndex = substring.find(')')
                    leftContentIndex = substring.find('{')
                    rightContentIndex = substring.find('}')

                    condition = substring[substring.find('(') + 1:rightParenIndex]
                    contents = substring[substring.find('{') + 1:rightContentIndex]

                    if evaluate_condition(condition, script):
                        response = parse(script, contents)
                        if response is not None:
                            return response
                elif body.startswith('else'):
                    index = findEndingIndex(body, 4)
                    substring = body[:index]
                    body = body[index:]

                    # Parse else contents
                    leftContentIndex = substring.find('{')
                    rightContentIndex = substring.find('}')

                    contents = substring[leftContentIndex + 1:rightContentIndex]

                    response = parse(script, contents)
                    if response is not None:
                        return response

            return None
        elif body.startswith("for"):
            index = findEndingIndex(body, 3)
            substring = body[:index - 3]
            body = body[index:]

            # Parse condition and contents
            rightParenIndex = substring.find(')')
            condition = substring[substring.find('(') + 1:rightParenIndex]
            contents = substring[rightParenIndex + 1:index]

            # Until for loop
            if 'untill' in condition:
                splitCondition = condition.split('untill')
                leftSide = typeFromString(script, splitCondition[0])
                rightSide = typeFromString(script, splitCondition[1])

                while leftSide != rightSide:
                    response = parse(script, contents)
                    if response is not None:
                        return response
                    leftSide = typeFromString(script, condition.split('untill')[0])
                    rightSide = typeFromString(script, condition.split('untill')[1])
            if 'in' in condition:
                splitCondition = condition.split('in')
                name = splitCondition[0][1:]
                script.variables[name] = Variable(name, None, Modifier.OWO)
                items = resolveValue(script, splitCondition[1])

                if type(items) is list:
                    for item in items:
                        script.variables[name].value = item
                        response = parse(script, contents)
                        if response is not None:
                            return response
                del script.variables[name]
        elif body.startswith("do"):
            index = findEndingIndex(body, 3)
            substring = body[:index - 3]
            body = body[index:]

            # Parse condition and contents
            rightParenIndex = substring.find(')')
            condition = substring[substring.find('(') + 1:rightParenIndex]
            contents = substring[rightParenIndex + 1:index]

            # Until for loop
            if 'untill' in condition:
                splitCondition = condition.split('untill')
                leftSide = typeFromString(script, splitCondition[0])
                rightSide = typeFromString(script, splitCondition[1])

                while leftSide != rightSide:
                    response = parse(script, contents)
                    if response is not None:
                        return response
                    leftSide = typeFromString(script, condition.split('untill')[0])
                    rightSide = typeFromString(script, condition.split('untill')[1])
            if 'in' in condition:
                splitCondition = condition.split('in')
                name = splitCondition[0][1:]
                script.variables[name] = Variable(name, None, Modifier.OWO)
                items = resolveValue(script, splitCondition[1])

                if type(items) is list:
                    for item in items:
                        script.variables[name].value = item
                        response = parse(script, contents)
                        if response is not None:
                            return response
                del script.variables[name]
        elif body.startswith("foreeach"):
            index = findEndingIndex(body, 3)
            substring = body[:index - 3]
            body = body[index:]

            # Parse condition and contents
            rightParenIndex = substring.find(')')
            condition = substring[substring.find('(') + 1:rightParenIndex]
            contents = substring[rightParenIndex + 1:index]

            # Until for loop
            if 'in' in condition:
                splitCondition = condition.split('in')
                name = splitCondition[0][1:]
                script.variables[name] = Variable(name, None, Modifier.OWO)
                items = resolveValue(script, splitCondition[1])

                if type(items) is list:
                    for item in items:
                        script.variables[name].value = item
                        response = parse(script, contents)
                        if response is not None:
                            return response
                del script.variables[name]
        elif body.startswith('fn'):
            index = findEndingIndex(body, 3)
            substring = body[:index]
            body = body[index:]

            # Parse args and contents
            rightParenIndex = substring.find(')')
            name = substring[3:rightParenIndex - 1]
            args = substring[substring.find('(') + 1:rightParenIndex]
            contents = substring[rightParenIndex + 1:index]
            methodMap[name] = contents
        elif body.startswith('try'):
            index = findEndingIndex(body, 4)
            substring = body[:index]
            body = body[index:]

            catchIndex = substring.find('catch')
            tryContents = substring[3:catchIndex]
            rightParenIndex = substring.find(')')
            catchContents = substring[rightParenIndex + 1:index - 3]
            exceptionVarName = substring[substring.find('(') + 1:rightParenIndex]

            try:
                response = parse(script, tryContents)
                if response is not None:
                    return response
            except Exception as e:
                script.variables[exceptionVarName] = Variable(exceptionVarName, str(e), Modifier.ONO)
                response = parse(script, catchContents)
                del script.variables[exceptionVarName]
                if response is not None:
                    return response
        elif body.startswith('nudges'):
            index = body.find(';')
            substring = body[:index]
            body = body[index + 1:]
            return resolveValue(script, substring[6:])
        elif ';' in body:
            # Find the index of first ';' and substring it
            index = body.find(';')
            substring = body[:index]
            body = body[index + 1:]
            _parseInstruction(script, substring)
        else:
            parsing = False
    return None

def resolveValue(script, string):
    if string[0] != '$':
        return typeFromString(script, string)
    for var in script.variables:
        varString = '$' + var
        while varString in string:
            value = script.variables[var].value
            # If value is dict
            if type(value) is dict:
                index = string.find(varString) + len(varString)                
                if len(string) > index and string[index] == '[' and string.find(']', index) != -1:
                    key = string[index + 1:string.find(']', index)]
                    return value[key[1:-1]]
                else:
                    return value
            else:
                return value
    return typeFromString(script, string)

def resolveString(script, string):
    for var in script.variables:
        varString = "$" + var
        while varString in string:
            value = script.variables[var].value
            # If value is dict
            if type(value) is dict:
                index = string.find(varString) + len(varString)
                
                if len(string) > index and string[index] == '[' and string.find(']', index) != -1:
                    key = string[index + 1:string.find(']', index)]
                    string = string.replace(varString + '[' + key + ']', str(value[key[1:-1]]))
                else:
                    string = string.replace('$' + var, str(value))
            else:
                string = string.replace('$' + var, str(value))
    return string

def findEndingIndex(body, index):
    openBraces = 1
    endingIndex = index

    while openBraces > 0:
        numbers = [0] * len(keyWords)

        for i in range(len(keyWords)):
            numbers[i] = body.find(keyWords[i], endingIndex)

        smallest = min(i for i in numbers if i > 0)
        for i in range(len(numbers)):
            if numbers[i] != smallest:
                continue

            keyWord = keyWords[i]
            endingIndex = smallest + len(keyWord)

            if keyWord == "}":
                openBraces -= 1
            else:
                openBraces += 1
    return endingIndex

def typeFromString(script, string):
    if string == 'None':
        return None

    name = string[1:]
    if name in script.variables:
        if string.startswith('$'):
            return script.variables[name].value
        elif string.startswith('@'):
            return script.variables[name]

    if string.endswith(')'):
        return handleMethod(script, string)
    else:
        string = resolveString(script, string)

    if string.startswith('{') and string.endswith('}'):
        return json.loads(string)
    if string.startswith('"{') and string.endswith('}"'):
        string = string[1:-1]
        return json.loads(string)
    elif string.startswith('[') and string.endswith(']'):
        items = string[1:-1].split(',')
        for i in range(len(items)):
            items[i] = typeFromString(script, items[i])
        return items
    elif string.startswith('"') and string.endswith('"'):
        return handleString(string[1:-1])
    elif string == 'True' or string == 'False':
        return string == "True"
    elif string == 'Yes' or string == 'No':
        return string == "Yes"
    elif string.isnumeric():
        return int(string)
    elif string.endswith('*float'):
        return float(string.replace('*float', ''))
    elif string.startswith('$'):
        return None
    else:
        return handleString(string)

def _parseInstruction(script, instruction):
    modifier = Modifier.NONE

    # Check for modifier
    for mod in Modifier:
        if instruction.startswith(mod.name.lower()):
            modifier = mod

    varReference = instruction.startswith('$')

    # Check for variable declaration
    if modifier is not Modifier.NONE or varReference:
        if varReference:
            instruction = instruction[1:]
        else:
            instruction = instruction[len(modifier.name):]
        equalsIndex = instruction.find(':=')
        name = instruction[:equalsIndex]
        value = instruction[equalsIndex + 2:]
        
        # Parse true type
        value = resolveValue(script, value)

        # ONO variables cannot have their value modified
        if name in script.variables and script.variables[name].modifier is Modifier.ONO:
            raise Exception(f"Cannot modify a variable `{script.variables[name].name}` with ONO modifier")

        if name in script.variables and script.variables[name].modifier is Modifier.Fixed:
            raise Exception(f"The variable `{script.variables[name].name}` has Fixed value, cannot change it!")

        if name in script.variables and script.variables[name].modifier is Modifier.ReadOnly:
            raise Exception(f"The variable `{script.variables[name].name}` is ReadOnly")

        if name in script.variables and script.variables[name].modifier is Modifier.VARf:
            if type(value) != float:
                print("The varf variable must have float value")
            
        #print(modifier)

        if varReference:
            script.variables[name].value = value
        else:
            script.variables[name] = Variable(name, value, modifier)
    else:
        handleMethod(script, instruction)


def handleMethod(script, instruction):
    # Parse name and args from instruction
    leftParenIndex = instruction.find('(')
    name = instruction[:leftParenIndex]
    argText = instruction[leftParenIndex + 1:instruction.rfind(')')]
    args = []

    if ',' in argText:
        for arg in splitComma(argText):
            args.append(typeFromString(script, arg))
    else:
        args.append(typeFromString(script, argText))

    # Check if method exists
    if name in methodMap:
        method = methodMap[name]
        if type(method) is str:
            returnValue = parse(script, method)
            if returnValue is not None:
                return returnValue
        else:
            return method(script, args)

def splitComma(string):
    result = []
    index = 0
    insideString = False
    insideMethodArgs = False

    for i in range(len(string)):
        if string[i] == '"':
            insideString = not insideString
        elif string[i] == '(': 
            insideMethodArgs = True
        elif string[i] == ')':
            insideMethodArgs = False
        elif string[i] == ',' and not insideString and not insideMethodArgs:
            result.append(string[index:i])
            index = i + 1
    
    result.append(string[index:])
    return result

def handleString(string):
    try:
        return ne.evaluate(string)
    except:
        string = re.sub(r'(?<!\\)"', '', string)
        string = re.sub(r'\\(.)', r'\1', string)
        string = re.sub(r'(?<!\\)\+', '', string)
        return string