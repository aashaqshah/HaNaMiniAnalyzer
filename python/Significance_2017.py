import ROOT as root
from Property import *
import math


selections = [ "PreselectionLL"]


f_in = root.TFile.Open( "../test/out_FinalPlots_defaults.root" )

f_out = root.TFile.Open("out.root" , "recreate")
for selection in selections:
	dir_in = f_in.GetDirectory( selection + "/General/amuMass")
	diLeptonMass = Property.FromDir( dir_in )

	for i in range(1 , 4):
		diLeptonMass.SetSignificances( i )
        diLeptonMass.SetExpectedLimits()
	diLeptonMass.Write( f_out , False )

f_out.Close()
f_in.Close()

	


