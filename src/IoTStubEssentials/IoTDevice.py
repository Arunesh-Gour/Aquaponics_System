import re

class IoTDevice:
   """Base class for IoT device stubs.
   
   Base class for all IoT devices or sensors.
   Keeps track of all items created - objects, and allows them to be fetched
   through this class directly, if pointer lost by any chance.
   
   Attributes
   ----------
   availableID : int
      Static attribute.
      Stores the total number of devices, used as serial for new registrations.
   deviceTypes : dict
      Static attribute.
      Stores list of device types which can be initialized / created with this
      class and attributes required for them in dict format, and a count for
      total registration for the type.
      Format: {"type" : [{"attributes" : default_value,}, 0,],}
   devices : dict
      Static attribute.
      Stores devices' names with their type and object.
      Format: {"name" : ["type", object,],}
   deviceType : str
      Type of device, within {deviceTypes}.
   deviceAttributes : dict
      All read-write-able attributes of a device.
      Format: {"attribute name": value,}
   serial : str
      Device's serial number, unique value assigned automatically.
   
   Methods
   -------
   read (key)
      Returns readings of particular attribute (key).
   write (key, value)
      Writes values to particular attribute (key).
   """
   
   availableID = 0
   deviceTypes = {
      # Type : [{"attribute" : values (default None)}, 0 (count)],
      # "House": [{"time" : 1, "apps" : 2,}, 0],
   }
   devices = {
      # Name (unique) : [type, object],
      # "Kryptonite" : ["House", None,],
   }
   
   def __init__ (self, deviceType, deviceName=None):
      """Initializes class and attributes.
      
      Sets up class with required attributes and auto-initializes them.
      
      Parameter
      ---------
      deviceType : str
         Type of device; from devices' list.
      deviceName : str
         Unique name for device (optional).
      """
      
      if (type(deviceType).__name__ == 'str'):
         if (deviceType in IoTDevice.deviceTypes.keys()):
            self.deviceType = deviceType
            self.deviceAttributes = (\
               # "Attribute" : value (default),
               IoTDevice.deviceTypes[deviceType][0]\
            ).copy()
         else:
            raise ValueError("unrecognized deviceType '{0}'".format(\
                  deviceType,
               )\
            )
      else:
         raise TypeError("deviceType requires 'str' only")
      
      if (deviceName == None):
         self.deviceName = "{0}{1:03}_{2:03}".format(\
            self.deviceType,
            IoTDevice.deviceTypes[self.deviceType][1],
            IoTDevice.availableID,
         )
      elif (type(deviceName).__name__ == 'str' and deviceName != ''):
         if (deviceName not in IoTDevice.devices.keys()):
            self.deviceName = deviceName
         else:
            raise ValueError(\
               "deviceName '{0}' already assigned to another device".format(
                  deviceName,
               )\
            )
      else:
         raise TypeError("deviceName requires 'str' only")
      
      self.serial = "{0:03}.{1:03}".format(\
         IoTDevice.deviceTypes[self.deviceType][1],
         IoTDevice.availableID,
      )
      
      IoTDevice.availableID += 1
      IoTDevice.deviceTypes[self.deviceType][1] += 1
      IoTDevice.devices[self.deviceName] = [self.deviceType, self,]
   
   def read(self, key):
      """Returns reading for specified attribute (key) in device.
      
      Reads the specified attribute (key) from device's attributes and returns
      the reading in apt format.
      
      Parameter
      ---------
      key : str
         Attribute name, to retreive the value of.
      
      Returns
      -------
      object
         Returns respective value, as stored for key specified.
      """
      
      if (key not in self.deviceAttributes.keys()):
         raise NameError("unrecognized key '{0}'".format(key))
      
      raise NotImplementedError("method 'read' not implemented")
   
   def write (self, key, value):
      """Writes values to the specified attribute (key).
      
      Writes the specified value to specified attribute (key) to device's
      attributes.
      
      Parameter
      ---------
      key : str
         Attribute name, to target value to.
      value : object
         Value to assign key with.
      """
      
      if (key not in self.deviceAttributes.keys()):
         raise NameError("unrecognized key '{0}'".format(key))
      
      raise NotImplementedError("method 'write' not implemented")
