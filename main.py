#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 12:56:58 2018

@author: Khaled Nakhleh
"""

from timeit import default_timer as timer
from radial_class import Radial
from spherical_class import Spherical
import matplotlib.pyplot as plt

def sch(rad, sph):
    
    return (rad.result) * (sph.result)

def rdp(rad):
    """ Radial probability density rdp"""
    radius = rad.r ** 2
    

    return radius * ((abs(rad.result)) ** 2)


def main():
    
    n = int(input("\n\tEnter 'n' value: "))
    l = int(input("\n\tEnter 'l' value: "))
    ml = int(input("\n\tEnter 'ml' value: "))
    r = float(input("\n\tEnter 'r' value: "))
    theta = float(input("\n\tEnter 'theta' value: "))
    phi = float(input("\n\tEnter 'phi' value: "))
    
    start = timer()
    
    rad = Radial(r, n, l)
    sph = Spherical(theta, phi, l, ml)
    sch_sol = sch(rad, sph)
    prob = rdp(rad)
    
    print("\n  --------------------")
    print("  first 3 values in range: \n", rad.r[0:3])
    print("  first 3 values in the Radial wave function [R] solution: \n", rad.result[0:3])
    print("  Spherical  harmonics function [Y] solution: \n", sph.result)
    print("  firt 3 values of Schrodinger's wave function solution: \n", sch_sol[0:3])
    print("  --------------------")
    
    plt.figure(1)
    
    plt.subplot(121)
    plt.plot(rad.r, rad.result)
    plt.xlim(0, 6)
    
    plt.subplot(122)
    plt.plot(rad.r, prob)
    
    end = timer() - start
    plt.show()
    

    print("\n\tTotal operation time: ", end, " seconds.\n")
    
if __name__ == "__main__":
    main()