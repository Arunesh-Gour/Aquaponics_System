import os
import sys
sys.path.append(\
   os.path.abspath(os.path.join(
      os.path.dirname(__file__), '..',
   ))
)
sys.path.append(\
   os.path.abspath(os.path.join(
      os.path.dirname(__file__), '..', 'Applications', 'SensorControl',
   ))
)

import time
import SensorControl
from AquaponicsSystem.Core import Core

# from AquaponicsSystem.EmulatedHardware.ProjectEssentials import AutoExecutor
# from threading import Thread

DBDIR = os.path.abspath(\
   os.path.join(os.path.dirname(__file__), '..', 'Applications', 'DB')
)

core = Core.Core(DBDIR)
sensorControl = SensorControl.SensorControl(core)

core.start()
# sensorThread.start()

"""
def update ():
   os.system('clear')
   for tank in core.gettanklist():
      print(tank)
      ftank = core.getTank(tank)
      for key in ftank.read('?'):
         print(key, ftank.read(key))

updateExecutor = AutoExecutor.AutoExecutor(
   exec_function=update,
   runType='thread',
   times=None,
   interval=1.0,
   autopause=False,
   daemon=True,
)
"""

try:
   # updateExecutor.start()
   sensorControl.start()
   while True:
      time.sleep(1)
except KeyboardInterrupt:
   # updateExecutor.kill()
   core.stop()
   '''
   if (sensorThread.is_alive()):
      sensorThread.join(1.0)
   '''
   exit()
