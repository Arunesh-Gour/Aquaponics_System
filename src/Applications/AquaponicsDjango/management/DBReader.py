import os
import sys

sys.path.append(\
   os.path.abspath(os.path.join(
      os.path.dirname(__file__),
      '..', '..', '..', 'AquaponicsSystem', 'EmulatedHardware',
      'ProjectEssentials',
   ))
)

DBDIR = (\
   os.path.abspath(os.path.join(
      os.path.dirname(__file__),
      '..', '..', 'DB',
   ))
)

import AutoExecutor

dataFiles = {
   # filename : filepath,
}

dataAttributes = {
   # filename : str_containing_json,
}

class DBReader:
   def __init__ (self, dirpath=DBDIR):
      if (type(dirpath).__name__ == 'str'):
         if (dirpath == '' or len(dirpath) < 2):
            raise TypeError("dirpath requires 'str' of length >= 2")
      else:
         raise TypeError("dirpath requires 'str' only")
      
      if (not os.path.isdir(dirpath)):
         raise TypeError("'{0}' is not a directory".format(dirpath))
      
      self.dirpath = dirpath
      
      for filename in os.listdir(dirpath):
         filepath = os.path.join(dirpath, filename)
         if (os.path.isfile(os.path.abspath(filepath))\
            and (filename.split('.')[-1].lower() == 'json')):
            dataFiles[\
               filename.split('.')[0]] = os.path.abspath(filepath)
      
      self.read_all()
      self.executor = AutoExecutor.AutoExecutor(
         exec_function=self.read_all,
         runType='thread',
         times=None,
         interval=1.0,
         autopause=False,
         daemon=True,
      )
   
   def reload (self):
      self.pause()
      
      dataFiles.clear()
      
      for filename in os.listdir(self.dirpath):
         filepath = os.path.join(self.dirpath, filename)
         if (os.path.isfile(os.path.abspath(filepath))\
            and (filename.split('.')[-1].lower() == 'json')):
            dataFiles[\
               filename.split('.')[0]] = os.path.abspath(filepath)
      
      dataAttributes.clear()
      
      self.read_all()
      
      self.resume()
   
   def read_all (self):
      for filename in dataFiles.keys():
         filepath = dataFiles[filename]
         with open(filepath, 'r') as filehandler:
            dataAttributes[filename] = str(filehandler.read())
   
   def start (self):
      if (self.executor.is_alive()):
         self.executor.start()
   
   def kill (self):
      if (self.executor.is_alive()):
         self.executor.kill()
   
   def pause (self):
      if (self.executor.is_alive() and not self.executor.is_paused()):
         self.executor.pause()
   
   def resume (self):
      if (self.executor.is_alive() and self.executor.is_paused()):
         self.executor.resume()
