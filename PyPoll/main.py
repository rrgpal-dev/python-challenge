#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:52:53 2020

@author: N457149 - Raj Ramachandran
"""
i = 0
num_of_voters = 0
khan_cnt = 0
correy_cnt = 0
li_cnt = 0
tooley_cnt = 0

with open ("election_data.csv") as f:
  for i, x in enumerate(f):
     if i >=1 :
        num_of_voters= i
        s = x.split(",")
        if s[1] == "Khan" :
            khan_cnt = khan_cnt + 1
        elif s[1]=="Correy":
            correy_cnt = correy_cnt+ 1
        elif s[1] == "Li":
            li_cnt = li_cnt + 1
        else:
            tooley_cnt= tooley_cnt+1
                
            
            
            
"""    month.append(s[0])
        monthly_amt.append(float(s[1]))
        monthly_change.append(float(s[1]) - previous_mth_amt)
        previous_mth_amt = float(s[1])
""" 
print("Election Results")
print("-----------------------------------")
print(f"Total Votes:  {num_of_voters}")
print("-----------------------------------")
