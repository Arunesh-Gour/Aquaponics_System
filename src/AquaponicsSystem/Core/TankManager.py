import os
import json

class TankManager:
   def __init__ (self, dirpath):
      if (type(dirpath).__name__ == 'str'):
         if (dirpath == '' or len(dirpath) < 2):
            raise TypeError("dirpath requires 'str' of length >= 2")
      else:
         raise TypeError("dirpath requires 'str' only")
      
      if (not os.path.isdir(dirpath)):
         raise TypeError("'{0}' is not a directory".format(dirpath))
      
      self.dirpath = dirpath
      
      """
      self._dataAttributes = dict([\
         (filename.split('.')[0], os.path.abspath(filename),)\
         for filename in os.listdir(dirpath)\
         if (os.path.isfile(filename)\
            and (filename.split('.')[-1]).lower() == 'json')\
      ])"""
      self._dataAttributes = {}
      
      for filename in os.listdir(dirpath):
         filepath = os.path.join(dirpath, filename)
         if (os.path.isfile(os.path.abspath(filepath))\
            and (filename.split('.')[-1].lower() == 'json')):
            self._dataAttributes[\
               filename.split('.')[0]] = os.path.abspath(filepath)
      self._tanklist = None
   
   def setlist (self, tanklist):
      if (not type(tanklist).__name__ == 'dict'):
         raise TypeError("tanklist requires 'dict'")
      
      self._tanklist = tanklist
   
   def getnames (self):
      return tuple(self._dataAttributes.keys())
   
   def read_values (self, filename):
      with open(self._dataAttributes[filename], 'r') as fh:
         data = json.load(fh)
      
      return data
   
   def write_all (self):
      for filename in self._dataAttributes.keys():
         filepath = self._dataAttributes[filename]
         data = dict([
            (attributename, self._tanklist[filename].read(attributename))\
            for attributename in self._tanklist[filename].read('?')\
         ])
         with open(filepath, 'w') as filehandler:
            json.dump(data, filehandler)
# Guard line below: Do NOT exceed 79 character limit per line in any case.
# -----------------------------------------------------------------------------
