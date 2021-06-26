# Date: 20th June, 2021
# Project: Matchmaker (Elements in Periodic Table)
# Perhaps, secondary school students may find this game interesting for them to revise for the chemical symbols listed in the periodic table.
# Ref.: https://www.youtube.com/watch?v=8PeqZMBCsCc
# Ref.: https://www.youtube.com/watch?v=qVZ5G2-lajE&t=8s

import random
import time
from tkinter import Tk, Button, DISABLED

# Create the Tk Window
root = Tk()
root.title('Matchmaker 2021')
root.resizable(width = False, height = False)

# Variable initialization
buttons = {}
first = True
previousX = 0
previousY = 0

button_symbols = {} 
symbols = ['H',  'Hydrogen',  'He', 'Helium',  'Li', 'Lithium',     'Be', 'Beryllium',
           'B',  'Boron',     'C',  'Carbon',  'N',  'Nitrogen',    'O',  'Oxygen',
           'F',  'Fluorine',  'Ne', 'Neon',    'Na', 'Sodium',      'Mg', 'Magnesium', 
           'Al', 'Aluminium', 'Si', 'Silicon', 'P',  'Phosphorous', 'S',  'Sulphur',
           'Cl', 'Chlorine',  'Ar', 'Argon',   'K',  'Potassium',   'Ca', 'Calcium',
           'Cu', 'Copper',    'Zn', 'Zinc',    'Br', 'Bromine',     'I',  'Iodine']


# A dictionary of elemental symbols
dict =    {'H':  'Hydrogen',  'He': 'Helium',  'Li': 'Lithium',     'Be': 'Beryllium',
           'B':  'Boron',     'C':  'Carbon',  'N':  'Nitrogen',    'O':  'Oxygen',
           'F':  'Fluorine',  'Ne': 'Neon',    'Na': 'Sodium',      'Mg': 'Magnesium', 
           'Al': 'Aluminium', 'Si': 'Silicon', 'P':  'Phosphorous', 'S':  'Sulphur',
           'Cl': 'Chlorine',  'Ar': 'Argon',   'K':  'Potassium',   'Ca': 'Calcium',
           'Cu': 'Copper',    'Zn': 'Zinc',    'Br': 'Bromine',     'I':  'Iodine'}

print(symbols)
print(dict['H'], dict['He'], dict['Li'])

# Randomize the predefined symbols
random.shuffle(symbols)
print(symbols)

def show_symbol(x, y):
  global first
  global previousX, previousY

  print(first)
  print(previousX)
  print(previousY)

  buttons[x, y]['text'] = button_symbols[x, y]
  buttons[x, y].update_idletasks()

  if first:
    previousX = x
    previousY = y
    first = False
  elif previousX != x or previousY != y:
    # if not matched, give 0.5 s for memorizing the icon
    # if buttons[previousX, previousY]['text'] != buttons[x, y]['text']:
    element1 = ''
    element2 = ''
    B1 = buttons[previousX, previousY]['text']
    B2 = buttons[x, y]['text']
    if len(B1)<= 2:
      element1 = dict[B1]
    if len(B2)<= 2:
      element2 = dict[B2]
      
    if (B1 == element2 or B2 == element1):
      # if patterns are matched, disable the two buttons
      buttons[previousX, previousY]['command'] = DISABLED
      buttons[x, y]['command'] = DISABLED
    else:
      time.sleep(0.5)
      buttons[previousX, previousY]['text'] = ''
      buttons[x, y]['text'] = ''
    first = True

# Create a 8x6 array buttons
for x in range(8):
  for y in range(6):
    button = Button(command = lambda x = x, y = y: show_symbol(x, y), width = 10, height = 5)
    button.grid(column = x, row = y)
    buttons[x, y] = button
    button_symbols[x, y] = symbols.pop()

# Tk mainloop here
root.mainloop
