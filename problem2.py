
"""
-------------------------------------------------------------------------------
Name:   problem2.py
Purpose:  Find if it's a triangle
 
Author: Chan.E
 
Created:  23/02/2021
------------------------------------------------------------------------------
"""

# get side lengths
side_1 = int(input("Enter side length 1: "))
side_2 = int(input("Enter side length 2: "))
side_3 = int(input("Enter side length 3: "))

# determine if it's a triangle
if (side_1 + side_2 == side_3):
   print ("The figure is a triangle.")

else:
   print ("The figure is NOT a triangle")