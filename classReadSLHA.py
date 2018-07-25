# Python class to read SLHA files using pyslha
# in case of problems send email to ozerozdal@gmail.com
# ----------------------------------------------------------------------
# Author: Ozer Ozdal
# Created: 21.07.2018,  18:10
# ----------------------------------------------------------------------

import pyslha

class ReadSLHAfiles():
    def __init__(self):
        pass
    def readSLHAblocks(self,SLHApath):
        self.SLHA = pyslha.read(SLHApath)

        self.m0              = self.SLHA.blocks["MINPAR"][1]
        self.m12             = self.SLHA.blocks["MINPAR"][2]
        self.SignumMu        = self.SLHA.blocks["MINPAR"][4]
        self.Azero           = self.SLHA.blocks["MINPAR"][5]
        self.TanBeta         = self.SLHA.blocks["MINPAR"][7]
        self.TanBetaR        = self.SLHA.blocks["MINPAR"][9]
        self.mARinput        = self.SLHA.blocks["MINPAR"][10]
        self.vR              = self.SLHA.blocks["MINPAR"][11]
        self.MuRinput        = self.SLHA.blocks["MINPAR"][12]
        self.mBino           = self.SLHA.blocks["MINPAR"][13]
        self.mBinop          = self.SLHA.blocks["MINPAR"][14]
        self.mGluino         = self.SLHA.blocks["MINPAR"][15]

        self.gBLGUT          = self.SLHA.blocks["GAUGEGUT"][1]
        self.gLGUT           = self.SLHA.blocks["GAUGEGUT"][2]
        self.gRGUT           = self.SLHA.blocks["GAUGEGUT"][4]
        self.g3GUT           = self.SLHA.blocks["GAUGEGUT"][3]

        self.gBLSUSY         = self.SLHA.blocks["GAUGE"][1]
        self.gLSUSY          = self.SLHA.blocks["GAUGE"][2]
        self.gRSUSY          = self.SLHA.blocks["GAUGE"][4]
        self.g3SUSY          = self.SLHA.blocks["GAUGE"][3]
        self.gBLgRSUSY       = self.SLHA.blocks["GAUGE"][10]
        self.gRgBLSUSY       = self.SLHA.blocks["GAUGE"][11]

        self.MuRSUSY         = self.SLHA.blocks["HMIX"][9]
        self.MuSUSY          = self.SLHA.blocks["HMIX"][1]
        self.BmuRSUSY        = self.SLHA.blocks["HMIX"][109]
        self.BmuSUSY         = self.SLHA.blocks["HMIX"][101]
        self.vChiRbSUSY      = self.SLHA.blocks["HMIX"][106]
        self.vChiRSUSY       = self.SLHA.blocks["HMIX"][105]
        self.vdSUSY          = self.SLHA.blocks["HMIX"][102]
        self.vuSUSY          = self.SLHA.blocks["HMIX"][103]
        self.vSUSY           = self.SLHA.blocks["HMIX"][3]

        self.mHd2SUSY        = self.SLHA.blocks["MSOFT"][21]
        self.mHu2SUSY        = self.SLHA.blocks["MSOFT"][22]
        self.mCR2SUSY        = self.SLHA.blocks["MSOFT"][31]
        self.mCRb2SUSY       = self.SLHA.blocks["MSOFT"][32]
        self.M1SUSY          = self.SLHA.blocks["MSOFT"][1]
        self.M2SUSY          = self.SLHA.blocks["MSOFT"][2]
        self.M3SUSY          = self.SLHA.blocks["MSOFT"][3]
        self.M4SUSY          = self.SLHA.blocks["MSOFT"][4]

        self.Ys11SUSY        = self.SLHA.blocks["YS"][1,1]
        self.Ys22SUSY        = self.SLHA.blocks["YS"][2,2]
        self.Ys33SUSY        = self.SLHA.blocks["YS"][3,3]
       
        self.Yv11SUSY        = self.SLHA.blocks["YV"][1,1]
        self.Yv12SUSY        = self.SLHA.blocks["YV"][1,2]
        self.Yv13SUSY        = self.SLHA.blocks["YV"][1,3]
        self.Yv21SUSY        = self.SLHA.blocks["YV"][2,1]        
        self.Yv22SUSY        = self.SLHA.blocks["YV"][2,2]
        self.Yv23SUSY        = self.SLHA.blocks["YV"][2,3]
        self.Yv31SUSY        = self.SLHA.blocks["YV"][3,1] 
        self.Yv32SUSY        = self.SLHA.blocks["YV"][3,2]        
        self.Yv33SUSY        = self.SLHA.blocks["YV"][3,3]

        self.MuRGUT          = self.SLHA.blocks["HMIXGUT"][9]
        self.MuGUT           = self.SLHA.blocks["HMIXGUT"][1]
        self.BMuRGUT         = self.SLHA.blocks["HMIXGUT"][109]
        self.BmuGUT          = self.SLHA.blocks["HMIXGUT"][101]

        self.mHd2GUT         = self.SLHA.blocks["MSOFTGUT"][21]
        self.mHu2GUT         = self.SLHA.blocks["MSOFTGUT"][22]
        self.mCR2GUT         = self.SLHA.blocks["MSOFTGUT"][31]
        self.mCRb2GUT        = self.SLHA.blocks["MSOFTGUT"][32]
        self.M1GUT           = self.SLHA.blocks["MSOFTGUT"][1]
        self.M2GUT           = self.SLHA.blocks["MSOFTGUT"][2]
        self.M3GUT           = self.SLHA.blocks["MSOFTGUT"][3]
        self.M4GUT           = self.SLHA.blocks["MSOFTGUT"][4]

        self.Sd_1            = self.SLHA.blocks["MASS"][1000001]
        self.Sd_2            = self.SLHA.blocks["MASS"][1000003]
        self.Sd_3            = self.SLHA.blocks["MASS"][1000005] 
        self.Sd_4            = self.SLHA.blocks["MASS"][2000001]
        self.Sd_5            = self.SLHA.blocks["MASS"][2000003]
        self.Sd_6            = self.SLHA.blocks["MASS"][2000005]

        self.Su_1            = self.SLHA.blocks["MASS"][1000002]
        self.Su_2            = self.SLHA.blocks["MASS"][1000004]
        self.Su_3            = self.SLHA.blocks["MASS"][1000006]
        self.Su_4            = self.SLHA.blocks["MASS"][2000002]
        self.Su_5            = self.SLHA.blocks["MASS"][2000004]
        self.Su_6            = self.SLHA.blocks["MASS"][2000006]        

        self.Se_1            = self.SLHA.blocks["MASS"][1000011]
        self.Se_2            = self.SLHA.blocks["MASS"][1000013]
        self.Se_3            = self.SLHA.blocks["MASS"][1000015]
        self.Se_4            = self.SLHA.blocks["MASS"][2000011]
        self.Se_5            = self.SLHA.blocks["MASS"][2000013]
        self.Se_6            = self.SLHA.blocks["MASS"][2000015]

        self.Sv_1            = self.SLHA.blocks["MASS"][1000012]
        self.Sv_2            = self.SLHA.blocks["MASS"][1000014]
        self.Sv_3            = self.SLHA.blocks["MASS"][1000016]
        self.Sv_4            = self.SLHA.blocks["MASS"][2000012]
        self.Sv_5            = self.SLHA.blocks["MASS"][2000014]
        self.Sv_6            = self.SLHA.blocks["MASS"][2000016]
        self.Sv_7            = self.SLHA.blocks["MASS"][3000012]
        self.Sv_8            = self.SLHA.blocks["MASS"][3000014]
        self.Sv_9            = self.SLHA.blocks["MASS"][3000016]

        self.hh_1            = self.SLHA.blocks["MASS"][25]
        self.hh_2            = self.SLHA.blocks["MASS"][35]
        self.hh_3            = self.SLHA.blocks["MASS"][225]
        self.hh_4            = self.SLHA.blocks["MASS"][232]

        self.Ah_3            = self.SLHA.blocks["MASS"][36]
        self.Ah_4            = self.SLHA.blocks["MASS"][236]
        self.Hpm_2           = self.SLHA.blocks["MASS"][37]

        self.VZ              = self.SLHA.blocks["MASS"][23]
        self.VMm             = self.SLHA.blocks["MASS"][24]
        self.VZR             = self.SLHA.blocks["MASS"][99]
        self.Glu             = self.SLHA.blocks["MASS"][1000021]

        self.Chi_1           = self.SLHA.blocks["MASS"][1000022]
        self.Chi_2           = self.SLHA.blocks["MASS"][1000023]
        self.Chi_3           = self.SLHA.blocks["MASS"][1000025]
        self.Chi_4           = self.SLHA.blocks["MASS"][1000035]
        self.Chi_5           = self.SLHA.blocks["MASS"][9000001]
        self.Chi_6           = self.SLHA.blocks["MASS"][9000002]
        self.Chi_7           = self.SLHA.blocks["MASS"][9000003]
        self.Cha_1           = self.SLHA.blocks["MASS"][1000024]
        self.Cha_2           = self.SLHA.blocks["MASS"][1000037]

        self.LSP             = self.SLHA.blocks["LSP"][1]
        self.NLSP            = self.SLHA.blocks["LSP"][2]

        self.SNUMIX11        = self.SLHA.blocks["SNUMIX"][1,1]
        self.SNUMIX12        = self.SLHA.blocks["SNUMIX"][1,2]
        self.SNUMIX13        = self.SLHA.blocks["SNUMIX"][1,3]
        self.SNUMIX14        = self.SLHA.blocks["SNUMIX"][1,4]
        self.SNUMIX15        = self.SLHA.blocks["SNUMIX"][1,5]
        self.SNUMIX16        = self.SLHA.blocks["SNUMIX"][1,6]
        self.SNUMIX17        = self.SLHA.blocks["SNUMIX"][1,7]
        self.SNUMIX18        = self.SLHA.blocks["SNUMIX"][1,8] 
        self.SNUMIX19        = self.SLHA.blocks["SNUMIX"][1,9]

        self.NMIX11          = self.SLHA.blocks["NMIX"][1,1]
        self.NMIX12          = self.SLHA.blocks["NMIX"][1,2]
        self.NMIX13          = self.SLHA.blocks["NMIX"][1,3]
        self.NMIX14          = self.SLHA.blocks["NMIX"][1,4] 
        self.NMIX15          = self.SLHA.blocks["NMIX"][1,5] 
        self.NMIX16          = self.SLHA.blocks["NMIX"][1,6] 
        self.NMIX17          = self.SLHA.blocks["NMIX"][1,7] 

        if self.SLHA.blocks["HIGGSLHC14"].keys() == [(1,25)]:  self.hh_1LHC14glufus = self.SLHA.blocks["HIGGSLHC14"][1,25]
        if self.SLHA.blocks["HIGGSLHC14"].keys() == [(1,35)]:  self.hh_2LHC14glufus = self.SLHA.blocks["HIGGSLHC14"][1,35]

        if self.SLHA.blocks["HIGGSFCC100"].keys() == [(1,25)]: self.hh_1FCC100glufus= self.SLHA.blocks["HIGGSFCC100"][1,25]
        if self.SLHA.blocks["HIGGSFCC100"].keys() == [(1,35)]: self.hh_2FCC100glufus= self.SLHA.blocks["HIGGSFCC100"][1,35]   

        self.muon_g_2         = self.SLHA.blocks["SPHENOLOWENERGY"][21]

        self.Bxsgamma         = self.SLHA.blocks["FLAVORKITQFV"][200]
        self.RBtaunu          = self.SLHA.blocks["FLAVORKITQFV"][503]
        self.Bsmumu           = self.SLHA.blocks["FLAVORKITQFV"][4006]

