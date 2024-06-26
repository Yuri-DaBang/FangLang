# Example code to test the _parseInstruction function

from interpreter import _parseInstruction

# Create a script context
script = {'variables': {}}

# Valid variable declarations
try:
    _parseInstruction(script, "var1 := 3.14")  # VARf (Float)
    _parseInstruction(script, "var2 := 5.0")   # VARf (Float)
    _parseInstruction(script, "var3 := 'hello'")  # VARstr (String)
    _parseInstruction(script, "var4 := True")     # VARbool (Boolean)
    _parseInstruction(script, "var5 := 42")       # VARint (Integer)
except Exception as e:
    print("Error:", e)

# Invalid variable declarations (to trigger exceptions)
try:
    _parseInstruction(script, "var6 := 10")      # Should raise exception for VARf type
    _parseInstruction(script, "var7 := 3.14f")   # Should raise exception for VARd type
    _parseInstruction(script, "var8 := 'world'") # Should raise exception for VARbool type
    _parseInstruction(script, "var9 := 3")       # Should raise exception for VARstr type
    _parseInstruction(script, "var10 := False")  # Should raise exception for VARint type
except Exception as e:
    print("Error:", e)