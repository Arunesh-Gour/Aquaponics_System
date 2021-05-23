from multiprocessing import (Lock,)
from ..EmulatedHardware import (AutoExecutor, Signal)

class SampleAISystem:
   def __init__ (self, tanSensor, temperaturepHSensor, doSensor,
      spectrophotometerSensor, waterlevelSensor, waterinlet,
      wateroutlet, alertSystem):
      if (type(tanSensor).__name__ != 'TANSensor'):
         raise TypeError("tanSensor requires 'TANSensor'")
      
      if (type(temperaturepHSensor).__name__ != 'WaterTemperaturepH'):
         raise TypeError("temperaturepHSensor requires 'WaterTemperaturepH'")
      
      if (type(doSensor).__name__ != 'WaterDO'):
         raise TypeError("doSensor requires 'WaterDO'")
      
      if (type(spectrophotometerSensor).__name__ != 'Spectrophotometer'):
         raise TypeError(\
            "spectrophotometerSensor requires 'Spectrophotometer'"\
         )
      
      if (type(waterlevelSensor).__name__ != 'WaterLevel'):
         raise TypeError("waterlevelSensor requires 'WaterLevel'")
      
      if (type(waterinlet).__name__ != 'WaterValve'):
         raise TypeError("waterinlet requires 'WaterValve'")
      
      if (type(wateroutlet).__name__ != 'WaterValve'):
         raise TypeError("wateroutlet requires 'WaterValve'")
      
      if (type(alertSystem).__name__ != 'Alert'):
         raise TypeError("alertSystem requires 'Alert'")
      
      self._dataAttributes = {
         "lock" : Lock(),
         # sensor/actuator name : [sensor/actuator, *signalIDs],
         "tan" : tanSensor,
         "temperaturepH" : temperaturepHSensor,
         "dO" : doSensor,
         "spectrophotometer" : spectrophotometerSensor,
         "waterlevel" : waterlevelSensor,
         "waterinlet" : waterinlet,
         "wateroutlet" : wateroutlet,
         "alert" : alertSystem,
         
         "safetyLevels" : {
            # 2 categories - safe / unsafe.
            "unionizedNH3" : "safe",
            "tan" : "safe",
            "pH" : "unsafe",
            "temperature" : "safe",
            "dO" : "safe",
            "NO2" : "safe",
            "NO3" : "safe",
            "waterlevel" : "safe",
         }
      }
      
      # Add signals and use autoexecutor to automate.
   
   def start (self):
      raise NotImplementedError
   
   def stop (self):
      raise NotImplementedError
   
   def _check_safetyLevels (self):
      # Call each checks.
      # Run appropriate resolvers.
      # _change_pH / _change_water / _change_waterlevel
      # or show alert.
      
      # For alert, use below:
      # self._dataAttributes['alert'].alert(
      #    attribute='unionizedNH3', # required
      #    title='alerttitle', # optional
      #    description='long desc about alert', # optional
      # )
      # Alerts are non-blocking.
      
      # For temperature, just check if temp is high or low
      # and raise alert. We're assuming we have automatic water
      # heater regulating temp itself with 1 deg C sensitivity.
      # sensitivity = if value >/< 1 deg, heater will manage itself.
      
      # Generally, here we need to add multiple coditions by applying
      # PnC logically over the combinations of each safety level,
      # as per analysis from chart given in discussion section.
      raise NotImplementedError
   
   def _change_pH (self):
      # Change pH.
      self._dataAttributes['lock'].acquire()
      # For alert, use below:
      # self._dataAttributes['alert'].alert(
      #    attribute='pH', # required
      #    title='alerttitle', # optional
      #    description='long desc about alert', # optional
      # )
      # Alerts are non-blocking.
      # Logic goes here.
      # keep checking pH levels after each second,
      # by using time.sleep(float).
      # if no effect, raise alert.
      self._dataAttributes['lock'].release()
      raise NotImplementedError
   
   def _change_water (self, changepercent=20):
      # Change changepercent amount of water from tank.
      self._dataAttributes['lock'].acquire()
      # For alert, use below:
      # self._dataAttributes['alert'].alert(
      #    attribute='waterinlet', # required
      #    title='alerttitle', # optional
      #    description='long desc about alert', # optional
      # )
      # Alerts are non-blocking.
      # Logic goes here.
      # use _change_waterlevel to accomplish this task.
      self._dataAttributes['lock'].release()
      raise NotImplementedError
   
   def _change_waterlevel (self, changelevel=(-20)):
      # Change water level by adding/removing changelevel amout
      # of water from tank.
      self._dataAttributes['lock'].acquire()
      # For alert, use below:
      # self._dataAttributes['alert'].alert(
      #    attribute='wateroutlet', # required
      #    title='alerttitle', # optional
      #    description='long desc about alert', # optional
      # )
      # Alerts are non-blocking.
      # Logic goes here.
      # keep checking water levels using time.sleep(float)
      # if levels didn't change by significant time, raise alert.
      self._dataAttributes['lock'].release()
      raise NotImplementedError
   
   def _check_unionizedAmmonia (self):
      tan = self._dataAttributes['tan'][0].read('TAN')
      pH = self._dataAttributes['temperaturepH'][0].read('pH')
      temperature = self._dataAttributes['temperaturepH'][0].read(
         key='temperature',
      )
      # Calculate unionizedNH3 as per formula in discussion and check.
      # Check safe ranges.
      # If error, change safety levels:
      # self._dataAttributes['safetyLevels']['unionizedNH3'] = 'safe'
      raise NotImplementedError
   
   def _check_TAN (self):
      tan = self._dataAttributes['tan'][0].read('TAN')
      # Check safe ranges.
      # If error, change safety levels:
      # self._dataAttributes['safetyLevels']['tan'] = 'safe'
      raise NotImplementedError
   
   def _check_pH (self):
      pH = self._dataAttributes['temperaturepH'][0].read('pH')
      # Check safe ranges.
      # If error, change safety levels:
      # self._dataAttributes['safetyLevels']['pH'] = 'safe'
      raise NotImplementedError
   
   def _check_temperature (self):
      temperature = self._dataAttributes['temperaturepH'][0].read(
         key='temperature',
      )
      # Check safe ranges.
      # If error, change safety levels:
      # self._dataAttributes['safetyLevels']['temperature'] = 'safe'
      raise NotImplementedError
   
   def _check_DO (self):
      dO = self._dataAttributes['dO'][0].read('DO')
      # Check safe ranges.
      # If error, change safety levels:
      # self._dataAttributes['safetyLevels']['dO'] = 'safe'
      raise NotImplementedError
   
   def _check_nitrite (self):
      nitrite = self._dataAttributes['spectrophotometer'][0].read('NO2')
      # Check safe ranges.
      # If error, change safety levels:
      # self._dataAttributes['safetyLevels']['NO2'] = 'safe'
      raise NotImplementedError
   
   def _check_nitrate (self):
      nitrate = self._dataAttributes['spectrophotometer'][0].read('NO3')
      # Check safe ranges.
      # If error, change safety levels:
      # self._dataAttributes['safetyLevels']['NO3'] = 'safe'
      raise NotImplementedError
   
   def _check_waterLevel (self):
      waterLevel = self._dataAttributes['waterLevel'][0].read('level')
      # Check safe ranges.
      # If error, change safety levels:
      # self._dataAttributes['safetyLevels']['waterlevel'] = 'safe'
      raise NotImplementedError
# Guard line below: Do NOT exceed 79 character limit per line in any case.
# -----------------------------------------------------------------------------
