import os
import time
from .Core import Core
from threading import Thread

DBDIR = os.path.join('.', 'Applications', 'DB')

core = Core.Core(DBDIR)

"""
sensorController = SensorController(core)

sensorThread = Thread(
   target=sensorController.run,
)
"""

core.start()
# sensorThread.start()

try:
   while True:
      time.sleep(1)
except KeyboardInterrupt:
   core.stop()
   # if (sensorThread.is_alive()):
   #    sensorThread.join(1.0)
