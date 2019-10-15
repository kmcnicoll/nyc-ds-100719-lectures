#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:07:05 2019

@author: kylemcnicoll
"""

class Calculator:
    
    def __init__(self, data):
        self.data = data
        self.__calc_all__(self.data)
    
        
    def __calc_median__(self, data):
        data=sorted(data)
        sample = list(data)
        while len(sample) > 2:
            sample.pop(-1)
            sample.pop(0)
        if len(sample)<= 2:
            return sum(sample)/len(sample)
        
        
    def __cal_mean__(self, data):
        return sum(data)/len(data)
    
    def __calc_variance__(self, data):
        storage=[]
        for number in data:
           storage.append((number - self.mean)**2)
        return sum(storage)/(len(data)-1)
       
    def add_data(self, new_data):
        self.data= self.data + new_data
        self.__calc_all__(self.data)
        
    def __calc_all__(self, data):
        self.length= len(list(data))
        self.median=self.__calc_median__(data)
        self.mean=self.__cal_mean__(data)
        self.variance=self.__calc_variance__(data)
        self.stand_dev=(self.variance)**.5
    
    
    def remove_data(self,del_data):
        for number in del_data:
            if number in self.data:
                while number in self.data:
                    self.data.remove(number)
        self.__calc_all__(self.data)
            

       

    