#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 08:51:05 2017

@author: eliottguenat
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 15:40:58 2017

@author: eliottguenat
"""
from pylab import * 

def SolarFncn(PVaz,PVal):
    # Import librairies and packages
    import scipy.io
    import matplotlib.pyplot as plt
    
    # Import .MAT data from Matlab
    mat = scipy.io.loadmat('DataSolarPython.mat', squeeze_me=True, struct_as_record=False)
    Al= mat['Al']
    Az= mat['Az']
    Irr=mat['Irradiation']
    
    # Simulation parameters
    PVeff               = 0.15 #-
    StorageCapa         = 50 #Wh
    StorageLoad0        = 50 #Wh
    PVarea              = 0.03 #m^2
    DeviceConsumption   = 1 #W 
    
    # Nested function definition of the cos factor
    def CompCosFactor(phi1,delta1,phi2,delta2): return cos(phi1)*cos(delta1)*cos(phi2)*cos(delta2)+sin(phi1)*cos(delta1)*sin(phi2)*cos(delta2)+sin(delta1)*sin(delta2)
    
    ## Computation of the hourly PV production over the year
    CosFactor       = CompCosFactor(PVaz,PVal,Az,Al)
    PVproduction     = Irr*PVeff*PVarea*CosFactor
    PVproduction[PVproduction < 0] = 0
    
    ## Computation of the storage SoC
    #Initialization of the SoC array 
    StorageLoad     = zeros(len(PVproduction))
    StorageLoad[0]  = StorageLoad0
    
    for countH in range(1,len(PVproduction)):
        StorageLoad[countH]=min(max(StorageLoad[countH-1] + PVproduction[countH] - DeviceConsumption,0),StorageCapa)
    
    PVyield     = sum(PVproduction)
    StorageFail = sum(StorageLoad==0)
    
    return (PVyield,StorageFail)


