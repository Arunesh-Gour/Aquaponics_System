from ..ProjectEssentials import (IoTDevice, Signal)

if ("TemperaturepHMeter" not in (IoTDevice.IoTDevice.deviceTypes[0]).keys()):
   IoTDevice.IoTDevice.deviceTypes[0]["TemperaturepHMeter"] = [
      {
         # "attribute_name" : default_value_in_apt_format,
         "power" : False,
         "temperature" : 0.0,
         "pH" : 0.0,
      },
      0, # IoTDevice manages this automatically.
   ]

class TemperaturepHMeter (IoTDevice.IoTDevice):
   def __init__ (self, deviceName=None):
      super().__init__(deviceType="TemperaturepHMeter", deviceName=deviceName)
      
      Signal.Signal.register(self.serial, self.read(key="?"))
   
   def delete (self):
      Signal.Signal.unregister(self.serial)
      
      super().delete()
   
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
      
      # Returns a tuple of what values are readable.
      if (key == "?"):
         return tuple(self.deviceAttributes.keys())
      
      if (key == "serial"):
         return self.serial
      
      # Basic check.
      if (key not in self.deviceAttributes.keys()):
         raise NameError("unrecognized key '{0}'".format(key))
      
      # Main read method start here:
      return self.deviceAttributes[key]
   
   def write (self, key, value=None):
      if (type(key).__name__ == 'str'):
         if (key.strip() == '' or len(key.strip()) < 1):
            raise ValueError("unrecognized key '{0}'".format(\
                  key,
               )\
            )
      else:
         raise TypeError("key requires 'str' only")
      
      key = key.strip()
      
      # Basic check.
      if (key not in self.deviceAttributes.keys()):
         raise NameError("unrecognized key '{0}'".format(key))
      
      # Main write method start here:
      if (key == "power"):
         if (type(value).__name__ == 'bool'):
            oldValue = self.deviceAttributes["power"]
            
            self.deviceAttributes["power"] = value
            
            if (oldValue != self.deviceAttributes["power"]):
               Signal.Signal.signal(self.serial, "power")
         else:
            raise TypeError("power requires 'bool' only")
      elif (key in list(self.deviceAttributes.keys())[1:2]):
         if (type(value).__name__ == 'float'):
            if (value >= -50.0 and value <= 60.0):
               oldValue = self.deviceAttributes[key]
               
               self.deviceAttributes[key] = value
               
               if (oldValue != self.deviceAttributes[key]):
                  Signal.Signal.signal(self.serial, key)
            else:
               raise ValueError("invalid {0} '{1}'".format(key, value))
         else:
            raise TypeError("{0} requires 'float' value".format(key))
      elif (key in list(self.deviceAttributes.keys())[2:]):
         if (type(value).__name__ == 'float'):
            if (value >= 0.0 and value <= 14.0):
               oldValue = self.deviceAttributes[key]
               
               self.deviceAttributes[key] = value
               
               if (oldValue != self.deviceAttributes[key]):
                  Signal.Signal.signal(self.serial, key)
            else:
               raise ValueError("invalid {0} '{1}'".format(key, value))
         else:
            raise TypeError("{0} requires 'float' value".format(key))
      else:
         raise ValueError("immutable key '{0}'".format(key))
# Guard line below: Do NOT exceed 79 character limit per line in any case.
# -----------------------------------------------------------------------------
