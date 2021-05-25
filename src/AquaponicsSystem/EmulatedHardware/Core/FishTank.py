from ..Actuators import (WaterValve,)
from ..Sensors import (
   DOMeter, SpectrophotoMeter, TANMeter, TemperaturepHMeter, WaterLevel,
)

class FishTank:
   tanks = [
      {
         # tankname : tank,
      },
      0,
   ]
   
   unusedTankIDs = []
   
   def __init__ (self, tankName=None):
      if (tankName == None or type(tankName).__name__ == 'str'):
         if (tankName != None):
            if (tankName == '' or len(tankName) < 2):
               raise TypeError("tankName requires 'str' of length >= 2")
            
            if (tankName in (FishTank.tanks[0]).keys()):
               raise ValueError("tankName '{0}' already in use".format(
                     tankName,
                  )\
               )
      else:
         raise TypeError("tankName requires 'NoneType' or 'str' only")
      
      if (tankName == None):
         if (len(FishTank.unusedTankIDs) > 0):
            self.tankID = FishTank.unusedTankIDs.pop()
            self.tankName = "Tank_{0:03}".format(self.tankID)
         else:
            self.tankID = FishTank.tanks[1]
            self.tankName = "Tank_{0:03}".format(FishTank.tanks[1])
         
         FishTank.tanks[1] += 1
      else:
         self.tankName = tankName
      
      self._dataAttributes = {
         'sensors' : {
            # sensor : sensor
            'dO': DOMeter.DOMeter(),
            'spectrophotoMeter' : SpectrophotoMeter.SpectrophotoMeter(),
            'tan' : TANMeter.TANMeter(),
            'temperaturepH' : TemperaturepHMeter.TemperaturepHMeter(),
            'waterLevel' : WaterLevel.WaterLevel(),
         },
         'actuators' : {
            # actuator : actuator
            'waterinlet' : WaterValve.WaterValve(),
            'wateroutlet' : WaterValve.WaterValve(),
         },
         "unionizedNH3" : 0.0,
      }
      self.blocker = False
      
      self._dataAttributes['sensors']['dO'].write(
         'power', True,
      )
      self._dataAttributes['sensors']['dO'].write(
         'DO', 8.0,
      )
      self._dataAttributes['sensors']['spectrophotoMeter'].write(
         'power', True,
      )
      self._dataAttributes['sensors']['spectrophotoMeter'].write(
         'NO2', 0.8,
      )
      self._dataAttributes['sensors']['spectrophotoMeter'].write(
         'NO3', 80.0,
      )
      self._dataAttributes['sensors']['tan'].write(
         'power', True,
      )
      self._dataAttributes['sensors']['tan'].write(
         'TAN', 0.18,
      )
      self._dataAttributes['sensors']['temperaturepH'].write(
         'power', True,
      )
      self._dataAttributes['sensors']['temperaturepH'].write(
         'temperature', 28.0,
      )
      self._dataAttributes['sensors']['temperaturepH'].write(
         'pH', 7.0,
      )
      self._dataAttributes['sensors']['waterLevel'].write(
         'power', True,
      )
      self._dataAttributes['sensors']['waterLevel'].write(
         'level', 80.0,
      )
      self._dataAttributes['actuators']['waterinlet'].write(
         'power', True,
      )
      self._dataAttributes['actuators']['waterinlet'].write(
         'maxFlow', 0.5,
      )
      self._dataAttributes['actuators']['wateroutlet'].write(
         'power', True,
      )
      self._dataAttributes['actuators']['wateroutlet'].write(
         'maxFlow', 0.5,
      )
      
      FishTank.tanks[0][self.tankName] = self
   
   def delete (self):
      FishTank.tanks[1] -= 1
      FishTank.unusedTankIDs.append(self.tankID)
      (FishTank.tanks[0]).pop(self.tankName)
   
   def get (self, category, device):
      if (type(category).__name__ == 'str'):
         if (category.strip() == '' or len(category.strip()) < 1):
            raise ValueError("unrecognized category '{0}'".format(\
                  category,
               )\
            )
      else:
         raise TypeError("category requires 'str' only")
      
      category = category.strip()
      
      # Basic check.
      if (category not in self._dataAttributes.keys()):
         raise NameError("unrecognized category '{0}'".format(category))
      
      if (category == 'unionizedNH3'):
         raise NameError("unrecognized category '{0}'".format(category))
      
      if (type(device).__name__ == 'str'):
         if (device.strip() == '' or len(device.strip()) < 1):
            raise ValueError("unrecognized device '{0}'".format(\
                  device,
               )\
            )
      else:
         raise TypeError("device requires 'str' only")
      
      device = device.strip()
      
      # Basic check.
      if (device not in self._dataAttributes[category].keys()):
         raise NameError("unrecognized device '{0}'".format(device))
      
      return self._dataAttributes[category][device]
   
   def set (self, category, device, value):
      if (type(category).__name__ == 'str'):
         if (category.strip() == '' or len(category.strip()) < 1):
            raise ValueError("unrecognized category '{0}'".format(\
                  category,
               )\
            )
      else:
         raise TypeError("category requires 'str' only")
      
      category = category.strip()
      
      # Basic check.
      if (category not in self._dataAttributes.keys()):
         raise NameError("unrecognized category '{0}'".format(category))
      
      if (category == 'unionizedNH3'):
         raise NameError("unrecognized category '{0}'".format(category))
      
      if (type(device).__name__ == 'str'):
         if (device.strip() == '' or len(device.strip()) < 1):
            raise ValueError("unrecognized device '{0}'".format(\
                  device,
               )\
            )
      else:
         raise TypeError("device requires 'str' only")
      
      device = device.strip()
      
      # Basic check.
      if (device not in self._dataAttributes[category].keys()):
         raise NameError("unrecognized device '{0}'".format(device))
      
      if (category == "sensors"):
         if (device == "dO"):
            if (type(value).__name__ != 'DOMeter'):
               raise TypeError("{0}.{1} requires 'DOMeter'".format(
                     device, category,
                  )\
               )
            
            self._dataAttributes[category][device] = value
         elif (device == "spectrophotoMeter"):
            if (type(value).__name__ != 'SpectrophotoMeter'):
               raise TypeError("{0}.{1} requires 'SpectrophotoMeter'".format(
                     device, category,
                  )\
               )
            
            self._dataAttributes[category][device] = value
         elif (device == "tan"):
            if (type(value).__name__ != 'TANMeter'):
               raise TypeError("{0}.{1} requires 'TANMeter'".format(
                     device, category,
                  )\
               )
            
            self._dataAttributes[category][device] = value
         elif (device == "temperaturepH"):
            if (type(value).__name__ != 'TemperaturepH'):
               raise TypeError("{0}.{1} requires 'TemperaturepHMeter'".format(
                     device, category,
                  )\
               )
            
            self._dataAttributes[category][device] = value
         elif (device == "waterLevel"):
            if (type(value).__name__ != 'WaterLevel'):
               raise TypeError("{0}.{1} requires 'WaterLevel'".format(
                     device, category,
                  )\
               )
            
            self._dataAttributes[category][device] = value
      elif (category == "actuators"):
         if (device == "waterinlet"):
            if (type(value).__name__ != 'WaterValve'):
               raise TypeError("{0}.{1} requires 'WaterValve'".format(
                     device, category,
                  )\
               )
            
            self._dataAttributes[category][device] = value
         elif (device == "wateroutlet"):
            if (type(value).__name__ != 'WaterValve'):
               raise TypeError("{0}.{1} requires 'WaterValve'".format(
                     device, category,
                  )\
               )
            
            self._dataAttributes[category][device] = value
   
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
      
      if (key == '?'):
         return (
            'DO', 'NO2', 'NO3', 'TAN', 'temperature', 'pH', 'waterLevel',
            'unionizedNH3',
         )
      
      # Basic check.
      if (key not in self.read('?')):
         raise NameError("unrecognized key '{0}'".format(key))
      
      if (key == "DO"):
         return self._dataAttributes['sensors']['dO'].read('DO')
      elif (key == "NO2"):
         return self._dataAttributes['sensors']['spectrophotoMeter'].read(
            key='NO2',
         )
      elif (key == "NO3"):
         return self._dataAttributes['sensors']['spectrophotoMeter'].read(
            key='NO3',
         )
      elif (key == "TAN"):
         return self._dataAttributes['sensors']['tan'].read('TAN')
      elif (key == "temperature"):
         return self._dataAttributes['sensors']['temperaturepH'].read(
            key='temperature',
         )
      elif (key == "pH"):
         return self._dataAttributes['sensors']['temperaturepH'].read(
            key='pH',
         )
      elif (key == "waterLevel"):
         return self._dataAttributes['sensors']['waterLevel'].read(
            key='level',
         )
      elif (key == "unionizedNH3"):
         return self._dataAttributes['unionizedNH3']
   
   def write (self, key, value, blockable=False):
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
      if (key not in self.read('?')):
         raise NameError("unrecognized key '{0}'".format(key))
      
      if (type(value).__name__ != 'float'):
         raise TypeError("{0} requires 'float'".format(key))
      
      if (blockable):
         while(self.blocker):
            pass
      
      if (key == "DO"):
         self._dataAttributes['sensors']['dO'].write('DO', value)
      elif (key == "NO2"):
         self._dataAttributes['sensors']['spectrophotoMeter'].write(
            key='NO2',
            value=value,
         )
      elif (key == "NO3"):
         self._dataAttributes['sensors']['spectrophotoMeter'].write(
            key='NO3',
            value=value,
         )
      elif (key == "TAN"):
         self._dataAttributes['sensors']['tan'].write(
            key='TAN',
            value=value,
         )
      elif (key == "temperature"):
         self._dataAttributes['sensors']['temperaturepH'].write(
            key='temperature',
            value=value,
         )
      elif (key == "pH"):
         self._dataAttributes['sensors']['temperaturepH'].write(
            key='pH',
            value=value,
         )
      elif (key == "waterLevel"):
         self._dataAttributes['sensors']['waterLevel'].write(
            key='level',
            value=value,
         )
      elif (key == "unionizedNH3"):
         if (value >= 0.0 and value <= 2000.0):
            self._dataAttributes['unionizedNH3'] = value
         else:
            raise ValueError("invalid {0}".format(key))
# Guard line below: Do NOT exceed 79 character limit per line in any case.
# -----------------------------------------------------------------------------
