from . import TankManager
from ..AISystems import SimplexAgent
from ..EmulatedHardware.Core import FishTank
from ..EmulatedHardware.ProjectEssentials import AutoExecutor

class Core:
   def __init__ (self, dirpath):
      if (type(dirpath).__name__ == 'str'):
         if (dirpath == '' or len(dirpath) < 2):
            raise TypeError("dirpath requires 'str' of length >= 2")
      else:
         raise TypeError("dirpath requires 'str' only")
      
      self.dirpath = dirpath
      
      self._dataAttributes = {
         "tankManager" : TankManager.TankManager(self.dirpath),
         "tankExecutor" : None,
         "fishTanks" : {},
         "simplexAgents" : {},
      }
      for tankname in self._dataAttributes['tankManager'].getnames():
         fishTank = FishTank.FishTank(tankname)
         self._dataAttributes['fishTanks'][tankname] = fishTank
         simplexAgent = SimplexAgent.SimplexAgent(fishTank)
         self._dataAttributes['simplexAgents'][tankname] = simplexAgent
         
         data = self._dataAttributes['tankManager'].read_values(tankname)
         
         for attribute in fishTank.read('?'):
            fishTank.write(attribute, float(data[attribute]))
      
      self._dataAttributes['tankManager'].setlist(
         self._dataAttributes['fishTanks'],
      )
      
      self._dataAttributes['tankExecutor'] = AutoExecutor.AutoExecutor(
         exec_function=self._dataAttributes['tankManager'].write_all,
         runType='thread',
         times=None,
         interval=1.0,
         autopause=False,
         daemon=True,
      )
   
   def gettanklist (self):
      return tuple(self._dataAttributes['fishTanks'].keys())
   
   def getTank (self, tank):
      if (type(tank).__name__ == 'str'):
         if (tank == '' or len(tank) < 2):
            raise TypeError("tank requires 'str' of length >= 2")
      else:
         raise TypeError("tank requires 'str' only")
      
      return self._dataAttributes['fishTanks'][tank]
   
   def start (self):
      for simplexAgent in self._dataAttributes['simplexAgents'].values():
         simplexAgent.start()
      
      if (self._dataAttributes['tankExecutor'].is_alive()):
         self._dataAttributes['tankExecutor'].start()
   
   def stop (self):
      for simplexAgent in self._dataAttributes['simplexAgents'].values():
         simplexAgent.stop()
      
      if (self._dataAttributes['tankExecutor'].is_alive()):
         self._dataAttributes['tankExecutor'].kill()
# Guard line below: Do NOT exceed 79 character limit per line in any case.
# -----------------------------------------------------------------------------
