#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:01:37 2017

@author: eliottguenat
"""
import scipy.io
from pylab import * 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from SolarFunc import SolarFncn
import numpy

PVaz = 0
PVal = 90*pi/180

PVazList    = linspace(0,2*pi,20)
PValList    = linspace(0,pi/2,20)

FailureDays   = numpy.zeros((20,20))
Yield         = numpy.zeros((20,20))
x             = numpy.linspace(0,360,20)
y             = numpy.linspace(0,90,20)

xv, yv = numpy.meshgrid(y,x)

for countAZ in range(len(PVazList)):
    for countAL in range(len(PValList)):
        out   = SolarFncn(PVazList[countAZ],PValList[countAL])
        FailureDays[countAZ,countAL] = out[1]
        Yield[countAZ,countAL]       = out[0]
        #print('top')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')        
ax.plot_surface(xv, yv, FailureDays,)
plt.show()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')        
ax.plot_surface(xv, yv, Yield,)
plt.show()

maxYield    = argmax(Yield)
argY        = mod(maxYield,20)
argX        = int(maxYield/20)