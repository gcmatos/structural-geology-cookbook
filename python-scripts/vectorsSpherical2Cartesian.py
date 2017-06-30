# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:55:19 2016

@author: Thiago
"""
# Algorithm based on Almendinger's book. Page. 32.
# Function SphToCart. Function to convert planes and Lines from spherical
# coordinate system to cartesian coordinate system.
# The Algorith is in MatLab, here let's try to rewrite it in Python.

# We are going to calculate the cn - coordinate north; ce - coordinate east and cd - coordinate down. All of it, from spherical ones: trd - plunge, plg - plunge and k - line or plane.
# Angles should be entered in radians
import math
print "Insert the spherical orientation of your structure."
trd = float(raw_input("Trend> "))
plg = float(raw_input("Plunge> "))
tpl = float(raw_input("what kind of structures do you have? Line or Plan?\n> "))
###
#while tpl != "line" and tpl != "plan":
#    print "This structure doesn't exist, or it was miss typed, please, insert plan or line!"
#    tpl = raw_input("What kind of structures do you have? Line or Plan?\n> ")
#"""
#tp = 9
#if tpl == "line":
#    tp = 0
#elif tpl == "plan":
#    tp = 1

sph = [trd, plg, tpl]
k = sph[2]
if k == 0:
    trend = sph[0]*math.pi/180
    plunge = sph[1]*math.pi/180
    print "%s/%s" % (trd, plg)
    print "%s %s" % (trend, plunge)

else:
    strike = sph[0]*math.pi/180
    dip = sph[1]*math.pi/180
    print "%s/%s" % (trd, plg)
    print "%s/%s" % (strike, dip)
#%%      
if k == 0:
    cd = math.sin(plunge)
    ce = math.cos(plunge) * math.sin(trend)
    cn = math.cos(plunge) * math.cos(trend)
elif k == 1:
    cd = math.cos(dip)
    ce = (-1)*math.sin(dip)*math.cos(strike)
    cn = math.sin(dip)*math.sin(strike)

cd = round(cd, 4)
ce = round(ce, 4)
cn = round(cn, 4) 
cart = [cn, ce, cd]
print cart
