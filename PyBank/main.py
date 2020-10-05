# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from itertools import islice
num_of_months = 0

with open ("budget_data.csv") as f:
  for i, x in enumerate(f):
     if i >=1 :
        num_of_months = i
        
        
        
print("Financial Analysis")
print("---------------------------------------------")
print(f"Number of Monthsnum_of_months: {num_of_months}) 
        
        