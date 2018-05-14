import ROOT as root
from Property import *
import math

ZMass = 91.
window_size = 10.0

f_in = root.TFile.Open( "../test/out_FinalPlots_defaults_withoutKF.root" )
dir_in = f_in.GetDirectory("PreselectionLL/General/amuMass")
amuMass = Property.FromDir( dir_in )
dataMbkg=amuMass.SubtractDataMC(["Top" , "DiBoson"])
DY = amuMass.Bkg["DY"]
bin_1 = DY.FindBin( ZMass - window_size )
bin_2 = DY.FindBin( ZMass + window_size )
Err_DY = root.Double()
DY_InZPeak = DY.IntegralAndError(bin_1 , bin_2 , Err_DY)
Err_Data = root.Double()
Data_InZPeak = dataMbkg.IntegralAndError( bin_1 , bin_2 , Err_Data )
print  bin_1 , bin_2 , Err_Data , Err_DY
kfactor = Data_InZPeak/DY_InZPeak
print "KFactor is %.2f +- %.2f " % (kfactor, kfactor*sqrt( (Err_Data.real/Data_InZPeak)*(Err_Data.real/Data_InZPeak) + (Err_DY.real/DY_InZPeak)* (Err_DY.real/DY_InZPeak) ) )

