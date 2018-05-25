import ROOT as root
from Property import *
import math
import os


selections = [ "PreselectionLL", "PreselectionML", "PreselectionTL", "PreselectionMM", "PreselectionTM", "PreselectionTT"]
sub_dir = ["Mu1", "Mu2", "Jet1", "Jet2"]

f_in = root.TFile.Open( "../test/out_FinalPlots_defaults.root" )

f_out = root.TFile.Open("significance.root" , "recreate")
for selection in selections:
 
        print "Calculating significance for ", selection
 	dir_in_Pt = f_in.GetDirectory( selection + "/General/amuPt")
	dir_in = f_in.GetDirectory( selection + "/General/amuMass")

	dir_Mu1Pt = f_in.GetDirectory( selection + "/Mus/Mu1Pt")
	dir_Mu2Pt = f_in.GetDirectory( selection + "/Mus/Mu2Pt")

	dir_Jet1Pt = f_in.GetDirectory( selection + "/Jets/Jet1Pt")
	dir_Jet2Pt = f_in.GetDirectory( selection + "/Jets/Jet2Pt")

	#diLeptonMass = Property.FromDir( dir_in )
	#diLeptonPt = Property.FromDir( dir_in_Pt )

	Mu1_Pt = Property.FromDir( dir_Mu1Pt )
	Mu2_Pt = Property.FromDir( dir_Mu2Pt )

	Jet1_Pt = Property.FromDir( dir_Jet1Pt )
	Jet2_Pt = Property.FromDir( dir_Jet2Pt )
        
	for i in range(2 , 4):
		#diLeptonMass.SetSignificances( i )
		#diLeptonPt.SetSignificances( i )
		Mu1_Pt.SetSignificances( i )
		Mu2_Pt.SetSignificances( i )
		Jet1_Pt.SetSignificances( i )
		Jet2_Pt.SetSignificances( i )
        	#diLeptonMass.SetExpectedLimits()
        	#diLeptonPt.SetExpectedLimits()
	Mu1_Pt.SetExpectedLimits()
	#Mu2_Pt.SetExpectedLimits()
	#Jet1_Pt.SetExpectedLimits()
	#Jet2_Pt.SetExpectedLimits()

        new_dir  = f_out.mkdir( selection )
        #print "Created directory ", new_dir, "Successfully"
        new_dir.cd()
        #sub_di = new_dir.mkdir("Mu1")
	#diLeptonMass.Write( f_out , False )
	#diLeptonPt.Write( f_out , False )
        #Mu1_Pt.Write(new_dir, False)
        for sub_d in sub_dir:
             if sub_d =="Mu1":
                sub_di = new_dir.mkdir(sub_d)
                Mu1_Pt.Write(sub_di, False)
                del(Mu1_Pt)
             elif sub_d == "Mu2":
                sub_di = new_dir.mkdir(sub_d)
                Mu2_Pt.Write(sub_di, False)
                del(Mu2_Pt)
             elif sub_d == "Jet1":
                sub_di = new_dir.mkdir(sub_d)
                Jet1_Pt.Write(sub_di, False)
                del(Jet1_Pt)
             elif sub_d == "Jet2":
                sub_di = new_dir.mkdir(sub_d)
                Jet2_Pt.Write(sub_di, False)
                del(Jet2_Pt)
                  

            #if sub_d =="Mu1":
            #   sub_di = new_dir.mkdir( sub_d)
            #   Mu1_Pt.Write(sub_di, False)
            #   del(Mu1_Pt)

        #Mu1_Pt.Write(sub_di, False)
        #del(Mu1_Pt)
        #del(new_dir)
        #Mu2Pt.Write(new_dir, False)
        #del(Mu2Pt)
        #del(new_dir)
	#new_dir.Write( f_out , False )
f_out.Close()
f_in.Close()

	


