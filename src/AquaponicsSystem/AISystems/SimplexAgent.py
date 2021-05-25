import time
from ..EmulatedHardware.ProjectEssentials import (AutoExecutor)

class SimplexAgent:
   factorTable = {
      7.0 : {
         10.0 : 0.18,
         16.0 : 0.294,
         18.0 : 0.342,
         20.0 : 0.396,
         21.0 : 0.425,
         22.0 : 0.457,
         24.5 : 0.546,
         26.0 : 0.607,
         28.0 : 0.697,
         30.0 : 0.799,
         32.0 : 0.95,
      },
      7.2 : {
         10.0 : 0.29,
         16.0 : 0.466,
         18.0 : 0.540,
         20.0 : 0.625,
         21.0 : 0.673,
         22.0 : 0.723,
         24.5 : 0.863,
         26.0 : 0.958,
         28.0 : 1.10,
         30.0 : 1.25,
         32.0 : 1.25,
      },
      7.4 : {
         10.0 : 0.46,
         16.0 : 0.736,
         18.0 : 0.854,
         20.0 : 0.988,
         21.0 : 1.06,
         22.0 : 1.14,
         24.5 : 1.36,
         26.0 : 1.50,
         28.0 : 1.73,
         30.0 : 1.98,
         32.0 : 2.36,
      },
      7.6 : {
         10.0 : 0.73,
         16.0 : 1.16,
         18.0 : 1.35,
         20.0 : 1.56,
         21.0 : 1.67,
         22.0 : 1.80,
         24.5 : 2.14,
         26.0 : 2.36,
         28.0 : 2.72,
         30.0 : 3.11,
         32.0 : 3.11,
      },
      7.8 : {
         10.0 : 1.16,
         16.0 : 1.82,
         18.0 : 2.12,
         20.0 : 2.44,
         21.0 : 2.63,
         22.0 : 2.80,
         24.5 : 3.35,
         26.0 : 3.68,
         28.0 : 4.24,
         30.0 : 4.84,
         32.0 : 4.84,
      },
      8.0 : {
         10.0 : 1.82,
         16.0 : 2.86,
         18.0 : 3.31,
         20.0 : 3.82,
         21.0 : 4.10,
         22.0 : 4.39,
         24.5 : 5.21,
         26.0 : 5.75,
         28.0 : 6.56,
         30.0 : 7.46,
         32.0 : 8.77,
      },
      8.2 : {
         10.0 : 2.86,
         16.0 : 4.45,
         18.0 : 5.16,
         20.0 : 5.92,
         21.0 : 6.34,
         22.0 : 6.79,
         24.5 : 8.01,
         26.0 : 8.75,
         28.0 : 10.0,
         30.0 : 11.3,
         32.0 : 13.2,
      },
      8.4 : {
         10.0 : 4.45,
         16.0 : 6.88,
         18.0 : 7.93,
         20.0 : 9.07,
         21.0 : 9.69,
         22.0 : 10.3,
         24.5 : 12.1,
         26.0 : 13.0,
         28.0 : 15.0,
         30.0 : 16.8,
         32.0 : 19.5,
      },
      8.6 : {
         10.0 : 6.88,
         16.0 : 10.5,
         18.0 : 12.0,
         20.0 : 13.7,
         21.0 : 14.5,
         22.0 : 15.5,
         24.5 : 17.9,
         26.0 : 19.4,
         28.0 : 21.8,
         30.0 : 24.3,
         32.0 : 27.7,
      },
      8.8 : {
         10.0 : 10.5,
         16.0 : 15.7,
         18.0 : 17.8,
         20.0 : 20.0,
         21.0 : 21.2,
         22.0 : 22.5,
         24.5 : 25.7,
         26.0 : 27.8,
         28.0 : 30.7,
         30.0 : 33.7,
         32.0 : 37.8,
      },
      9.0 : {
         10.0 : 15.6,
         16.0 : 22.7,
         18.0 : 25.6,
         20.0 : 28.4,
         21.0 : 29.9,
         22.0 : 31.5,
         24.5 : 35.5,
         26.0 : 37.7,
         28.0 : 41.2,
         30.0 : 44.6,
         32.0 : 49.0,
      },
      9.2 : {
         10.0 : 22.7,
         16.0 : 31.8,
         18.0 : 35.2,
         20.0 : 38.6,
         21.0 : 40.4,
         22.0 : 42.1,
         24.5 : 46.5,
         26.0 : 49.2,
         28.0 : 63.8,
         30.0 : 66.1,
         32.0 : 70.8,
      },
      9.4 : {
         10.0 : 31.8,
         16.0 : 42.5,
         18.0 : 46.3,
         20.0 : 49.9,
         21.0 : 51.8,
         22.0 : 53.5,
         24.5 : 58.0,
         26.0 : 60.5,
         28.0 : 63.8,
         30.0 : 66.9,
         32.0 : 70.7,
      },
      9.6 : {
         10.0 : 42.5,
         16.0 : 53.9,
         18.0 : 57.7,
         20.0 : 61.3,
         21.0 : 63.0,
         22.0 : 64.6,
         24.5 : 68.5,
         26.0 : 70.8,
         28.0 : 73.6,
         30.0 : 76.2,
         32.0 : 85.9,
      },
      9.8 : {
         10.0 : 53.9,
         16.0 : 65.0,
         18.0 : 68.4,
         20.0 : 71.6,
         21.0 : 72.9,
         22.0 : 74.3,
         24.5 : 77.6,
         26.0 : 79.4,
         28.0 : 81.6,
         30.0 : 83.6,
         32.0 : 85.9,
      },
      10.0 : {
         10.0 : 65.0,
         16.0 : 74.6,
         18.0 : 77.4,
         20.0 : 79.9,
         21.0 : 81.0,
         22.0 : 82.1,
         24.5 : 84.5,
         26.0 : 85.9,
         28.0 : 87.5,
         30.0 : 89.0,
         32.0 : 90.6,
      },
   }
   
   def __init__ (self, fishtank):
      if (type(fishtank).__name__ != 'FishTank'):
         raise TypeError("fishtank requires 'FishTank'")
      
      self._dataAttributes = {
         "fishtank" : fishtank,
         "executor" : AutoExecutor.AutoExecutor(
            exec_function=self._checkLevels,
            runType='thread',
            times=None,
            interval=5.0,
            autopause=True,
            daemon=True,
         ),
         "executorResume" : None,
      }
      self._dataAttributes["executorResume"] = AutoExecutor.AutoExecutor(
         exec_function=self.resume,
         runType='thread',
         times=None,
         interval=1.0,
         autopause=False,
         daemon=True,
      )
   
   def resume (self):
      if (self._dataAttributes['executor'].is_alive()):
         if (self._dataAttributes['executor'].is_paused()):
            self._dataAttributes['executor'].resume()
   
   def start (self):
      if (self._dataAttributes['executor'].is_alive()):
         self._dataAttributes['executor'].start()
      
      if (self._dataAttributes['executorResume'].is_alive()):
         self._dataAttributes['executorResume'].start()
   
   def stop (self):
      if (self._dataAttributes['executor'].is_alive()):
         self._dataAttributes['executor'].kill()
      
      if (self._dataAttributes['executorResume'].is_alive()):
         self._dataAttributes['executorResume'].kill()
   
   def _checkLevels (self):
      self._dataAttributes['fishtank'].blocker = True
      dO = self._dataAttributes['fishtank'].read('DO')
      nO2 = self._dataAttributes['fishtank'].read('NO2')
      nO3 = self._dataAttributes['fishtank'].read('NO3')
      tan = self._dataAttributes['fishtank'].read('TAN')
      temperature = self._dataAttributes['fishtank'].read('temperature')
      pH = self._dataAttributes['fishtank'].read('pH')
      waterLevel = self._dataAttributes['fishtank'].read('waterLevel')
      pHDiff = [\
         (pH - pHVal) if (pH > pHVal) else (pHVal - pH)\
         for pHVal in SimplexAgent.factorTable.keys()\
      ]
      pHDiff.sort()
      pHDiff = pHDiff[0]
      if ((pHDiff + pH) in SimplexAgent.factorTable.keys()):
         pHDiff += pH
      else:
         pHDiff -= pH
      """
      pHDiff = (\
         (pHDiff + pH) if ((pHDiff + pH) in SimplexAgent.factorTable.keys())\
         else (pHDiff - pH)\
      )"""
      tempDiff = [\
         (temperature - temperatureVal)\
         if (temperature > temperatureVal)\
         else (temperatureVal - temperature)\
         for temperatureVal in SimplexAgent.factorTable[7.0].keys()\
      ]
      tempDiff.sort()
      tempDiff = tempDiff[0]
      if ((tempDiff + temperature) in SimplexAgent.factorTable[7.0].keys()):
         tempDiff += temperature
      else:
         tempDiff -= temperature
      """
      tempDiff = (\
         (tempDiff + temperature)\
         if ((tempDiff + temperature)\
            in SimplexAgent.factorTable[7.0].keys())\
         else (tempDiff - temperature)\
      )"""
      pHDiff = pHDiff if (pHDiff > 0) else -pHDiff
      tempDiff = tempDiff if (tempDiff > 0) else -tempDiff
      unionizedNH3 = tan * SimplexAgent.factorTable[pHDiff][tempDiff]
      self._dataAttributes['fishtank'].write(
         'unionizedNH3', unionizedNH3,
      )
      
      # Check values.
      if ((pH < 6.8) or (pH > 7.0)):
         self._change_pH(pH)
         time.sleep(5.0)
         return
      
      if ((temperature < 27.0) or (temperature > 29.0)):
         self._change_temperature(temperature)
         time.sleep(3.0)
         return
      
      if ((tan > 1.0)\
            or (dO < 6.5)\
            or ((nO2 < 0.5) or (nO2 > 1.0))\
            or ((nO3 < 10.0) or (nO3 > 100.0))\
            or (unionizedNH3 > 0.3)\
         ):
         self._change_water(35.0)
         time.sleep(2.0)
         return
      
      if (waterLevel < 70.0 or waterLevel > 80.0):
         changepercent = 78.0 - waterLevel
         self._change_waterlevel(changepercent, True)
         return
      
      self._dataAttributes['fishtank'].blocker = False
   
   def _change_pH (self, pH):
      # Change pH.
      time.sleep(1.0)
      self._dataAttributes['fishtank'].write('pH', 7.0)
   
   def _change_temperature (self, temperature):
      # Change pH.
      changepercent = 28.0 - temperature
      pchanges = -(-changepercent//2.0)
      pchanges = pchanges if (pchanges > 0) else -pchanges
      for _ in range(0, int(pchanges)):
         self._dataAttributes['fishtank'].write(
            'temperature',
            (self._dataAttributes['fishtank'].read('temperature')
            + 2.0),
         )
         time.sleep(1.0)
      self._dataAttributes['fishtank'].write(
         'temperature', 28.0,
      )
   
   def _change_water (self, changepercent=20.0):
      # Change changepercent amount of water from tank.
      self._change_waterlevel(-changepercent)
      self._change_waterlevel(changepercent, True)
      
      self._dataAttributes['fishtank'].write('DO', 8.0)
      self._dataAttributes['fishtank'].write('NO2', 0.6)
      self._dataAttributes['fishtank'].write('NO3', 25.0)
      self._dataAttributes['fishtank'].write('TAN', 0.2)
   
   def _change_waterlevel (self, changelevel=20.0, leveller=False):
      # Change water level by adding/removing changelevel amout
      # of water from tank.
      if (changelevel > 0):
         watervalve = self._dataAttributes['fishtank'].get(
            'actuators', 'waterinlet',
         )
      else:
         watervalve = self._dataAttributes['fishtank'].get(
            'actuators', 'wateroutlet',
         )
      maxFlow = watervalve.read('maxFlow')
      currentlevel = self._dataAttributes['fishtank'].read('waterLevel')
      watervalve.write('valve', 100.0)
      pchanges = int(-(-changelevel // maxFlow))
      pchanges = pchanges if (pchanges > 0) else -pchanges
      
      for _ in range(0, pchanges):
         self._dataAttributes['fishtank'].write(
            'waterLevel',
            (self._dataAttributes['fishtank'].read('waterLevel')
            + (maxFlow if (changelevel > 0) else -maxFlow)),
         )
         time.sleep(1.0)
      if (leveller):
         self._dataAttributes['fishtank'].write(
            'waterLevel', 78.0,
         )
      watervalve.write('valve', 0.0)
      """
      newlevel = currentlevel + changelevel
      
      if (newlevel >= 50.0 and newlevel <= 80.0):
         for _ in range(0, int(pchangelevel/maxFlow)):
            self._dataAttributes['fishtank'].write(
               'waterLevel',
               (self._dataAttributes['fishtank'].read('waterLevel')
               + (maxFlow if (changelevel > 0) else -maxFlow)),
            )
            time.sleep(1.0)
         self._dataAttributes['fishtank'].write(
            'waterLevel', 75.0,
         )"""
# Guard line below: Do NOT exceed 79 character limit per line in any case.
# -----------------------------------------------------------------------------
