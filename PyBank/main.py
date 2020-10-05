# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
from itertools import islice
num_of_months = 0
total_amt = 0
monthly_amt = [0.00]
month = [""]
monthly_change = [0.00]
previous_mth_amt = 0.00
with open ("budget_data.csv") as f:
  for i, x in enumerate(f):
     if i >=1 :
        num_of_months = i
        s = x.split(",")
        month.append(s[0])
        monthly_amt.append(float(s[1]))
        monthly_change.append(float(s[1]) - previous_mth_amt)
        previous_mth_amt = float(s[1])
 
        
avg_month_val = sum(monthly_change)/len(monthly_change)
Great_increase = max(monthly_change)
Great_month_idx = monthly_change.index(Great_increase)
Great_month = month[Great_month_idx]

print("Financial Analysis")
print("---------------------------------------------")
print(f"Total Months: {num_of_months}") 
print(f"Total: ${sum(monthly_amt)}")
print(f"Average Change:$ {avg_month_val}")
print(Great_month)
        
        