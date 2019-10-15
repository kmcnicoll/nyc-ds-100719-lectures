#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 17:57:04 2019

@author: kylemcnicoll
"""

import csv
roll_dict=[]
with open("data.csv") as f:
    reader= csv.DictReader(f)
   # roll_dict=[{k:v for k,v in row.items()} for row in reader]
    for row in reader:
        roll_dict.append(row)

roll_dict=[row for row in reader]
    #for row in reader: