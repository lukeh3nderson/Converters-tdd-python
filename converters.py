"""Library of unit converters"""

# Declare useful constants 

NPL = 4.4822 # newtons per pound-foot
IPM = 1550 # square inches per square meter

"""Gallon to liter converter""" 
def gal_to_liter(gal):
    return gal*3.79 


""" Converts PSI to KPa"""
def psi_2kpa(psi):
    return psi * NPL * IPM / 1000

