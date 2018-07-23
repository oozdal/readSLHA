# Python script to read SLHA files using the class named classReadSLHA
# in case of problems send email to ozerozdal@gmail.com
# ----------------------------------------------------------------------
# Author: Ozer Ozdal 
# Created: 21.07.2018,  16:03


################### Required Python Packages ##############################
import sys
import os
from classReadSLHA import *
##########################################################################

################# User Inputs to Required File Paths #####################
sys.path.append("/Users/oozdal/hepwork/pyslha-3.2.1")  # Please insert the path for pyslha
SLHAfilePath = "/Volumes/LaCie/SyncforGuillimin/scratch/NonunigauginomchiBLR/out_files/stem."   # Please insert the path for SLHA files

initial = 0
final = 1000

##########################################################################

newSLHA = ReadSLHAfiles()
for order in range(initial,final):
    FullSLHAfilePath = SLHAfilePath + str(order)
    if os.path.exists(FullSLHAfilePath) == True:
        print "SLHA file Reading: stem."+str(order)
        newSLHA.readSLHAblocks(FullSLHAfilePath)
        newSLHA.Check_Bphysics()
    else:
        print "SLHA file stem."+str(order)+" does not exist!"
        continue
