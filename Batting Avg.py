# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 19:13:25 2016

@author: Lisa Rush
"""

hits=input("Hits: ")
at_bat=input('Times at bat: ')
avg=int(hits)/int(at_bat)

hit1 = int(input("Hit or not (1/0): "))
hit2 = int(input("Hit or not (1/0): "))
hit3 = int(input("Hit or not (1/0): "))
total_hits= int(hit1+hit2+hit3)
total_ab=3
ba=(total_hits)/(total_ab)
print("Your average is: ")
