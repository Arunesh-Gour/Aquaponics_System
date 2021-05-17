from ..IoTStubEssentials import (IoTDevice, Signal)

if ("WaterHeater" not in (IoTDevice.IoTDevice.deviceTypes[0]).keys()):
   IoTDevice.IoTDevice.deviceTypes[0]["WaterHeater"] = [
      {
         # "attribute_name" : default_value_in_apt_format,
         "power" : False,
      },
      0, #IoTDevice manages this automatically.
   ]

class WaterHeater (IoTDevice.IoTDevice):
   def __init__ (self, deviceName=None):
      super().__init__(deviceType="WaterHeater", deviceName=deviceName)
      
      Signal.Signal.register(self.serial, self.read(key="?"))
   
   def read (self, key):
      if (type(key).__name__ == 'str'):
         if (key.strip().lower() == '' or len(key.strip().lower()) < 1):
            raise ValueError("unrecognized key '{0}'".format(\
                  key,
               )\
            )
      else:
         raise TypeError("key requires 'str' only")
      
      # Returns a tuple of what values are readable.
      if (key.strip().lower() == "?"):
         return ("serial", "power",)
      
      if (key.strip().lower() == "serial"):
         return self.serial
      
      # Basic check.
      if (key not in self.deviceAttributes.keys()):
         raise NameError("unrecognized key '{0}'".format(key))
      
      # Main read method start here:
      if (key.strip().lower() == "power"):
         # Explicitly checking so as not to pass mutable value.
         if (self.deviceAttributes["power"] == True):
            return True
         else:
            return False
      else:
         raise ValueError("non-readable key '{0}'".format(key))
   
   def write (self, key, value=None):
      if (type(key).__name__ == 'str'):
         if (key.strip().lower() == '' or len(key.strip().lower()) < 1):
            raise ValueError("unrecognized key '{0}'".format(\
                  key,
               )\
            )
      else:
         raise TypeError("key requires 'str' only")
      
      # Returns a tuple of what values are mutable.
      if (key.strip().lower() == "?"):
         # Contains visible values.
         return ("power",)
      elif (key.strip().lower() == "_?"):
         # Contains hidden values as well.
         return ("power",)
      
      # Basic check.
      if (key not in self.deviceAttributes.keys()):
         raise NameError("unrecognized key '{0}'".format(key))
      
      # Main write method start here:
      if (key.strip().lower() == "power"):
         if (type(value).__name__ == 'bool'):
            oldValue = self.deviceAttributes["power"]
            if (value == True):
               self.deviceAttributes["power"] = True
            elif (value == False):
               self.deviceAttributes["power"] = False
            
            if (oldValue != self.deviceAttributes["power"]):
               Signal.Signal.signal(self.serial, "power")
         else:
            raise TypeError("power requires 'bool' only")
      else:
         raise ValueError("immutable key '{0}'".format(key))
# Guard line below: Do NOT exceed 79 character limit per line in any case.
# -----------------------------------------------------------------------------