#########################################################################
# If Block HiggsBoundsResults is added by
# HiggsBounds http://projects.hepforge.org/higgsbounds

        if 'HIGGSBOUNDSRESULTS' in self.SLHA.blocks.keys():
            self.HBresult         = self.SLHA.blocks["HIGGSBOUNDSRESULTS"][1,2]   # HBresult

#########################################################################
# If BLOCK HiggsSignalsResults is added by HiggsSignals

        if 'HIGGSSIGNALSRESULTS' in self.SLHA.blocks.keys():
            self.totchi2          = self.SLHA.blocks["HIGGSSIGNALSRESULTS"][12]   # chi^2 (total)

#########################################################################
# If BLOCK RELIC is added by MicrOmegas

        if 'RELIC' in self.SLHA.blocks.keys():        
            self.RelicDensity     = self.SLHA.blocks["RELIC"][700]   # relic density
            self.ProtonSI         = self.SLHA.blocks["RELIC"][201]   # Proton SI [pb]
            self.NeutronSI        = self.SLHA.blocks["RELIC"][203]   # Neutron SI [pb]
            self.IceCubeExcCL     = self.SLHA.blocks["RELIC"][305]   # IceCube22 exclusion confidence level
            self.sigmaV           = self.SLHA.blocks["RELIC"][306]   # sigmaV [cm^3/s] Annihilation cross section
            self.PhotonFlux       = self.SLHA.blocks["RELIC"][307]   # Photon flux [cm^2 s GeV]^{-1}
            self.PositronFlux     = self.SLHA.blocks["RELIC"][308]   # Positron flux [cm^2 sr s GeV]^{-1}
            self.AntiProtonFlux   = self.SLHA.blocks["RELIC"][309]   # Antiproton flux [cm^2 sr s GeV]^{-1}
            self.NeutrinoFlux     = self.SLHA.blocks["RELIC"][310]   # Neutrino Flux [1/Year/km^2]
            self.AntiNeutrinoFlux = self.SLHA.blocks["RELIC"][311]   # Anti-Neutrino Flux [1/Year/km^2]
    

