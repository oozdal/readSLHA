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
sys.path.append("/Users/oozdal/hepwork/pyslha-3.2.1")                                           # Please insert the path for pyslha
SLHAfilePath = "/Volumes/LaCie/SyncforGuillimin/scratch/NonunigauginomchiBLR/out_files/stem."   # Please insert the path for SLHA files

initial = 0
final = 217257

##########################################################################

newSLHA = ReadSLHAfiles()
for order in range(initial,final):
    FullSLHAfilePath = SLHAfilePath + str(order)
    if os.path.exists(FullSLHAfilePath) == True:
        print "SLHA file Reading: stem."+str(order)
        try:
            newSLHA.readSLHAblocks(FullSLHAfilePath)
            if newSLHA.Check_LSP() == True:                                      # Choose if the LSP is Neutralino or Snuetrino
                if newSLHA.Check_Bphysics() == True:                             # Check B-physics
                    if newSLHA.Check_HiggsBounds_Signals() == True:              # Check HiggsBounds and HiggsSignals
                        if newSLHA.Check_MassBounds() == True:                   # Check MassBounds
                            if newSLHA.LSPcontent == "NeutralinoLSP":            # Assign this solution as consistent Neutralino LSP
                                if newSLHA.Check_RelicDensityBound() == True:    # Assign this solution as Neutralino Dark Matter
                                    newSLHA.FindBenchmarks("newBenchmarks.dat", order)
                            if newSLHA.LSPcontent == "SneutrinoLSP":             # Assign this solution as consistent Sneutrino LSP
                                print "sneutrino LSP"
                                if newSLHA.Check_RelicDensityBound() == True:    # Assign this solution as Sneutrino Dark Matter
                                    print "sneutrino DM"
                                    
            else:
                continue
        except:
            print "This is an error message!"
            
    else:
        print "SLHA file stem."+str(order)+" does not exist!"
        continue
