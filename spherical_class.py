#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 10:34:20 2018

@author: Khaled Nakhleh
"""

import numpy as np

class Spherical:
    
    def __init__(self, theta, phi, l, ml):
        self.theta = theta
        self.phi = phi
        self.l = l
        self.ml = ml
        self.mlabs = abs(ml)
        self.check_param()
        self.result = self.choose_func()
        
    def check_param(self):
        if self.l > 3:
            print("\n\tCode only runs for l values of: 0, 1, 2, 3. You entered: "+str(self.l))
            exit
        elif abs(self.ml) > self.l:
            print("\n\tEntered 'ml' value is: " + str(self.ml) + ". entered 'l' value is " + str(self.l) +".")
            print("\tml must be smaller than 'l' value (ab(ml) <= l).")
            exit
    
    def choose_func(self):
        if self.l == 3:
            if self.mlabs == 3:
                q = Spherical.harmonics_33(self)
            elif self.mlabs == 2:
                q = Spherical.harmonics_32(self)
            elif self.mlabs == 1:
                q = Spherical.harmonics_31(self)
            elif self.mlabs == 0:
                q = Spherical.harmonics_30(self)
                
        elif self.l == 2:    
            if self.mlabs == 2:
                q = Spherical.harmonics_22(self)
            elif self.mlabs == 1:
                q = Spherical.harmonics_21(self)
            elif self.mlabs == 0:
                q = Spherical.harmonics_20(self)
                
        elif self.l == 1:
            if self.mlabs == 1:
                q = Spherical.harmonics_11(self)
            elif self.mlabs == 0:
                q = Spherical.harmonics_10(self)
                
        elif self.l == 0:
            q = Spherical.harmonics_00(self)
            
        else:
           print("\n\tEntered values are not defined in the code.")
           exit
        return q

    def harmonics_00(self):
        first = 2 * np.sqrt(np.pi)
        
        return 1/first

    def harmonics_10(self):
        first = np.sqrt(3/np.pi) * np.cos(self.theta)
        
        return 0.5 * first
    
    def harmonics_11(self):
        first = np.exp(1j*self.phi)
        second = np.sqrt(3/(2*np.pi)) * np.sin(self.theta)
        
        return 0.5 * first * second
    
    def harmonics_20(self):
        first = (3 * (np.cos(self.theta))**2) -  1
        second = np.sqrt(5/np.pi)
        
        return 0.25 * first * second
    
    def harmonics_21(self):
        first = np.sin(self.theta) * np.cos(self.theta) * np.exp(1j*self.phi)
        second = np.sqrt(15/(2*np.pi))
        
        return 0.5 * first * second
    
    def harmonics_22(self):
        first = (np.sin(self.theta) ** 2) * np.exp(2*1j*self.phi)
        second = np.sqrt(15/(2*np.pi))
        
        return 0.25 * first * second
    
    def harmonics_30(self):
        first = (5 * (np.cos(self.theta) ** 3)) - 3*np.cos(self.theta)
        second = np.sqrt(7/np.pi)
        
        return 0.25 * first * second
    
    def harmonics_31(self):
        first = (5 * (np.cos(self.theta) ** 2)) - 1
        second = np.sin(self.theta) * np.exp(1j*self.phi)
        third = np.sqrt(21/np.pi)
        
        return 0.125 * first * second * third
    
    def harmonics_32(self):
        first = (np.sin(self.theta)) ** 2
        second = np.cos(self.theta) * np.exp(2*1j*self.phi)
        third = np.sqrt(105/(2*np.pi))
        
        return 0.25 * first * second * third
    
    def harmonics_33(self):
        first = (np.sin(self.theta)) ** 3

        second = np.sqrt(35/np.pi) * np.exp(3*1j*self.phi)

        
        return 0.125 * first * second

if __name__ == "__main__":
    print("\n\tThis file only contains internal functions. Please use main.py to run the program.\n")
    exit