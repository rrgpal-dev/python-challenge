# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from itertools import islice
num_of_months = 0
total_amt = 0
monthly_amt = [0.00]
month = [""]
with open ("budget_data.csv") as f:
  for i, x in enumerate(f):
     if i >=1 :
        num_of_months = i
        s = x.split(",")
        month.append(s[0])
        monthly_amt.append(s[1])

    
print("Financial Analysis")
print("---------------------------------------------")
print(f"Total Months: {num_of_months}") 
        
        