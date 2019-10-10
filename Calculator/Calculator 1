#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 10:30:51 2019

@author: kylemcnicoll
"""

def cal_mean(data):
    return sum(data)/len(data)

def calc_median(data):
   data.sort()
   sample = list(data)
   while len(sample) > 2:
       sample.pop(-1)
       sample.pop(0)
   if len(sample)<= 2:
       return sum(sample)/len(sample)