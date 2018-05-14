import ROOT as root
from Property import *
import math


selections = [ "PreselectionLL"]


f_in = root.TFile.Open( "../test/out_FinalPlots_defaults.root" )

f_out = root.TFile.Open("significance.root" , "recreate")
for selection in selections:
	dir_in = f_in.GetDirectory( selection + "/General/amuMass")
	dir_in_Pt = f_in.GetDirectory( selection + "/General/amuPt")
	diLeptonMass = Property.FromDir( dir_in )
	diLeptonPt = Property.FromDir( dir_in_Pt )

	for i in range(1 , 4):
		diLeptonMass.SetSignificances( i )
		diLeptonPt.SetSignificances( i )
        diLeptonMass.SetExpectedLimits()
        diLeptonPt.SetExpectedLimits()
	#diLeptonMass.Write( f_out , False )
	diLeptonPt.Write( f_out , False )

f_out.Close()
f_in.Close()

	