#########################################################################
######################## Reading Decay Blocks ###########################

    def Sv_1_Decays(self):
        pass


    def Chi_2_Decays(self):
        pass

    def Cha_1_Decays(self):
        pass


    def VZR_Decays(self):
        pass


#########################################################################
######################### Let's check the LSP ###########################

    def Check_LSP(self):
        self.NeutralinoLSPbound = False
        self.SneutrinoLSPbound  = False
        self.LSPbound           = False

        if self.LSP == 1000022                : self.LSPcontent = "NeutralinoLSP"
        if self.LSP == 1000012                : self.LSPcontent = "SneutrinoLSP"

        if self.LSPcontent == "NeutralinoLSP" : self.NeutralinoLSPbound = True
        if self.LSPcontent == "SneutrinoLSP"  : self.SneutrinoLSPbound  = True

        self.LSPbound = self.NeutralinoLSPbound or self.SneutrinoLSPbound

        return self.LSPbound

#########################################################################
################ Ready to Check Experimental Bounds #####################

################ Let's check SUSY mass bounds ###########################
    def Check_MassBounds(self):
        self.HiggsMassBound = False
        self.GluinoBound    = False
        self.ZprimeBound    = False
        self.Cha_1_Bound    = False
        self.Se_1_Bound     = False


        if (self.hh_1 > 122. and self.hh_1 < 128.) or (self.hh_2 > 122. and self.hh_2 < 128.) : self.HiggsMassBound = True
        if self.Glu   > 1800.                                                                 : self.GluinoBound    = True
        if self.Cha_1 > 103.5 and self.Cha_1 < 275.                                           : self.Cha_1_Bound    = True
        if self.Se_1  > 105.                                                                  : self.Se_1_Bound     = True
        if self.VZR   > 3500.                                                                 : self.ZprimeBound    = True


        if 99 not in self.SLHA.blocks["MASS"].keys():   # For MSSM kind of SUSY models which does not have Z' in their particle content
            self.MassBounds = self.HiggsMassBound and self.GluinoBound and self.Cha_1_Bound and self.Se_1_Bound
        if 99 in self.SLHA.blocks["MASS"].keys():       # For Extended SUSY Models which have Z' in their particle content
            self.MassBounds = self.HiggsMassBound and self.GluinoBound and self.Cha_1_Bound and self.Se_1_Bound and self.ZprimeBound
        
        return self.MassBounds

