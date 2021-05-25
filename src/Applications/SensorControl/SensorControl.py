# Imports
from tkinter import *
import json

# Constants
FILE_PATH = './'
FILE_NAME = 'system1'

# Function to convert values to float
def getFloat(s):
    return 0 if len(s) == 0 else float(s) 

# Function to update json
def updateJSON():
    waterLevel = getFloat(WaterLevel.get())
    acidity = getFloat(Acidity.get())
    temperature = getFloat(Temperature.get())
    dissolvedOxygen = getFloat(DissolvedOxygen.get())
    dissolvedNitrite = getFloat(DissolvedNitrite.get())
    dissolvedNitrate = getFloat(DissolvedNitrate.get())
    tan = getFloat(Tan.get())
    data = {}
    data['WaterLevel'] = waterLevel 
    data['pH'] = acidity
    data['Temperature'] = temperature
    data['DO'] = dissolvedOxygen
    data['NO2'] =  dissolvedNitrite
    data['NO3'] = dissolvedNitrate
    data['TAN'] = tan
    with open(f'{FILE_PATH}/{FILE_NAME}.json', 'w') as f:
        json.dump(data, f)

# Window configuration
window = Tk()
window.geometry('512x200')
window.title('Sensor System Contols')

# Labels and Enteries for each sensor
waterLevel = Label(window, text = 'Water level:')
WaterLevel = Entry(window)
acidity = Label(window, text = 'pH:')
Acidity = Entry(window)
temperature = Label(window, text='Temperature:')
Temperature = Entry(window)
dissolvedOxygen = Label(window, text='Dissolved Oxygen:')
DissolvedOxygen = Entry(window)
dissolvedNitrite = Label(window, text='Dissolved Nitrite:')
DissolvedNitrite = Entry(window)
dissolvedNitrate = Label(window, text='Dissolved Nitrate:')
DissolvedNitrate = Entry(window)
tan = Label(window, text = 'TAN:')
Tan = Entry(window)
submit = Button(window,text='Update',command = updateJSON)

# Element alignments
waterLevel.grid(row = 0, column = 0)
WaterLevel.grid(row = 0, column = 1)
acidity.grid(row = 1, column = 0)
Acidity.grid(row = 1, column = 1)
temperature.grid(row = 2, column = 0)
Temperature.grid(row = 2, column = 1)
tan.grid(row = 3, column = 0)
Tan.grid(row = 3, column = 1)
dissolvedNitrate.grid(row = 0, column = 3)
DissolvedNitrate.grid(row = 0, column = 4)
dissolvedNitrite.grid(row = 1, column = 3)
DissolvedNitrite.grid(row = 1, column = 4)
dissolvedOxygen.grid(row = 2, column = 3)
DissolvedOxygen.grid(row = 2, column = 4)
submit.grid(row = 5, column = 2)

mainloop()
