import pytest
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

def test_find_blacks():
    peaks = playground.core_black.find_blacks([[0,10,0],[0, 0, 0], [200,0,0]])
    assert peaks == [1]  
    
def test_find_two_blacks():
    peaks = playground.core_black.find_blacks([[0,10,0],[0, 0, 0], [200,0,0], [0,10,0],[0, 0, 0], [200,0,0]])
    assert peaks == [1, 4] 

def test_find_blacks_max_edge():
    peaks = playground.core_black.find_blacks([0, 0, 0], [200,0,0], [0,10,0],[0, 0, 0])
    assert peaks == [] 
    
def test_find_blacks_empty_list():
    peaks = playground.core_black.find_blacks([])
    print("yeah")
    assert peaks == [] 
    
#test_find_blacks_empty_list()
