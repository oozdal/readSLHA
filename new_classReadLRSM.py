import pyslha
import pandas as pd

class ReadLRSM():
    def __init__(self,SLHApath):
        self.SLHA = pyslha.read(SLHApath, ignoreblocks=['SPINFO'])

        
    def Read_Block(self, BlockName, id1=None, id2=None, id3=None):
        self.BlockName       = BlockName
        self.id1             = id1
        self.id2             = id2
        self.id3             = id3

        self.list_all_blocks = self.SLHA.blocks
        self.pyslha_Block    = self.SLHA.blocks[self.BlockName]
        
        if self.id1 != None and self.id2 == None and self.id3 == None:     
            self.VarValue1   = self.pyslha_Block[self.id1]
            return self.VarValue1

        elif self.id1 != None and self.id2 != None and self.id3 == None:
            self.VarValue2   = self.pyslha_Block[self.id1,self.id2] 
            return self.VarValue2

        else:
            self.VarValue3   = self.pyslha_Block[self.id1,self.id2,self.id3]
            return self.VarValue3
            

    def Read_MassBlock(self):
        
        self.W_R_mass        = self.SLHA.blocks["MASS"][34]


    def ReadxSection(self,xsectionPath):
        file = open(xsectionPath, "r")
        for line in file:
            if line[3:20] == "Integrated weight":
                self.xsectionforWr = float(line[35:50])
        
    def Read_Decays(self, PySLHAparticleID, DecayProduct = None):
        
        self.PySLHAparticle = self.SLHA.decays[PySLHAparticleID]

        self.DecayProduct = DecayProduct

        self.list_decaysmodes = self.PySLHAparticle.decays
        self.totalwidth       = self.PySLHAparticle.totalwidth
        self.ParticleMass     = self.PySLHAparticle.mass

        for i in range(len(self.list_decaysmodes)):
            self.decaymode = self.list_decaysmodes[i]
            if self.decaymode.ids == self.DecayProduct:
                return self.decaymode.br

