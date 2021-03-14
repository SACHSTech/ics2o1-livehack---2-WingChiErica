
"""
-------------------------------------------------------------------------------
Name:   problem1.py
Purpose:  Find the martian class
 
Author: Chan.E
 
Created:  23/02/2021
------------------------------------------------------------------------------
"""

# of attennas, eyes
attennas = int(input("How many attennas? "))
eyes = int(input("How many eyes? "))

# determine what type of martian
if attennas <= 6 and eyes >= 2:
    print ("It is a MaxMartian!")
if attennas >= 3 and eyes <= 4:
   print ("It is an AudreyMartian!")
if attennas <= 2 and eyes <= 3:
   print ("It is a BrooklynMartian!")
if attennas == 0 and eyes == 2:
   print ("It is a MattDamonMartian!")
if attennas > 6 and eyes > 4:
   print ("There is no lifeform detected.")