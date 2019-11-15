# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 11:15:52 2019

@author: user
"""
import sys, os
# This block is not neccessary if you instaled your package
# using e.g. pip install -e
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), # location of this file
            os.pardir, # and one level up, in linux ../
        )
    )
)
# EOBlock

import playground


def find_blacks(list_of_intensities):
    """Find blacks
    Find local minima of the most black RGB values 
    Intensities are defined as local minima if the 
    intensities of the elements in the list before and after 
    are higher than the peak we want to determine.
    Args:
        list_of_intensities (list of floats or ints): a list of
            numeric values
    Returns:
        list of floats: list of the identified local maxima
    Note:
        Using the find_peaks function to determin the local maxima.
        Values are inverted to "2*255-sum of tuple" to convert 
        to maxima.
    """
    max_value = 255*3
    list_of_tuple_sum = []
    for element in list_of_intensities:
        list_of_tuple_sum.append(max_value-sum(element))
     
    list_of_maxima=playground.core.find_peaks(list_of_tuple_sum)    
    return list_of_maxima

"""
ergebnis=find_blacks([[0,10,0],[0, 0, 0], [200,0,0]])
print(ergebnis)"""