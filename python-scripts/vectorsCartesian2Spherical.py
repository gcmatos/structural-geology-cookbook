# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 11:17:03 2016

@author: Thiago
"""

# Algorithm based on Almendinger's book. Page. 32.
#Function SphToCart. Function to convert planes and Lines from spherical coordinate system to cartesian coordinate system.
# The Algorith is in MatLab, here let's try to rewrite it in Python.

# We are going to calculate the cn - coordinate north; ce - coordinate east and cd - coordinate down. All of it, from spherical ones: trd - plunge, plg - plunge and k - line or plane.
# Angles should be entered in radians
# for that let's converts cartesian to spherical coordinates, which are more suitable for structural geologists.

import math

lista = [0.033916, 0.870032, 0.493560]
#vector x, vector y e vector z

cd = float(lista[2])
cn = float(lista[0])
ce = float(lista[1])


plg = math.asin(cd)

#plg_plan = math.cos(cd)

plg_graus = (plg)*(180/(math.pi))

#plg_graus_plan = ((math.pi*plg_plan)/4)*(180/(math.pi*plg_plan))

if cn == 0:
    if ce < 0:
        trd = 3/2*math.pi
    else:
        trd = math.pi/2
else:
    trd = math.atan(ce/cn)

if cn < 0:
    trd = trd + math.pi
 
trd_graus = (trd)*(180/math.pi)


print ("%s %s %s") % (cn, ce, cd)
print math.pi
print round(plg, 4)
print round(plg_graus, 1)
#print plg_graus_plan

print round (trd_graus, 1)

# this result is bringing us the polo of the plan

# let's do here polo to plan
