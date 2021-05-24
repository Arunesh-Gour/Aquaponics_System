import os

class DBController:
   def __init__ (self, filename, variables):
      if (type(filename).__name__ != 'str'):
         raise TypeError("filename requires 'str'")
      
      if (type(variables).__name__ != 'dict'):
         raise TypeError("variables requires 'dict'")
      
      if (not os.path.exists(filename)):
         raise ValueError("file '{0}' does not exists".format(filename))
      
      self._filename = filename
      self.variables = variables
      """Variables =
      {
         "tan" : float,
         "ph" : float,
         "temperature" : float,
         "dO" : float,
         "NO2" : float,
         "NO3" : float,
         "unionizedNH3" : float,
         "waterlevel" : float,
         "chelatedIron" : str,
      }
      """
   
   def load (self):
      # Read variables from file.
      with open(self.filename, "r") as filehandler:
         # Read entire file as filehandler.read().
         # Or read line by line as filehandler.readline().
   
   def save (self):
      # Write variables to file.
      with open(self.filename, "w") as filehandler:
         # Write entire file as filehandler.write(string).
   
   def read (self, key):
      if (type(key).__name__ == 'str'):
         if (key.strip() == '' or len(key.strip()) < 1):
            raise ValueError("unrecognized key '{0}'".format(\
                  key,
               )\
            )
      else:
         raise TypeError("key requires 'str' only")
      
      key = key.strip()
      
      if (key not in self.variables.keys()):
         raise NameError("unrecognized key '{0}'".format(key))
      
      # Read value from file.
      # And return it in appropriate format.
   
   def write (self, key, value):
      if (type(key).__name__ == 'str'):
         if (key.strip() == '' or len(key.strip()) < 1):
            raise ValueError("unrecognized key '{0}'".format(\
                  key,
               )\
            )
      else:
         raise TypeError("key requires 'str' only")
      
      key = key.strip()
      
      if (key not in self.variables.keys()):
         raise NameError("unrecognized key '{0}'".format(key))
      
      # Write value to file.
      # Efficiently.
      # Check value type and raise appropriate error where needed.
# Guard line below: Do NOT exceed 79 character limit per line in any case.
# -----------------------------------------------------------------------------
