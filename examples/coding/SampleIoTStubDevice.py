from ..ProjectEssentials-Python import (IoTDevice, Signal)
# Above line will generate error as IoTStubEssentials is in current
# directory, not in parent. This it not changed to show how you need
# to write in IoTStub devices / files.

if ("SampleDeviceName" not in (IoTDevice.IoTDevice.deviceTypes[0]).keys()):
   IoTDevice.IoTDevice.deviceTypes[0]["SampleDeviceName"] = [
      {
         # "attribute_name" : default_value_in_apt_format,
         "SomeKey" : 0,
         "_SomeKey2" : True,
      },
      0, # IoTDevice manages this automatically.
   ]

class SampleDeviceName (IoTDevice.IoTDevice):
   def __init__ (self, deviceName=None):
      # Initializes the IoTDevice as per base class.
      super().__init__(deviceType="SampleDeviceName", deviceName=deviceName)
      
      # Registers this IoT device with Signalling service.
      Signal.Signal.register(self.serial, self.write(key="_?"))
   
   def delete (self):
      # Unregisters this IoT device from Signalling service.
      Signal.Signal.unregister(self.serial)
      
      super().delete()
   
   def read (self, key):
      # Basic type, value check mechanism, required.
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
         # Returns tuple containing readable values, may contain immutable
         # values as well (immutable to main app).
         # If single value is readable, then also return tuple.
         # return ("SomeKey",)
         # Comma at end represents a tuple.
         return ("serial", "SomeKey", "_SomeKey2",)
      
      if (key == "serial"):
         return self.serial
      
      # Basic check.
      if (key not in self.write(key="_?")):
         raise NameError("unrecognized key '{0}'".format(key))
      
      # Main read method start here:
      if (key == "SomeKey"):
         # Do NOT pass key to deviceAttributes. Always hardcode them
         # yourself to avoid other sorts of bugs / errors / security flaws.
         retval = self.deviceAttributes["SomeKey"]
         # Process retval if required.
         return retval
      elif (key == "_SomeKey2"):
         retval = self.deviceAttributes["_SomeKey2"]
         # Process retval if required.
         return retval
      else:
         # Raise appropriate error or perform other function.
         raise ValueError("immutable key '{0}'".format(key))
   
   def write (self, key, value=None):
      # Basic type, value check mechanism, required.
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
         # Returns tuple containing readable values, may contain immutable
         # values as well (immutable to main app).
         # If single value is readable, then also return tuple.
         # return ("SomeKey",)
         # Comma at end represents a tuple.
         # Contains visible values.
         return ("SomeKey",)
      elif (key == "_?"):
         # Contains hidden values as well.
         return ("SomeKey", "_SomeKey2",)
      
      # Basic check.
      if (key not in self.write(key="_?")):
         raise NameError("unrecognized key '{0}'".format(key))
      
      # Main write method start here:
      if (key == "SomeKey"):
         # Storing old value for later use in signal.
         oldValue = self.deviceAttributes["SomeKey"]
         # Perform checks on value provided.
         value = someprocess(value)
         # Process value as needed.
         # Do NOT pass key to deviceAttributes. Always hardcode them
         # yourself to avoid other sorts of bugs / errors / security flaws.
         self.deviceAttributes["SomeKey"] = value
         
         # Sends signals only when value is changed.
         # Use this in all places where value is written. REQUIRED.
         if (oldValue != self.deviceAttributes["SomeKey"]):
            Signal.Signal.signal(self.serial, "SomeKey")
      elif (key == "_SomeKey2"):
         # Storing old value for later use in signal.
         oldValue = self.deviceAttributes["_SomeKey2"]
         # Process value as needed.
         self.deviceAttributes["_SomeKey2"] = value
         
         # Sends signals only when value is changed.
         # Use this in all places where value is written. REQUIRED.
         if (oldValue != self.deviceAttributes["_SomeKey2"]):
            Signal.Signal.signal(self.serial, "_SomeKey2")
      else:
         # Raise appropriate error or perform other function.
         raise ValueError("immutable key '{0}'".format(key))
# Guard line below: Do NOT exceed 79 character limit per line in any case.
# -----------------------------------------------------------------------------
