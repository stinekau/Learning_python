#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 14:08:22 2022

@author: stinekaupang
"""

x = input ("legg inn verdi for A:")

y = input ("legg inn verdi for B:")
#konverterer x og y fra string til int
a = int(x)
b = int(y)

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")