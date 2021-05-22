import random
from ...ProjectEssentials import (AutoExecutor, Signal,)

class Weather:
   def __init__ (self, externalweathersensor, timespeed=None):
      if (type(externalweathersensor).__name__ != 'ExternalWeather'):
         raise TypeError("externalweathersensor requires 'ExternalWeather'")
      
      if (type(timespeed).__name__ == 'NoneType'\
            or type(timespeed).__name__ == 'int'\
            or type(timespeed).__name__ == 'float'):
         if (timespeed == None):
            timespeed = 1.0
         
         if (timespeed <= 0.0 or timespeed >= 60000.0):
            raise ValueError("invalid timespeed '{0}'".format(timespeed))
      else:
         raise TypeError("timespeed requires 'None' or 'int' or 'float'")
      
      self._dataAttributes = {
         "sensor" : externalweathersensor,
         # event : [eventexecutor, *signalIDs]
         "raining" : [
            AutoExecutor.AutoExecutor(
               exec_function=self.change_raining,
               runType='thread',
               times=None,
               interval=1800.0,
               timespeed=timespeed,
               # autopause=True,
               daemon=True,
            ),
         ],
         "sunlight" : [
            AutoExecutor.AutoExecutor(
               exec_function=self.change_sunlight,
               runType='thread',
               times=None,
               interval=900.0,
               timespeed=timespeed,
               # autopause=True,
               daemon=True,
            ),
         ],
         "temperature" : [
            AutoExecutor.AutoExecutor(
               exec_function=self.change_temperature,
               runType='thread',
               times=None,
               interval=360.0,
               timespeed=timespeed,
               # autopause=True,
               daemon=True,
            ),
         ],
         "humidity" : [
            AutoExecutor.AutoExecutor(
               exec_function=self.change_humidity,
               runType='thread',
               times=None,
               interval=480.0,
               timespeed=timespeed,
               # autopause=True,
               daemon=True,
            ),
         ],
      }
      """
         "randomChanger" : [
            AutoExecutor.AutoExecutor(
               exec_function=self._randomChanger,
               runType='thread',
               times=None,
               interval=600.0,
               timespeed=timespeed,
               autopause=False,
               daemon=True,
            ),
         ],
      }
      
      (self._dataAttributes['raining']).append(
         Signal.Signal.add(
            self._dataAttributes['sensor'].serial,
            'raining',
            [
               self._dataAttributes['raining'][0].resume,
               None,
               None,
            ],
            autodelete=True,
         )
      )
      (self._dataAttributes['raining']).append(
         Signal.Signal.add(
            self._dataAttributes['sensor'].serial,
            'sunlight',
            [
               self._dataAttributes['raining'][0].resume,
               None,
               None,
            ],
            autodelete=True,
         )
      )
      
      (self._dataAttributes['sunlight']).append(
         Signal.Signal.add(
            self._dataAttributes['sensor'].serial,
            'raining',
            [
               self._dataAttributes['sunlight'][0].resume,
               None,
               None,
            ],
            autodelete=True,
         )
      )
      (self._dataAttributes['sunlight']).append(
         Signal.Signal.add(
            self._dataAttributes['sensor'].serial,
            'sunlight',
            [
               self._dataAttributes['sunlight'][0].resume,
               None,
               None,
            ],
            autodelete=True,
         )
      )
      
      (self._dataAttributes['temperature']).append(
         Signal.Signal.add(
            self._dataAttributes['sensor'].serial,
            'raining',
            [
               self._dataAttributes['temperature'][0].resume,
               None,
               None,
            ],
            autodelete=True,
         )
      )
      (self._dataAttributes['temperature']).append(
         Signal.Signal.add(
            self._dataAttributes['sensor'].serial,
            'sunlight',
            [
               self._dataAttributes['temperature'][0].resume,
               None,
               None,
            ],
            autodelete=True,
         )
      )
      (self._dataAttributes['temperature']).append(
         Signal.Signal.add(
            self._dataAttributes['sensor'].serial,
            'temperature',
            [
               self._dataAttributes['temperature'][0].resume,
               None,
               None,
            ],
            autodelete=True,
         )
      )
      
      (self._dataAttributes['humidity']).append(
         Signal.Signal.add(
            self._dataAttributes['sensor'].serial,
            'raining',
            [
               self._dataAttributes['humidity'][0].resume,
               None,
               None,
            ],
            autodelete=True,
         )
      )
      (self._dataAttributes['humidity']).append(
         Signal.Signal.add(
            self._dataAttributes['sensor'].serial,
            'sunlight',
            [
               self._dataAttributes['humidity'][0].resume,
               None,
               None,
            ],
            autodelete=True,
         )
      )
      (self._dataAttributes['humidity']).append(
         Signal.Signal.add(
            self._dataAttributes['sensor'].serial,
            'temperature',
            [
               self._dataAttributes['humidity'][0].resume,
               None,
               None,
            ],
            autodelete=True,
         )
      )
      (self._dataAttributes['humidity']).append(
         Signal.Signal.add(
            self._dataAttributes['sensor'].serial,
            'humidity',
            [
               self._dataAttributes['humidity'][0].resume,
               None,
               None,
            ],
            autodelete=True,
         )
      )
      """
   
   def start (self):
      if (self._dataAttributes['raining'][0].is_alive()):
         self._dataAttributes['raining'][0].start()
      if (self._dataAttributes['sunlight'][0].is_alive()):
         self._dataAttributes['sunlight'][0].start()
      if (self._dataAttributes['temperature'][0].is_alive()):
         self._dataAttributes['temperature'][0].start()
      if (self._dataAttributes['humidity'][0].is_alive()):
         self._dataAttributes['humidity'][0].start()
      # if (self._dataAttributes['randomChanger'][0].is_alive()):
         # self._dataAttributes['randomChanger'][0].start()
   
   def stop (self):
      if (self._dataAttributes['raining'][0].is_alive()):
         self._dataAttributes['raining'][0].kill()
      if (self._dataAttributes['sunlight'][0].is_alive()):
         self._dataAttributes['sunlight'][0].kill()
      if (self._dataAttributes['temperature'][0].is_alive()):
         self._dataAttributes['temperature'][0].kill()
      if (self._dataAttributes['humidity'][0].is_alive()):
         self._dataAttributes['humidity'][0].kill()
      # if (self._dataAttributes['randomChanger'][0].is_alive()):
         # self._dataAttributes['randomChanger'][0].kill()
   
   """
   def _randomChanger (self):
      key = random.choice(['raining', 'sunlight', 'temperature', 'humidity',])
      if (self._dataAttributes[key][0].is_alive()\
         and self._dataAttributes[key][0].is_paused()):
         self._dataAttributes[key][0].resume()
   """
   
   def change_raining (self):
      if (self._dataAttributes['sensor'].read('sunlight')\
         and self._dataAttributes['sensor'].read('raining')):
         self._dataAttributes['sensor'].write(
            key='raining',
            value=random.choice(
               [
                  False, False, False, False, False, False,
                  True, True, True, True,
                  # 40% rain, 60% no rain.
               ],
            ),
         )
      elif (not self._dataAttributes['sensor'].read('sunlight')\
         and self._dataAttributes['sensor'].read('raining')):
         self._dataAttributes['sensor'].write(
            key='raining',
            value=random.choice(
               [
                  False, False, False,
                  True, True, True, True, True, True, True,
                  # 70% rain, 30% no rain.
               ],
            ),
         )
      elif (self._dataAttributes['sensor'].read('sunlight')\
         and not self._dataAttributes['sensor'].read('raining')):
         self._dataAttributes['sensor'].write(
            key='raining',
            value=random.choice(
               [
                  False, False, False, False, False, False, False, False,
                  True, True,
                  # 20% rain, 80% no rain.
               ],
            ),
         )
      elif (not self._dataAttributes['sensor'].read('sunlight')\
         and not self._dataAttributes['sensor'].read('raining')):
         self._dataAttributes['sensor'].write(
            key='raining',
            value=random.choice(
               [
                  False, False, False, False, False,
                  True, True, True, True, True,
                  # 50% rain, 50% no rain.
               ],
            ),
         )
   
   def change_sunlight (self):
      if (self._dataAttributes['sensor'].read('sunlight')\
         and self._dataAttributes['sensor'].read('raining')):
         self._dataAttributes['sensor'].write(
            key='sunlight',
            value=random.choice(
               [
                  False, False, False, False,
                  True, True, True, True, True, True,
                  # 60% sunlight, 40% no sunlight.
               ],
            ),
         )
      elif (not self._dataAttributes['sensor'].read('sunlight')\
         and self._dataAttributes['sensor'].read('raining')):
         self._dataAttributes['sensor'].write(
            key='sunlight',
            value=random.choice(
               [
                  False, False, False, False, False, False, False, False,
                  True, True,
                  # 20% sunlight, 80% no sunlight.
               ],
            ),
         )
      elif (self._dataAttributes['sensor'].read('sunlight')\
         and not self._dataAttributes['sensor'].read('raining')):
         self._dataAttributes['sensor'].write(
            key='sunlight',
            value=random.choice(
               [
                  False, False,
                  True, True, True, True, True, True, True, True,
                  # 80% sunlight, 20% no sunlight.
               ],
            ),
         )
      elif (not self._dataAttributes['sensor'].read('sunlight')\
         and not self._dataAttributes['sensor'].read('raining')):
         self._dataAttributes['sensor'].write(
            key='sunlight',
            value=random.choice(
               [
                  False, False, False, False, False,
                  True, True, True, True, True,
                  # 50% sunlight, 50% no sunlight.
               ],
            ),
         )
   
   def change_temperature (self):
      if (self._dataAttributes['sensor'].read('sunlight')\
         and self._dataAttributes['sensor'].read('raining')):
         self._dataAttributes['sensor'].write(
            key='temperature',
            value=round(
               random.uniform(
                  self._dataAttributes['sensor'].read('temperature')\
                  - (self._temperatureAdjustment() * 3.0),
                  self._dataAttributes['sensor'].read('temperature')\
                  + (self._temperatureAdjustment(True) * 3.0),
               ),
               2,
            ),
         )
      elif (not self._dataAttributes['sensor'].read('sunlight')\
         and self._dataAttributes['sensor'].read('raining')):
         self._dataAttributes['sensor'].write(
            key='temperature',
            value=round(
               random.uniform(
                  self._dataAttributes['sensor'].read('temperature')\
                  - (self._temperatureAdjustment() * 3.0),
                  self._dataAttributes['sensor'].read('temperature')\
                  + (self._temperatureAdjustment() * 2.0),
               ),
               2,
            ),
         )
      elif (self._dataAttributes['sensor'].read('sunlight')\
         and not self._dataAttributes['sensor'].read('raining')):
         self._dataAttributes['sensor'].write(
            key='temperature',
            value=round(
               random.uniform(
                  self._dataAttributes['sensor'].read('temperature')\
                  - (self._temperatureAdjustment(True) * 2.0),
                  self._dataAttributes['sensor'].read('temperature')\
                  + (self._temperatureAdjustment(True) * 3.0),
               ),
               2,
            ),
         )
      elif (not self._dataAttributes['sensor'].read('sunlight')\
         and not self._dataAttributes['sensor'].read('raining')):
         self._dataAttributes['sensor'].write(
            key='temperature',
            value=round(
               random.uniform(
                  self._dataAttributes['sensor'].read('temperature')\
                  - (self._temperatureAdjustment() * 2.0),
                  self._dataAttributes['sensor'].read('temperature')\
                  + (self._temperatureAdjustment(True) * 1.0),
               ),
               2,
            ),
         )
   
   def change_humidity (self):
      if (self._dataAttributes['sensor'].read('sunlight')\
         and self._dataAttributes['sensor'].read('raining')):
         self._dataAttributes['sensor'].write(
            key='humidity',
            value=round(
               random.uniform(
                  50.0 - (self._humidityAdjustment(False, True) * 25.0),
                  50.0 + (self._humidityAdjustment(False, False) * 15.0),
               ),
               2,
            ),
         )
      elif (not self._dataAttributes['sensor'].read('sunlight')\
         and self._dataAttributes['sensor'].read('raining')):
         self._dataAttributes['sensor'].write(
            key='humidity',
            value=round(
               random.uniform(
                  60.0 - (self._humidityAdjustment(True, False) * 5.0),
                  80.0 + (self._humidityAdjustment(True, False) * 15.0),
               ),
               2,
            ),
         )
      elif (self._dataAttributes['sensor'].read('sunlight')\
         and not self._dataAttributes['sensor'].read('raining')):
         self._dataAttributes['sensor'].write(
            key='humidity',
            value=round(
               random.uniform(
                  10.0 - (self._humidityAdjustment(False, True) * 5.0),
                  20.0 + (self._humidityAdjustment(True, False) * 10.0),
               ),
               2,
            ),
         )
      elif (not self._dataAttributes['sensor'].read('sunlight')\
         and not self._dataAttributes['sensor'].read('raining')):
         self._dataAttributes['sensor'].write(
            key='humidity',
            value=round(
               random.uniform(
                  50.0 - (self._humidityAdjustment(True, False) * 25.0),
                  50.0 + (self._humidityAdjustment(False, True) * 25.0),
               ),
               2,
            ),
         )
   
   def _normalize (self, x, low, high):
      return ((x - low)/(high - low))
   
   def _sigmoid (self, x):
      return (1/(1 + (2.71828182846) ** (-x)))
   
   def _temperatureAdjustment (self, invert=False):
      if (type(invert).__name__ != 'bool'):
         raise TypeError("invert requires 'bool'")
      
      temperature = self._dataAttributes['sensor'].read('temperature')
      
      if (temperature >= 40.0 and temperature <= 50.0):
         result = self._normalize(temperature, 45.0, 50.0)
      elif (temperature >= 30.0 and temperature < 40.0):
         result = self._normalize(temperature, 35.0, 40.0)
      elif (temperature >= 20.0 and temperature < 30.0):
         result = self._normalize(temperature, 25.0, 30.0)
      elif (temperature >= 0.0 and temperature < 20.0):
         result = self._normalize(temperature, 10.0, 20.0)
      elif (temperature >= -20.0 and temperature < 0.0):
         result = self._normalize(temperature, -10.0, 0.0)
      
      result *= 7.0
      
      return (self._sigmoid(-result if (invert) else result))
   
   def _humidityAdjustment (self, invert=True, highRate=True):
      if (type(invert).__name__ != 'bool'):
         raise TypeError("invert requires 'bool'")
      
      if (type(highRate).__name__ != 'bool'):
         raise TypeError("highRate requires 'bool'")
      
      temperature = self._dataAttributes['sensor'].read('temperature')
      humidity = self._dataAttributes['sensor'].read('humidity')
      
      result = self._normalize(temperature, 20.0, 50.0) * 7.0
      
      result = (self._sigmoid(-result if (invert) else result))
      result = self._normalize((result * humidity), 50.0, 100.0) * 7.0
      
      return (self._sigmoid(result if (highRate) else -result))
