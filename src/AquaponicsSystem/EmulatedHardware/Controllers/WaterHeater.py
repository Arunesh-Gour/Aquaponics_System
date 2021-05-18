from ..IoTStubEssentials import (IoTDevice, Signal)

if ("WaterHeater" not in (IoTDevice.IoTDevice.deviceTypes[0]).keys()):
   IoTDevice.IoTDevice.deviceTypes[0]["WaterHeater"] = [
      {
         # "attribute_name" : default_value_in_apt_format,
         "power" : False,
         "_heatingRate" : 0.0,
      },
      0, # IoTDevice manages this automatically.
   ]

class WaterHeater (IoTDevice.IoTDevice):
   def __init__ (self, deviceName=None):
      super().__init__(deviceType="WaterHeater", deviceName=deviceName)
      
      Signal.Signal.register(self.serial, self.write(key="_?"))
   
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
         return ("serial", "power", "_heatingRate")
      
      if (key == "serial"):
         return self.serial
      
      # Basic check.
      if (key not in self.write(key="_?")):
         raise NameError("unrecognized key '{0}'".format(key))
      
      # Main read method start here:
      if (key == "power"):
         # Explicitly checking so as not to pass mutable value.
         if (self.deviceAttributes["power"] == True):
            return True
         else:
            return False
      if (key == "_heatingRate"):
         return self.deviceAttributes["_heatingRate"]
      else:
         raise ValueError("non-readable key '{0}'".format(key))
   
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
      
      # Returns a tuple of what values are mutable.
      if (key == "?"):
         # Contains visible values.
         return ("power",)
      elif (key == "_?"):
         # Contains hidden values as well.
         return ("power", "_heatingRate",)
      
      # Basic check.
      if (key not in self.write(key="_?")):
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
      if (key == "_heatingRate"):
         if (type(value).__name__ == 'float'):
            if (value > -5.0 and value < 5.0):
               oldValue = self.deviceAttributes["_heatingRate"]
               
               self.deviceAttributes["_heatingRate"] = value
               
               if (oldValue != self.deviceAttributes["_heatingRate"]):
                  Signal.Signal.signal(self.serial, "_heatingRate")
            else:
               raise ValueError("invalid _heatingRate '{0}'".format(value))
         else:
            raise TypeError("_heatingRate requires 'float' value")
      else:
         raise ValueError("immutable key '{0}'".format(key))
# Guard line below: Do NOT exceed 79 character limit per line in any case.
# -----------------------------------------------------------------------------
