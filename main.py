#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 15:40:58 2017

@author: eliottguenat
"""
# Import librairies and packages
import scipy.io
from pylab import * 
import matplotlib.pyplot as plt

# Import .MAT data from Matlab
mat = scipy.io.loadmat('DataSolarPython.mat', squeeze_me=True, struct_as_record=False)
Al= mat['Al']
Az= mat['Az']
Irr=mat['Irradiation']

# Simulation parameters
PVaz                = 0 # rad
PVal                = 70*pi/180 #rad
PVeff               = 0.15 #-
StorageCapa         = 100 #Wh
StorageLoad0        = 100 #Wh
PVarea              = 0.04 #m^2
DeviceConsumption   = 0.5 #W 

# Nested function definition of the cos factor
def CompCosFactor(phi1,delta1,phi2,delta2): return cos(phi1)*cos(delta1)*cos(phi2)*cos(delta2)+sin(phi1)*cos(delta1)*sin(phi2)*cos(delta2)+sin(delta1)*sin(delta2)

## Computation of the hourly PV production over the year
CosFactor       = CompCosFactor(PVaz,PVal,Az,Al)
PVproduction     = Irr*PVeff*PVarea*CosFactor
PVproduction[PVproduction < 0] = 0
# Plot the evolution of the PV production
plt.plot(linspace(0,1,len(CosFactor)),PVproduction)
plt.show()

## Computation of the storage SoC
#Initialization of the SoC array 
StorageLoad     = zeros(len(PVproduction))
StorageLoad[0]  = StorageLoad0

for countH in range(1,len(PVproduction)):
    StorageLoad[countH]=min(max(StorageLoad[countH-1] + PVproduction[countH] - DeviceConsumption,0),StorageCapa)

plt.plot(linspace(0,1,len(StorageLoad)),StorageLoad)
plt.show()

