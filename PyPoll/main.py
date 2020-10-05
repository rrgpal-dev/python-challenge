#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:52:53 2020

@author: N457149 - Raj Ramachandran
"""
i = 0
with open ("election_data.csv") as f:
  for i, x in enumerate(f):
     if i >=1 :
        num_of_voters= i
        s = x.split(",")
        month.append(s[0])
        monthly_amt.append(float(s[1]))
        monthly_change.append(float(s[1]) - previous_mth_amt)
        previous_mth_amt = float(s[1])
 
print("Election Results")
print("-----------------------------------")
print(f"Total Votes:  {num_of_votes}")
print("-----------------------------------")