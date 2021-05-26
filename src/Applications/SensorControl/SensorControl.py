# Imports
from tkinter import *
from tkinter.font import names

class SensorControl:
   # Window Configuration
   window = Tk()
   window.geometry('550x200')
   window.title('Sensor System Contols')
   
   # Creating entry variables for each sensor and tank selection
   selectedTank = StringVar()
   selectedTank.set('Select a tank')
   WaterLevel = Entry(window)
   Acidity = Entry(window)
   Temperature = Entry(window)
   DissolvedOxygen = Entry(window)
   DissolvedNitrite = Entry(window)
   DissolvedNitrate = Entry(window)
   Tan = Entry(window)
   
   tanks = []
   
   def setAvailableTanks(self, tanks):
      self.tanks = tanks
   
   # Function to update Selected tank values
   def updateValues(self):
      fishTank = self.core.getTank(self.selectedTank.get())
      
      waterLevel = self.getFloat(self.WaterLevel.get())
      acidity = self.getFloat(self.Acidity.get())
      temperature = self.getFloat(self.Temperature.get())
      dissolvedOxygen = self.getFloat(self.DissolvedOxygen.get())
      dissolvedNitrite = self.getFloat(self.DissolvedNitrite.get())
      dissolvedNitrate = self.getFloat(self.DissolvedNitrate.get())
      tan = self.getFloat(self.Tan.get())
      
      try:
         if (tan != -1):
            fishTank.write('TAN', float(tan), True)
      except:
         pass
      try:
         if (temperature != -1):
            fishTank.write('temperature', float(temperature), True)
      except:
         pass
      try:
         if (acidity != -1):
            fishTank.write('pH', float(acidity), True)
      except:
         pass
      try:
         if (dissolvedOxygen != -1):
            fishTank.write('DO', float(dissolvedOxygen), True)
      except:
         pass
      try:
         if (dissolvedNitrite != -1):
            fishTank.write('NO2', float(dissolvedNitrite), True)
      except:
         pass
      try:
         if (dissolvedNitrate != -1):
            fishTank.write('NO3', float(dissolvedNitrate), True)
      except:
         pass
      try:
         if (waterLevel != -1):
            fishTank.write('waterLevel', float(waterLevel), True)
      except:
         pass
      # NOTE: Use selectedTank.get() to get Tank name
      # print(self.selectedTank.get())
      # Logic to update values
   
   # Function to convert values to float
   def getFloat(self, s):
      return -1 if len(s) == 0 else float(s)
   
   def __init__(self, core):
      self.core = core
      # Load all available tanks
      self.setAvailableTanks(list(self.core.gettanklist()))
      
      # Labels each field
      tankMenu = OptionMenu(self.window, self.selectedTank, *self.tanks)
      waterLevel = Label(self.window, text = 'Water level:')
      acidity = Label(self.window, text = 'pH:')
      temperature = Label(self.window, text='Temperature:')
      dissolvedOxygen = Label(self.window, text='Dissolved Oxygen:')
      dissolvedNitrite = Label(self.window, text='Dissolved Nitrite:')
      dissolvedNitrate = Label(self.window, text='Dissolved Nitrate:')
      tan = Label(self.window, text = 'TAN:')
      submit = Button(self.window, text='Update', command = self.updateValues)
      
      # Aligning labels
      tankMenu.grid(row = 0, column = 2)
      waterLevel.grid(row = 1, column = 0)
      acidity.grid(row = 2, column = 0)
      temperature.grid(row = 3, column = 0)
      dissolvedNitrite.grid(row = 1, column = 3)
      dissolvedOxygen.grid(row = 2, column = 3)
      dissolvedNitrate.grid(row = 3, column = 3)
      tan.grid(row = 4, column = 3)
      submit.grid(row = 6, column = 2)
      
      # Aligning Entries
      self.WaterLevel.grid(row = 1, column = 1)
      self.Acidity.grid(row = 2, column = 1)
      self.Temperature.grid(row = 3, column = 1)
      self.DissolvedNitrite.grid(row = 1, column = 4)
      self.DissolvedOxygen.grid(row = 2, column = 4)
      self.DissolvedNitrate.grid(row = 3, column = 4)
      self.Tan.grid(row = 4, column = 4)
   
   def start (self):
      mainloop()
# s = SensorControl(['TANK_001', 'TANK_002'])
