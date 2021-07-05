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
    
  def number(self):
    return self._number
