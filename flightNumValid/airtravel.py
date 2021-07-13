import os
import sys

class Flight:
  def __init__(self, number):
    # class invariants
    if not number[:2].isalpha():
      raise ValueError(f"No Airline Code in '{number}'")
    if not number[:2].isupper():
      raise ValueError(f"Invalid Airline Code in '{number}'")
    if not (number[2:].isdigit() and int(number[2:]) <= 9999):
      raise ValueError(f"Invalid Code in '{number}'")
    self._number = number
    
  def num(self):
    return self._number

class Aircraft:
  def __init__(self, registration, model):
      self._registration = registration
      self._model = model

  def registration(self):
    return(self._registration)
  

x = Flight("SN0010009292992929")
print(Flight.num(x))

