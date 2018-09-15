#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 10:33:42 2018

@author: Khaled Nakhleh
"""

import numpy as np

class Radial:
    
    def __init__(self, r, n, l):
        self.r = np.linspace(0, r, 10000000)
        self.n = n
        self.l = l
        self.a = 5.29 * (10 ** (-11))  # Bohr's radius
        self.check_param()
        self.result = self.choose_func()
    
    def check_param(self):
        if self.n <= 0:
            print("\n\tEntered 'n' value is: " + str(self.n) + ". n must be 1 or larger." )
            exit
        elif self.l >= self.n:
            print("\n\tEntered 'l' value is: " + str(self.l) + ". entered 'n' value is " + str(self.n) +".")
            print("\tl must be smaller than 'n' value (l < n).")
            exit
    
    def choose_func(self):
        if self.n == 3:
            if self.l == 2:
                q = self.radius_32()
            elif self.l == 1:
                q = self.radius_31()
            else:
                q = self.radius_30()
                
        elif self.n == 2:
            if self.l == 1:
                q = self.radius_21()
            else:   
                q = self.radius_20()
                
        elif self.n == 1:
                q = self.radius_10()
                
        else:
           print("\n\tProgram does not include n values above 3.")
           exit
           
        return q
            
    def radius_10(self):
        first = (-1 * self.r)/self.a
        second = np.exp(first)
        third = second / (self.a ** (3/2))
        result = 2 * third 
         
        return result
        
    def radius_20(self):
        first = np.exp((-1*self.r)/2*self.a)
        second = (2*self.a)**(3/2)
        third = 2 - (self.r/self.a)
        result = third * (first/second)
        
        return result
    
    def radius_21(self):
        first = np.exp((-1*self.r)/2*self.a)
        second = np.sqrt(3)*((2*self.a)**(3/2))
        result = (self.r/self.a) * (first/second)
        
        return result
    
    def radius_30(self):
        first = 2 * np.exp((-1*self.r)/3*self.a)
        second = 81 * np.sqrt(3) * (self.a ** (3/2))
        third = 27 - ((18*self.r)/self.a) + ((2*(self.r**2))/(self.a**2))
        result = (first/second) * third
        
        return result
    
    def radius_31(self):
        first = 4 * self.r * np.exp((-1*self.r)/3*self.a)
        second = ((self.a ** (3/2)) * 81 * np.sqrt(6) *self.a)
        third = 6 - (self.r/self.a)
        result = (first/second) * third
        
        return result
    
    def radius_32(self):
        first = 4 * (self.r ** 2) * (np.exp((-1*self.r)/3*self.a))
        second = 81 * np.sqrt(30) * (self.a ** (3/2)) * (self.a ** 2)
        result = first/second
        
        return result

if __name__ == "__main__":
    print("\n\tThis file only contains internal functions. Please use main.py to run the program.\n")
    exit