########################################################################
######## Let's check HiggsBounds and HiggsSignals Results ###############
        
    def Check_HiggsBounds_Signals(self):
        self.HiggsBounds   = False
        self.HiggsSignals  = False

        if self.HBresult == 1                                     : self.HiggsBounds  = True                               
        if self.totchi2  < 3                                      : self.HiggsSignals = True

        self.Combined_HiggsBounds_Signals = self.HiggsBounds and self.HiggsSignals

        return self.Combined_HiggsBounds_Signals

########################################################################
############### Let's check B-physics constraints ######################

    def Check_Bphysics(self):
        self.BxsgammaBound = False
        self.RBtaunuBound  = False
        self.BsmumuBound   = False
        self.BphysicsBounds = False

        if self.Bxsgamma > 2.99e-4 and self.Bxsgamma < 3.87e-4    : self.BxsgammaBound = True
        if self.RBtaunu > 0.15 and self.RBtaunu < 2.41            : self.RBtaunuBound = True
        if self.Bsmumu > 0.8e-9 and self.Bsmumu < 6.2e-9          : self.BsmumuBound = True

        self.BphysicsBounds = self.BxsgammaBound and self.RBtaunuBound and self.BsmumuBound
    
        return self.BphysicsBounds

########################################################################
################## Let's Check Relic Density ###########################

    def Check_RelicDensityBound(self):
        self.RelicDenBound = False
        
        if self.RelicDensity >= 0.0913 and self.RelicDensity <= 0.1363 : self.RelicDenBound = True
        
        return self.RelicDenBound

########################################################################
############# Let's Check Other Dark Matter Experiments ################

    def Check_DMexperiments(self):
        pass
# Check Spin Independent Cross Section for Proton and Neutron
# Check Annihilation Cross Section




########################################################################

    def FindBenchmarks(self, pathtodatafile, SLHAnumber):
        self.file = open(pathtodatafile, 'a+')
        self.file.write("stem."+str(SLHAnumber)+"\n")
        self.file.close()
        
