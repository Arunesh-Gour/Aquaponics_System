import time
from multiprocessing import (Lock,)
from threading import Thread

class AutoExecutor:
   """Automatically executes a function as per instructions.
   
   Executes provided function in provided intervals, either indefinitely or
   for certain number of times, until instructed to stop.
   Executes in non-blocking or blocking manner depending on runType specified.
   
   Attributes
   ----------
   _requiredAttributes : dict
      Set of all attributes and data required by autoexecutor.
   
   Methods
   -------
   __init__ (exec_function, runType=None, times=None, interval=None,\
         timespeed=None, autopause=False, daemon=False, args=None, kwargs=None)
      Initializes and sets up the executor.
   start ()
      Runs the executor.
      Dead executors can't be started.
   kill ()
      Kills the executor.
      Dead executors can't be killed.
   pause ()
      Pause the executor.
      Dead executors can't be paused.
   resume ()
      Resumes the executor from the point where it was paused.
      Dead executors can't be resumed.
   is_alive ()
      Return if the executor is alive or dead.
   is_paused ()
      Return if the executor is paused or not.
   _autoexecute ()
      Core part of AutoExecutor. This runs during execution.
   """
   
   def __init__ (self, exec_function, runType=None, times=None, interval=None,
      timespeed=None, autopause=False, daemon=False, args=None, kwargs=None):
      """Initializes and sets-up the executor.
      
      Parameters
      ----------
      exec_function : callable
         Callable, to be called automatically.
      runType : {'sequential', 'thread',}
         Specifies how to run the executor in - sequential mode (blocking), or
         using threads (non-blocking).
      times : NoneType, int
         Specifies how many times to execute the callable.
         NoneType specifies indefinitely.
      interval : int, float, default=1.0
         Specifies timegap between 2 executions of callable.
      timespeed : int, float, default=1.0
         Specifies the speed of time flowing; to speed up time.
         Though full-fillable by interval, this help preserve some thoughts.
      autopause : bool
         Specifies whether to pause the executor automatically after one
         execution.
      daemon : bool
         Specifies whether to make executor daemonic, if runType is 'thread'.
      args : NoneType, tuple, list
         Set of args, to be passed to exec_function during execution.
      kwargs : NoneType, dict
         Set of keyed args (kwargs), to be passed to exec_function during
         execution.
      
      Raises
      ------
      TypeError
         *  Non 'callable' exec_function.
         *  Non 'str' runType.
         *  Non 'int' times.
         *  Non 'int' or 'float' interval.
         *  Non 'int' or 'float' timespeed.
         *  Non 'bool' autopause.
         *  Non 'bool' daemon.
         *  Non 'tuple' or 'list' args.
         *  Non 'tuple' or 'list' kwargs.
      ValueError
         *  Invalid runType.
         *  Invalid times.
         *  Invalid interval.
         *  Invalid timespeed.
         *  Invalid args.
         *  Invalid kwargs.
      """
      
      if (not callable(exec_function)):
         raise TypeError("exec_function is not callable")
      
      if (type(runType).__name__ == 'str'\
            or type(runType).__name__ == 'NoneType'):
         if (runType == None):
            runType = 'sequential'
         
         if (runType not in ('sequential', 'thread',)):
            raise ValueError("invalid runType '{0}'".format(runType))
      else:
         raise TypeError("runType requires 'None' or 'str'")
      
      if (type(times).__name__ == 'NoneType'\
            or type(times).__name__ == 'int'):
         if (times != None):
            if (times <= 0 or times >= 60000):
               raise ValueError("invalid times '{0}'".format(times))
      else:
         raise TypeError("times requires 'None' or 'int'")
      
      if (type(interval).__name__ == 'NoneType'\
            or type(interval).__name__ == 'int'\
            or type(interval).__name__ == 'float'):
         if (interval == None):
            interval = 1.0
         
         if (interval <= 0.0 or interval >= 60000.0):
            raise ValueError("invalid interval '{0}'".format(interval))
      else:
         raise TypeError("interval requires 'None' or 'int' or 'float'")
      
      if (type(timespeed).__name__ == 'NoneType'\
            or type(timespeed).__name__ == 'int'\
            or type(timespeed).__name__ == 'float'):
         if (timespeed == None):
            timespeed = 1.0
         
         if (timespeed <= 0.0 or timespeed >= 60000.0):
            raise ValueError("invalid timespeed '{0}'".format(timespeed))
      else:
         raise TypeError("timespeed requires 'None' or 'int' or 'float'")
      
      if (type(autopause).__name__ != 'bool'):
         raise TypeError("autopause requires 'bool'")
      
      if (type(daemon).__name__ != 'bool'):
         raise TypeError("daemon requires 'bool'")
      
      if (type(args).__name__ == 'NoneType'\
            or type(args).__name__ == 'tuple'\
            or type(args).__name__ == 'list'):
         if (args == None):
            args = None
         elif (args != None and len(args) < 1):
            raise ValueError("invalid args".format(args))
      else:
         raise TypeError("args requires 'None' or 'tuple' or 'list'")
      
      if (type(kwargs).__name__ == 'NoneType'\
            or type(kwargs).__name__ == 'dict'):
         if (kwargs == None):
            kwargs = None
         elif (kwargs != None and len(kwargs) < 1):
            raise ValueError("invalid kwargs".format(kwargs))
      else:
         raise TypeError("kwargs requires 'None' or 'dict'")
      
      if (args == None):
         args=()
      
      if (kwargs == None):
         kwargs={}
      
      if (runType == 'sequential'):
         runtimeController = None
      elif (runType == 'thread'):
         runtimeController = Thread(
            target=self._autoexecute,
            daemon=daemon,
         )
      
      self._requiredAttributes = {
         "kill" : False,
         "paused" : False,
         "lock" : Lock(),
         "runType" : runType,
         "runtimeController" : runtimeController,
         "exec_function": exec_function,
         "autopause" : autopause,
         "args" : args,
         "kwargs" : kwargs,
         "times" : times,
         "interval" : interval,
         "timespeed" : timespeed,
         "sleeptime" : float(interval / timespeed),
      }
   
   def start (self):
      """Runs the executor.
      
      Runs the autoexecutor in blocking or non-blocking mode as set-up.
      
      Raises
      ------
      RuntimeError
         Raises when executor is already dead.
      """
      
      if (self.is_alive()):
         if (self._requiredAttributes['runtimeController'] == None):
            self._autoexecute()
         else:
            self._requiredAttributes['runtimeController'].start()
      else:
         raise RuntimeError("tried to start a dead "\
            + (
                  'sequence'\
                  if (self._requiredAttributes['runType'] == 'sequential')\
                  else self._requiredAttributes['runType']\
            )\
         )
   
   def kill (self):
      """Kills the executor.
      
      Un-pauses the executor and kills it.
      
      Raises
      ------
      RuntimeError
         Raises when executor is already dead.
      """
      
      if (self.is_alive()):
         if (self.is_paused()):
            self.resume()
         
         self._requiredAttributes['kill'] = True
      else:
         raise RuntimeError("tried to kill a dead "\
            + (
                  'sequence'\
                  if (self._requiredAttributes['runType'] == 'sequential')\
                  else self._requiredAttributes['runType']\
            )\
         )
   
   def pause (self):
      """Pauses the executor.
      
      Pauses the executor, temporarily.
      
      Raises
      ------
      RuntimeError
         Raises when executor is already dead.
      """
      
      if (self.is_alive()):
         if (not self.is_paused()):
            self._requiredAttributes['lock'].acquire()
            self._requiredAttributes['paused'] = True
      else:
         raise RuntimeError("tried to pause a dead "\
            + (
                  'sequence'\
                  if (self._requiredAttributes['runType'] == 'sequential')\
                  else self._requiredAttributes['runType']\
            )\
         )
   
   def resume (self):
      """Resumes the executor.
      
      Resumes the paused executor service from the point where it was paused.
      
      Raises
      ------
      RuntimeError
         Raises when executor is already dead.
      """
      
      if (self.is_alive()):
         if (self.is_paused()):
            self._requiredAttributes['paused'] = False
            self._requiredAttributes['lock'].release()
      else:
         raise RuntimeError("tried to resume a dead "\
            + (
                  'sequence'\
                  if (self._requiredAttributes['runType'] == 'sequential')\
                  else self._requiredAttributes['runType']\
            )\
         )
   
   def is_alive (self):
      """Returns whether the executor is alive.
      
      Checks if executor is alive and available to pause / resume or other
      operations.
      
      Returns
      -------
      bool
         Returns whether the executor is alive.
      """
      
      return not self._requiredAttributes['kill']
   
   def is_paused (self):
      """Returns whether the executor is paused.
      
      Checks if the executor is temporarily paused, only if it is alive.
      
      Returns
      -------
      bool
         Returns whether the executor is temporarily paused, if it is alive.
      """
      
      if (self.is_alive()):
         return self._requiredAttributes['paused']
      else:
         return False
   
   def _autoexecute (self):
      """Core of AutoExecutor.
      
      Automatically executes the exec_function as per set-up.
      Kills self if the times expires.
      """
      
      while self._requiredAttributes['kill'] == False:
         if (self._requiredAttributes['times'] == None\
               or self._requiredAttributes['times'] > 0):
            time.sleep(self._requiredAttributes['sleeptime'])
            
            if (not self.is_alive()):
               break
            
            self._requiredAttributes['lock'].acquire()
            
            if (self._requiredAttributes['times'] != None):
               self._requiredAttributes['times'] -= 1
            
            args = self._requiredAttributes['args']
            kwargs = self._requiredAttributes['kwargs']
            
            self._requiredAttributes['exec_function'](*args, **kwargs)
            
            self._requiredAttributes['lock'].release()
            
            if (self._requiredAttributes['autopause']):
               if (self.is_alive() and not self.is_paused()\
                  and (self._requiredAttributes['times'] == None\
                     or self._requiredAttributes['times'] > 0)\
                  ):
                  self.pause()
         else:
            self.kill()
      
      if (self.is_alive()):
         self.kill()
