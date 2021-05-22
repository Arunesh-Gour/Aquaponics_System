class Signal:
   """Signalling service; handles and dispatches signals.
   
   Signals (calls) a callback function when the set attribute of registered
   object changes its value.
   To be able to dispatch signal, an object must be registered.
   To be able to receive signal, a callback function must be present and
   processed over either another thread/process or should take no more than
   0.1 sec, for other callbacks to receive signals.
   
   Attributes
   ----------
   signalObjects : list
      Stores a dict containing serial ids (str) as keys and another dict as
      values, which contain attribute names (str) as keys and a list as values,
      which contain count of signalIDs and signalIDs which needs to be used
      for signal event if the attribute's value changes, and count of all
      objects currently registered.
   unusedSignalIDs : list
      List of all signalID that were unallocated after being used, and are
      available to be used again. These will be used prior to assigning any
      new signalID.
   signals : list
      Stores a dict with signalID as key and a list as values which contains
      onchange, onexhaust and ondelete callback functions which fires up at
      respective trigger events, times of onchange trigger to fire before
      onexhaust trigger fires, autodelete which triggers auto deletion of
      signal and firing of ondelete event callback; and count of all signals
      stored.
   
   Methods
   -------
   register (serial, attributes)
      Registers objects with signalling service to be able to send signals.
   unregister (serial)
      Unregisters registered object from signalling service.
   updateregistration (serial, attributes, mode='add', new_attributes=None)
      Updates registered objects by adding, deleting or renaming attributes.
   add (serial, attribute, callbacks=None, times=None, autodelete=True)
      Creates new signal and attaches it to provided serial ID and attributes.
   update (signalID, mode='onchange_callback', callback=None, times=None, \
      autodelete=None, serial=None, attribute=None)
      Updates properties of specified signal using signalID.
   remove (signalID, triggerevent=True)
      Removes signal specified using signalID. Triggers ondelete event on
      signal if triggerevent is True.
   signal (serial, attribute)
      Signals all signals attached to specified serial and attribute with
      'onchange' trigger.
   _signal (signalIDs, trigger='onchange')
      Sends appropriate signals as per trigger event for provided signalIDs.
   """
   
   signalObjects = [
      {
         # serial : {
         #    attribute : [0 (count), signalID,],
         # }
      },
      0, # objects count
   ]
   
   unusedSignalIDs = []
   
   signals = [
      {
         # signalID : [
         #    onchange_callback, ondelete_callback, onexhaust_callback,
         #    times, autodelete, serial, attribute,
         # ],
      },
      0, # signals count
   ]
   
   def register (serial, attributes):
      """Registers objects to the signalling service.
      
      Registers object using a unique serial (str) and list of attributes which
      support signals.
      
      Parameters
      ----------
      serial : str
         Unique serial id of the object.
      attributes : list, tuple
         List of all attributes of object supporting signals.
      
      Raises
      ------
      TypeError
         * If serial is not of type 'str'.
         * If attributes is not of type 'list' or 'tuple'.
         * If any attribute in attributes in not of type 'str'.
      ValueError
         * If object with serial id is already registered with the service.
         * If an attribute is repeated again in attributes' list.
      """
      
      if (type(serial).__name__ == 'str'):
         if (serial in (Signal.signalObjects[0]).keys()):
            raise ValueError(\
               "object with serial '{0}' already registered".format(
                  serial,
               )\
            )
      else:
         raise TypeError("serial requires a 'str' value")
      
      if (type(attributes).__name__ == 'tuple' or\
         type(attributes).__name__ == 'list'):
         if (len(attributes) < 1):
            raise TypeError("no attribute supplied, required 'str'")
         
         if (0 in [1 if (type(attribute).__name__ == 'str') else 0\
            for attribute in attributes]):
            raise TypeError("attribute names requires 'str' only")
      else:
         raise TypeError("attributes should be supplied as a 'tuple' or 'list'")
      
      Signal.signalObjects[0][serial] = {}
      
      for attribute in attributes:
         if (attribute in (Signal.signalObjects[0][serial]).keys()):
            (Signal.signalObjects[0]).pop(serial)
            raise ValueError(\
               "repeated attribute '{0}' in atrributes list".format(
                  attribute,
               )\
            )
         Signal.signalObjects[0][serial][attribute] = [0,]
      
      Signal.signalObjects[1] += 1
   
   def unregister (serial):
      """Unregisters objects from signalling service.
      
      Unregisters object registered using a unique serial (str).
      Calls ondelete_callback functions associated with signal ids related to
      the object being deleted.
      
      Parameters
      ----------
      serial : str
         Unique serial id of the object.
      
      Raises
      ------
      TypeError
         * If serial is not of type 'str'.
      ValueError
         * If no object is registered with provided serial id to the service.
      """
      
      if (type(serial).__name__ == 'str'):
         if (serial not in (Signal.signalObjects[0]).keys()):
            raise ValueError(\
               "object with serial '{0}' not registered".format(
                  serial,
               )\
            )
      else:
         raise TypeError("serial requires a 'str' value")
      
      linkedSignalIDs = []
      
      for attributeSignalIDs in (Signal.signalObjects[0][serial]).values():
         if (len(attributeSignalIDs) < 2):
            continue
         for attributeSignalID in attributeSignalIDs[1:]:
            linkedSignalIDs.append(attributeSignalID)
      
      if (len(linkedSignalIDs) > 0):
         Signal._signal(linkedSignalIDs[:], trigger="ondelete")
      
      (Signal.signalObjects[0]).pop(serial)
      Signal.signalObjects[1] -= 1
   
   def updateregistration (serial, attributes, mode="add", new_attributes=None):
      """Updates attributes of registered objects.
      
      Adds, deletes and renames new or already registered attributes of
      registered objects.
      Signals ondelete event to registered signals on deletion of attribute.
      
      Parameters
      ----------
      serial : str
         Serial id of registered object, which needs to be updated.
      attributes : list, tuple
         List of attributes (str) to perform updation on.
      mode : {'add', 'delete', 'rename'}
         Mode / method to perform for updation on attributes.
      new_attributes : list, tuple, optional
         If mode='rename', then populate this with exact number of elements as
         of attributes, in order, where attributes contain old names, and
         new_attributes contain new names.
      
      Raises
      ------
      TypeError
         * Non 'str' serial supplied.
         * Non 'str' mode supplied.
         * Non 'tuple' or 'list' supplied as attributes.
         * No attribute supplied in attributes.
         * Non 'str' attribute in attributes.
         * new_attributes not supplied in rename mode.
         * Non 'tuple' or 'list' supplied as new_attributes in rename mode.
         * No attribute supplied in new_attributes in rename mode.
         * Non 'str' new_attribute in new_attributes in rename mode.
      ValueError
         * Object with serial not registered.
         * Invalid mode.
         * attributes and new_attributes differ in length in rename mode.
         * attributes contain already registered attributes in add mode.
         * attributes contain unregistered attributes in delete mode.
         * attributes contain unregistered attribute in rename mode.
         * conflicting values in (attributes, new_attributes) in rename mode.
      """
      
      if (type(serial).__name__ == 'str'):
         if (serial not in (Signal.signalObjects[0]).keys()):
            raise ValueError(\
               "no object registered with serial '{0}'".format(
                  serial,
               )\
            )
      else:
         raise TypeError("serial requires a 'str' value")
      
      if (type(mode).__name__ == 'str'):
         if (mode not in ("add", "rename", "delete",)):
            raise ValueError("unrecognized mode '{0}'".format(mode))
      else:
         raise TypeError("mode requires a 'str' value")
      
      if (type(attributes).__name__ == 'tuple' or\
         type(attributes).__name__ == 'list'):
         if (len(attributes) < 1):
            raise TypeError("no attribute supplied, required 'str'")
         
         if (0 in [1 if (type(attribute).__name__ == 'str') else 0\
            for attribute in attributes]):
            raise TypeError("attribute names requires 'str' only")
      else:
         raise TypeError("attributes should be supplied as a 'tuple' or 'list'")
      
      if (mode == "rename"):
         if (new_attributes != None):
            if (type(new_attributes).__name__ == 'tuple' or\
               type(new_attributes).__name__ == 'list'):
               if (len(new_attributes) < 1):
                  raise TypeError("no new_attribute supplied, required 'str'")
               
               if (len(attributes) != len(new_attributes)):
                  raise ValueError(\
                     "mismatched lengths of attributes and new_attributes"\
                  )
               
               if (0 in [1 if (type(new_attribute).__name__ == 'str') else 0\
                  for new_attribute in new_attributes]):
                  raise TypeError("attribute names requires 'str' only")
            else:
               raise TypeError(\
                  "new_attributes should be supplied as a 'tuple' or 'list'"\
               )
         else:
            raise TypeError("new_attributes requires 'tuple' or 'list' only")
      else:
         if (new_attributes != None):
            raise TypeError(\
               "new_attributes requires 'NoneType' for current mode"\
            )
      
      if (mode == "add"):
         if (len(list(set((Signal.signalObjects[0][serial]).keys())\
            & set(attributes))) > 0):
            raise ValueError(\
               "attributes contains already registered attributes"\
            )
         
         for attribute in attributes:
            Signal.signalObjects[0][serial][attribute] = [0,]
      elif (mode == "delete"):
         if (len(list(set(attributes)\
            - set((Signal.signalObjects[0][serial]).keys()))) > 0):
            raise ValueError(\
               "attributes contains unrecognized attributes"\
            )
         
         linkedSignalIDs = []
         
         for attribute in attributes:
            if (len(Signal.signalObjects[0][serial][attribute]) < 2):
               continue
            
            for attributeSignalID in\
               Signal.signalObjects[0][serial][attribute][1:]:
               linkedSignalIDs.append(attributeSignalID)
            
            (Signal.signalObjects[0][serial]).pop(attribute)
         
         if (len(linkedSignalIDs) > 0):
            Signal._signal(linkedSignalIDs[:], trigger="ondelete")
      elif (mode == "rename"):
         """
         if (len(list(set((Signal.signalObjects[0][serial]).keys())\
            - set(attributes))) > 0):
            raise ValueError(\
               "attributes contains unrecognized attributes"\
            )
         """
         
         testattributes = []
         
         for attribute, new_attribute in zip(attributes, new_attributes):
            if (attribute not in testattributes and\
               attribute in (Signal.signalObjects[0][serial]).keys()):
               testattributes.append(attribute)
            elif (attribute not in testattributes and\
               attribute not in (Signal.signalObjects[0][serial]).keys()):
               raise ValueError("unrecognized attribute '{0}'".format(\
                     attribute,
                  )\
               )
            
            if (attribute in testattributes):
               testattributes.remove(attribute)
            
            testattributes.append(new_attribute)
         
         if (len(list((set(testattributes) - set(attributes))\
            & set((Signal.signalObjects[0][serial]).keys()))) > 0):
            raise ValueError(\
               "conflicting attributes in (attributes, new_attributes) with"\
               + " registered attributes"\
            )
         
         for attribute, new_attribute in zip(attributes, new_attributes):
            Signal.signalObjects[0][serial][new_attribute] =\
               (Signal.signalObjects[0][serial]).pop(attribute)
   
   def add (serial, attribute, callbacks=None, times=None, autodelete=True):
      """Adds / registers new signal.
      
      Adds new signal to the signalling service.
      
      Parameters
      ----------
      serial : str
         Unique serial ID of target object.
      attribute : str
         Attribute name to target, of target object.
      callbacks : list, tuple
         List of 3 callback functions for [onchange, onexhaust, ondelete]
         events. Can contain 'None' if no callback for respective event(s).
         Callbacks should be either None or callable.
      times : int
         Specific number of times for onchange_callback to be called.
         Set 'None' for unrestricted / infinite number.
      autodelete : bool
         Should signal be deleted automatically once times for onchange
         expires / exhausts.
      
      Raises
      ------
      TypeError
         * Non 'str' serial supplied.
         * Non 'str' attribute supplied.
         * Non 'tuple' or 'list' supplied in callbacks.
         * callbacks list does not contain 3 values.
         * callbacks list contain values other than 'None' and 'callable'.
         * times contain value other than 'None' and 'int'.
         * Non 'bool' autodelete supplied.
      ValueError
         * Invalid serial supplied.
         * Invalid attribute supplied.
         * Large 'int' supplied in times.
         * Corrupt values in signal ID registers.
         * onchange_callback is not supplied or is 'None'.
      
      Returns
      -------
      int
         Returns newSignalID generated for the new signal.
      """
      
      if (type(serial).__name__ == 'str'):
         if (serial not in (Signal.signalObjects[0]).keys()):
            raise ValueError(\
               "no object registered with serial '{0}'".format(
                  serial,
               )\
            )
      else:
         raise TypeError("serial requires a 'str' value")
      
      if (type(attribute).__name__ == 'str'):
         if (attribute not in (Signal.signalObjects[0][serial]).keys()):
            raise ValueError(\
               "unrecognized attribute '{0}' in object serial '{1}'".format(
                  attribute,
                  serial,
               )\
            )
      else:
         raise TypeError("attribute requires a 'str' value")
      
      if (type(callbacks).__name__ == 'tuple' or\
         type(callbacks).__name__ == 'list'):
         if (len(callbacks) < 1):
            raise TypeError("no values supplied, required 3 'callable'")
         
         if (len(callbacks) != 3):
            raise TypeError(\
               "'{0}' values supplied, required only 3 'callable'".format(
                  len(callbacks),
               )\
            )
         
         if (0 in [1 if (callable(callback) or callback == None) else 0\
            for callback in callbacks]):
            raise TypeError("callbacks requires 'callable' only")
         
         if (callbacks[0] == None or not callable(callbacks[0])):
            raise ValueError("onchange_callback is required")
      else:
         raise TypeError("callbacks should be supplied as a 'tuple' or 'list'")
      
      if (times != None):
         if (type(times).__name__ == 'int'):
            if (times < 0 or times > 99999):
               raise ValueError("invalid times' value '{0}'".format(times))
         else:
            raise TypeError("times requires an 'int' value")
      
      if (type(autodelete).__name__ != 'bool'):
         raise TypeError("autodelete requires a 'bool' value")
      
      if (len(Signal.unusedSignalIDs) > 0):
         newSignalID = Signal.unusedSignalIDs.pop()
      else:
         newSignalID = Signal.signals[1]
      
      if (newSignalID not in (Signal.signals[0]).keys()):
         Signal.signals[1] += 1
      else:
         raise ValueError(\
            "conflicting signalID values during new signal registration"\
         )
      
      Signal.signals[0][newSignalID] = [
         callbacks[0], callbacks[1], callbacks[2], times, autodelete,
         serial, attribute,
      ]
      
      Signal.signalObjects[0][serial][attribute][0] += 1
      (Signal.signalObjects[0][serial][attribute]).append(newSignalID)
      
      return newSignalID
   
   def update (signalID, mode='onchange_callback', callback=None, times=None, \
      autodelete=None, serial=None, attribute=None):
      """Updates active signal's properties.
      
      Updates properties of signal using signalID.
      
      Parameters
      ----------
      signalID : int
         Unique signal identifier, whose signal's properties are being changed.
      mode : str, default="onchange_callback"
         Defines which part of signal is to be changed.
      callback : NoneType, callable
         On mode being callback related, this needs to be either 'NoneType' or
         'callable' as per policies.
      times : NoneType, int
         On times being changed, this is either 'NoneType' denoting infinite
         times or unrestricted or 'int' value.
      autodelete : bool
         On autodelete being changed, it must be either True or False.
      serial : NoneType, str
         On remap mode, this needs to be 'str' value for identifying new
         mappable object, else 'NoneType'.
      attribute : NoneType, str
         On remap mode, this needs to be 'str' value for attribute under
         specified object using serial to which signal is being remapped to,
         else 'NoneType'.
      
      Raises
      ------
      TypeError
         * Non 'int' signalID supplied.
         * Non 'str' mode supplied.
         * Non 'NoneType' or non 'callable' callback supplied.
         * Non 'NoneType' or non 'int' times supplied.
         * Non 'bool' autodelete supplied during 'autodelete' mode.
         * Non 'str' serial supplied during 'remap' mode.
         * Non 'str' attribute supplied during 'remap' mode.
      ValueError
         * Invalid signalID.
         * Invalid mode.
         * 'NoneType' supplied to callback in 'onchange_callback' mode.
         * Invalid times.
         * Invalid serial supplied.
         * Invalid attribute supplied.
         * Self remap attempted, old target == new target.
      """
      
      if (type(signalID).__name__ == 'int'):
         if (signalID not in (Signal.signals[0]).keys()):
            raise ValueError("invalid signalID '{0}'".format(signalID))
      else:
         raise TypeError("signalID requires an 'int' value")
      
      if (type(mode).__name__ == 'str'):
         if (mode not in (
                  "onchange_callback", "onexhaust_callback",
                  "ondelete_callback", "times", "autodelete", "remap"
               )\
            ):
            raise ValueError("unrecognized mode '{0}'".format(mode))
      else:
         raise TypeError("mode requires a 'str' value")
      
      if (mode in (
               "onchange_callback", "onexhaust_callback", "ondelete_callback",
            )\
         ):
         if (callback == None or callable(callback)):
            if (mode == "onchange_callback"):
               if (callable(callback)):
                  Signal.signals[0][signalID][0] = callback
               else:
                  raise ValueError("onchange_callback requires a 'callable'")
            elif (mode == "onexhaust_callback"):
               Signal.signals[0][signalID][1] = callback
            elif (mode == "ondelete_callback"):
               Signal.signals[0][signalID][2] = callback
         else:
            raise TypeError("callback requires 'None' or 'callable' value")
      elif (mode == "times"):
         if (times == None or type(times).__name__ == 'int'):
            if (type(times).__name__ == 'int'):
               if (times < 0 or times > 99999):
                  raise ValueError("invalid times' value '{0}'".format(times))
            
            Signal.signals[0][signalID][3] = times
         else:
            raise TypeError("times requires 'None' or 'int' value")
      elif (mode == "autodelete"):
         if (type(autodelete).__name__ == 'bool'):
            Signal.signals[0][signalID][4] = autodelete
         else:
            raise TypeError("autodelete requires a 'bool' value")
      elif (mode == "remap"):
         if (type(serial).__name__ == 'str'):
            if (serial not in (Signal.signalObjects[0]).keys()):
               raise ValueError(\
                  "no object registered with serial '{0}'".format(
                     serial,
                  )\
               )
         else:
            raise TypeError("serial requires a 'str' value")
         
         if (type(attribute).__name__ == 'str'):
            if (attribute not in (Signal.signalObjects[0][serial]).keys()):
               raise ValueError(\
                  "unrecognized attribute '{0}' in object serial '{1}'".format(
                     attribute,
                     serial,
                  )\
               )
         else:
            raise TypeError("attribute requires a 'str' value")
         
         if (serial == Signal.signals[0][signalID][5] and \
            attribute == Signal.signals[0][signalID][6]):
            raise ValueError("attempted self remap")
         
         if (signalID == Signal.signalObjects[0][\
               Signal.signals[0][signalID][5]][\
               Signal.signals[0][signalID][6]][0]):
            Signal.signalObjects[0][Signal.signals[0][signalID][5]][\
               Signal.signals[0][signalID][6]][0] -= 1
            (Signal.signalObjects[0][Signal.signals[0][signalID][5]][\
               Signal.signals[0][signalID][6]][0]).remove(signalID)
         elif (signalID != Signal.signalObjects[0][\
               Signal.signals[0][signalID][5]][\
               Signal.signals[0][signalID][6]][0]):
            (Signal.signalObjects[0][Signal.signals[0][signalID][5]][\
               Signal.signals[0][signalID][6]][0]).remove(signalID)
            Signal.signalObjects[0][Signal.signals[0][signalID][5]][\
               Signal.signals[0][signalID][6]][0] -= 1
         
         Signal.signalObjects[0][serial][attribute][0] += 1
         (Signal.signalObjects[0][serial][attribute]).append(signalID)
         
         Signal.signals[0][signalID][5] = serial
         Signal.signals[0][signalID][6] = attribute
   
   def remove (signalID, triggerevent=True):
      """Removes / unregisters signal.
      
      Unregisters signal associated with signalID from signalling service.
      
      Parameters
      ----------
      signalID : int
         Unique signal ID number.
      triggerevent : bool, default=True
         Fires ondelete_callback if true and if exists.
      
      Raises
      ------
      TypeError
         * Non 'int' signalID supplied.
         * Non 'bool' triggerevent supplied.
      ValueError
         * Invalid signalID supplied.
      """
      
      if (type(signalID).__name__ == 'int'):
         if (signalID not in (Signal.signals[0]).keys()):
            raise ValueError("invalid signalID '{0}'".format(signalID))
      else:
         raise TypeError("signalID requires an 'int' value")
      
      if (type(triggerevent).__name__ != 'bool'):
         raise TypeError("triggerevent requires a 'bool' value")
      
      if (triggerevent == True and Signal.signals[0][signalID][2] != None):
         ondeleteCallback = Signal.signals[0][signalID][2]
      else:
         ondeleteCallback = None
      
      if (Signal.signalObjects[0][Signal.signals[0][signalID][5]][\
         Signal.signals[0][signalID][6]][0] == signalID):
         Signal.signalObjects[0][Signal.signals[0][signalID][5]][\
         Signal.signals[0][signalID][6]][0] -= 1
         (Signal.signalObjects[0][Signal.signals[0][signalID][5]][\
         Signal.signals[0][signalID][6]]).remove(signalID)
      elif (Signal.signalObjects[0][Signal.signals[0][signalID][5]][\
         Signal.signals[0][signalID][6]][0] != signalID):
         (Signal.signalObjects[0][Signal.signals[0][signalID][5]][\
         Signal.signals[0][signalID][6]]).remove(signalID)
         Signal.signalObjects[0][Signal.signals[0][signalID][5]][\
         Signal.signals[0][signalID][6]][0] -= 1
      
      Signal.unusedSignalIDs.append(signalID)
      Signal.signals[1] -= 1
      (Signal.signals[0]).pop(signalID)
      
      if (ondeleteCallback != None):
         ondeleteCallback()
   
   def signal (serial, attribute):
      """Signal dispatcher service.
      
      This signals all signalIDs attached to object's specified attribute.
      
      Parameters
      ----------
      serial : str
         Unique serial ID of object sending signal.
      attribute : str
         Attribute name whose values are changed for signal to be sent.
      
      Raises
      ------
      TypeError
         * Non 'str' serial supplied.
         * Non 'str' attribute supplied.
      ValueError
         * Invalid serial supplied.
         * Invalid attribute supplied.
      """
      
      if (type(serial).__name__ == 'str'):
         if (serial not in (Signal.signalObjects[0]).keys()):
            raise ValueError(\
               "no object registered with serial '{0}'".format(
                  serial,
               )\
            )
      else:
         raise TypeError("serial requires a 'str' value")
      
      if (type(attribute).__name__ == 'str'):
         if (attribute not in (Signal.signalObjects[0][serial]).keys()):
            raise ValueError(\
               "unrecognized attribute '{0}' in object serial '{1}'".format(
                  attribute,
                  serial,
               )\
            )
      else:
         raise TypeError("attribute requires a 'str' value")
      
      linkedSignalIDs = []
      
      if (len(Signal.signalObjects[0][serial][attribute]) > 1):
         for linkedSignalID in Signal.signalObjects[0][serial][attribute][1:]:
            linkedSignalIDs.append(linkedSignalID)
      
      if (len(linkedSignalIDs) > 0):
         Signal._signal(linkedSignalIDs, trigger="onchange")
   
   def _signal (signalIDs, trigger="onchange"):
      """Signalling function.
      
      Private / hidden method.
      Sends signals, to provided signalIDs for provided trigger event.
      Also controls the autodelete and times exhaust mechanisms.
      
      Parameters
      ----------
      signalIDs : tuple, list
         List of signalIDs (int) to send provided trigger signal to.
      trigger : {'onchange', 'onexhaust', 'ondelete'}
         Trigger event for signal to be sent to supplied signalIDs.
      
      Raises
      ------
      TypeError
         * signalIDs is not of type 'tuple' or 'list'.
         * No value provided in signalIDs list.
         * signalIDs contains non 'int' values.
         * Non 'str' value supplied to trigger.
      ValueError
         * Invalid signalID(s) present in signalIDs.
         * Unrecognized trigger event value.
      """
      
      if (type(signalIDs).__name__ == 'tuple' or\
         type(signalIDs).__name__ == 'list'):
         if (len(signalIDs) < 1):
            raise TypeError("no signalID supplied, required 'int'")
         
         if (0 in [1 if (type(signalID).__name__ == 'int') else 0\
            for signalID in signalIDs]):
            raise TypeError("signalID requires 'int' only")
         
         if (len(set(signalIDs) - set((Signal.signals[0]).keys())) > 0):
            raise ValueError("some invalid signalID(s) in signalIDs")
      else:
         raise TypeError("signalIDs should be supplied as a 'tuple' or 'list'")
      
      if (type(trigger).__name__ == 'str'):
         if (trigger not in ("onchange", "onexhaust", "ondelete",)):
            raise ValueError("unrecognized trigger '{0}'".format(trigger))
      else:
         raise TypeError("trigger requires a 'str' value")
      
      if (trigger == "onchange"):
         onchangeCallbacks = []
         onexhaustSignalIDs = []
         
         for signalID in signalIDs:
            if (Signal.signals[0][signalID][3] == None):
               onchangeCallbacks.append(Signal.signals[0][signalID][0])
            else:
               if (Signal.signals[0][signalID][3] > 0):
                  Signal.signals[0][signalID][3] -= 1
                  onchangeCallbacks.append(Signal.signals[0][signalID][0])
                  
                  if (Signal.signals[0][signalID][3] < 1): # times
                     onexhaustSignalIDs.append(signalID)
         
         if (len(onchangeCallbacks) > 0):
            for onchangeCallback in onchangeCallbacks:
               onchangeCallback()
         
         if (len(onexhaustSignalIDs) > 0):
            Signal._signal(onexhaustSignalIDs, trigger="onexhaust")
      elif (trigger == "onexhaust"):
         onexhaustCallbacks = []
         ondeleteSignalIDs = []
         
         for signalID in signalIDs:
            if (Signal.signals[0][signalID][1] !=None): # onexhaust()
               onexhaustCallbacks.append(Signal.signals[0][signalID][1])
            
            if (Signal.signals[0][signalID][4] == True): # autodelete
               ondeleteSignalIDs.append(signalID)
         
         if (len(onexhaustCallbacks) > 0):
            for onexhaustCallback in onexhaustCallbacks:
               onexhaustCallback()
         
         if (len(ondeleteSignalIDs) > 0):
            Signal._signal(ondeleteSignalIDs, trigger="ondelete")
      elif (trigger == "ondelete"):
         Signal.unusedSignalIDs.extend(signalIDs)
         Signal.signals[1] -= len(signalIDs)
         
         ondeleteCallbacks = []
         
         for signalID in signalIDs:
            if (Signal.signals[0][signalID][2] != None): # ondelete
               ondeleteCallbacks.append(Signal.signals[0][signalID][2])
            
            if (signalID == Signal.signalObjects[0][\
                  Signal.signals[0][signalID][5]][\
                  Signal.signals[0][signalID][6]][0]):
               Signal.signalObjects[0][Signal.signals[0][signalID][5]][\
                  Signal.signals[0][signalID][6]][0] -= 1
               (Signal.signalObjects[0][Signal.signals[0][signalID][5]][\
                  Signal.signals[0][signalID][6]]).remove(signalID)
            elif (signalID != Signal.signalObjects[0][\
                  Signal.signals[0][signalID][5]][\
                  Signal.signals[0][signalID][6]][0]):
               (Signal.signalObjects[0][Signal.signals[0][signalID][5]][\
                  Signal.signals[0][signalID][6]]).remove(signalID)
               Signal.signalObjects[0][Signal.signals[0][signalID][5]][\
                  Signal.signals[0][signalID][6]][0] -= 1
            
            (Signal.signals[0]).pop(signalID)
         
         if (len(ondeleteCallbacks) > 0):
            for ondeleteCallback in ondeleteCallbacks:
               ondeleteCallback()
