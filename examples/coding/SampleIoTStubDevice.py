from ..IoTStubEssentials import (IoTDevice, Signal)
# Above line will generate error as IoTStubEssentials in in current
# directory, not in parent. This it not changed to show how you need
# to write in IoTStub devices / files.

if ("SampleDeviceName" not in (IoTDevice.IoTDevice.deviceTypes[0]).keys()):
   IoTDevice.IoTDevice.deviceTypes[0]["SampleDeviceName"] = [
      {
         # "attribute_name" : default_value_in_apt_format,
         "SomeKey" : 0,
         "SomeKey2" : True,
      },
      0, #IoTDevice manages this automatically.
   ]

class SampleDeviceName (IoTDevice.IoTDevice):
   def __init__ (self, deviceName=None):
      # Initializes the IoTDevice as per base class.
      super().__init__(deviceType="WaterHeaterIoT", deviceName=deviceName)
      
      # Registers this IoT device with Signalling service.
      Signal.Signal.register(self.serial, self.read(key="?"))
   
   def read (self, key):
      # Basic type, value check mechanism, required.
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
         # Returns tuple containing readable values, may contain immutable
         # values as well (immutable to main app).
         # If single value is readable, then also return tuple.
         # return ("SomeKey",)
         # Comma at end represents a tuple.
         return ("serial", "SomeKey", "SomeKey2",)
      
      if (key.strip().lower() == "serial"):
         return self.serial
      
      # Basic check.
      if (key not in self.deviceAttributes.keys()):
         raise NameError("unrecognized key '{0}'".format(key))
      
      # Main read method start here:
      if (key.strip().lower() == "SomeKey".lower()):
         # Do NOT pass key to deviceAttributes. Always hardcode them
         # yourself to avoid other sorts of bugs / errors / security flaws.
         retval = self.deviceAttributes["SomeKey"]
         # Process retval if required.
         return retval
      elif (key.strip().lower() == "SomeKey2".lower()):
         retval = self.deviceAttributes["SomeKey2"]
         # Process retval if required.
         return retval
      else:
         # Raise appropriate error or perform other function.
         raise ValueError("immutable key '{0}'".format(key))
   
   def write (self, key, value=None):
      # Basic type, value check mechanism, required.
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
         # Returns tuple containing readable values, may contain immutable
         # values as well (immutable to main app).
         # If single value is readable, then also return tuple.
         # return ("SomeKey",)
         # Comma at end represents a tuple.
         # Contains visible values.
         return ("power",)
      elif (key.strip().lower() == "_?"):
         # Contains hidden values as well.
         return ("power",)
      
      # Basic check.
      if (key not in self.deviceAttributes.keys()):
         raise NameError("unrecognized key '{0}'".format(key))
      
      # Main write method start here:
      if (key.strip().lower() == "SomeKey".lower()):
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
      elif (key.strip().lower() == "SomeKey2".lower()):
         # Storing old value for later use in signal.
         oldValue = self.deviceAttributes["SomeKey2"]
         # Process value as needed.
         self.deviceAttributes["SomeKey2"] = value
         
         # Sends signals only when value is changed.
         # Use this in all places where value is written. REQUIRED.
         if (oldValue != self.deviceAttributes["SomeKey2"]):
            Signal.Signal.signal(self.serial, "SomeKey2")
      else:
         # Raise appropriate error or perform other function.
         raise ValueError("immutable key '{0}'".format(key))
# Guard line below: Do NOT exceed 79 character limit per line in any case.
# -----------------------------------------------------------------------------
