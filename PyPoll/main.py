#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:52:53 2020

@author: N457149 - Raj Ramachandran
"""
import statistics
from statistics import mode 


def percal(val1,val2):
    return "{:10.3f}".format(val2*100/val1)

def most_common(List): 
    return(mode(List)) 

def write_file_line(s,f):
    f.write(s)
    f.write("\n")

i = 0
num_of_voters = 0
khan_cnt = 0
correy_cnt = 0
li_cnt = 0
tooley_cnt = 0
Total_count = 0
li_can = [""]

with open ("election_data.csv") as f:
  for i, x in enumerate(f):
     if i >=1 :
        num_of_voters= i
        s = x.split(",")
        li_can.append(s[2])
        can_name = s[2].strip().upper()
        if can_name == "KHAN" :
            khan_cnt = khan_cnt + 1
        elif can_name=="CORREY":
            correy_cnt = correy_cnt+ 1
        elif can_name == "LI":
            li_cnt = li_cnt + 1
        else:
            tooley_cnt= tooley_cnt+1

        
            
Total_count = khan_cnt+correy_cnt+li_cnt+tooley_cnt   
perval =   percal(Total_count,khan_cnt)


print("Election Results")
print("-----------------------------------")
print(f"Total Votes:  {num_of_voters}")
print("-----------------------------------")
print(f"Khan: {percal(Total_count,khan_cnt)} % , {khan_cnt}")
print(f"Correy: {percal(Total_count,correy_cnt)} % , {correy_cnt}")
print(f"Li: {percal(Total_count,li_cnt)} % , {li_cnt}")
print(f"O'Tooley': {percal(Total_count,tooley_cnt)} % , {tooley_cnt}")
print("-----------------------------------")
print(f"Winner is: {most_common(li_can)}")
print("-----------------------------------")

f = open("log.txt", "w")
write_file_line("Election Results",f)
write_file_line("-----------------------------------",f)
write_file_line(f"Total Votes:  {num_of_voters}",f)
write_file_line("-----------------------------------",f)
write_file_line(f"Khan: {percal(Total_count,khan_cnt)} % , {khan_cnt}",f)
write_file_line(f"Correy: {percal(Total_count,correy_cnt)} % , {correy_cnt}",f)
write_file_line(f"Li: {percal(Total_count,li_cnt)} % , {li_cnt}",f)
write_file_line(f"O'Tooley': {percal(Total_count,tooley_cnt)} % , {tooley_cnt}",f)
write_file_line("-----------------------------------",f)
write_file_line(f"Winner is: {most_common(li_can)}",f)
write_file_line("-----------------------------------",f)
f.close()