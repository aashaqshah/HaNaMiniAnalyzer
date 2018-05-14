import ROOT as root
from Property import *
import math
import os, fnmatch, re

from ROOT import  TLatex

selections = [ "PreselectionLL" , "PreselectionMM", "PreselectionTM", "PreselectionTT" ]
#selections = [ "PreselectionLL"]
data_histo = ["Data"]
sample_names = ["ZZ", "WZ", "WW", "W4JetsToLNu", "W3JetsToLNu", "TTTo2L2Nu", "TW", "TbarW", "TChannelTbar", "TChannelT", "DYJetsLowMass", "DYJetsHighMass"]
sample_names_joint = ["DiBoson", "Top", "DY"]

path = "../test/Output_KFRootFiles/"
list_dirs = os.listdir(path)
for dirname in list_dirs:
  algorithm = dirname.split("_")[3]
  print "\v\vCurrent algorithm is "+ algorithm
  f_in = root.TFile.Open( path + dirname+"/"+ dirname+".root" )
  for selection in selections:
    if f_in.GetDirectory(selection):      
        input_dir_data = f_in.GetDirectory(selection + "/General/amuMass/cats/")
        input_dir_McJoint = f_in.GetDirectory(selection + "/General/amuMass/cats/")
        #input_dir_data = f_in.GetDirectory(selection + "/General/amuMass/cats/")
	input_dir = f_in.GetDirectory( selection + "/General/amuMass/samples")
        print "Yield for " + selection
        print "\vSample\t \t  Yield   Error"       
        Yield_Sum = 0.0 
        Err_Yield_Sum = 0.0 
        DiBoson = 0.0
        DY = 0.0
        Top = 0.0 
        #for data
        for data in data_histo:
            Error_Yield = root.Double()
            hist = input_dir_data.Get(selection+"_amuMass_"+data) 
            first_bin = hist.FindBin(0)
            last_bin  = hist.GetXaxis().GetNbins()
            Yield  = hist.IntegralAndError(first_bin , last_bin , Error_Yield )
            print   data.ljust(15) + " %.2f +- %.2f" % (Yield, Error_Yield )
            #print    " %.2f" % (Yield) 
            #print   "%.2f" % (Error_Yield )
        #print "\v" 
        for sample_joint in sample_names_joint:
            Error_Yield = root.Double()
            hist = input_dir_McJoint.Get(selection + "_amuMass_"+ sample_joint)
            first_bin = hist.FindBin(0)
            last_bin  = hist.GetXaxis().GetNbins()
            Yield  = hist.IntegralAndError(first_bin , last_bin , Error_Yield )
            Yield_Sum = Yield_Sum + Yield
            Err_Yield_Sum = sqrt((Err_Yield_Sum*Err_Yield_Sum)+(Error_Yield*Error_Yield))
            print   sample_joint.ljust(15) + " %.2f +- %.2f" % (Yield, Error_Yield )
            #print    "%.2f" % (Yield )
            #print    "%.2f" % (Error_Yield )
            if sample_joint == "DiBoson":
               DiBoson = Yield
               DiBoson_Error_Yield = Error_Yield
            elif sample_joint == "Top":
               Top = Yield 
               Top_Error_Yield = Error_Yield
            else:
               DY = Yield
               DY_Error_Yield = Error_Yield

	print   "Yield Sum\t %.2f +- %.2f" % (Yield_Sum, Err_Yield_Sum)
	#print   "%.2f" % (Yield_Sum)
	#print   "%.2f" % (Err_Yield_Sum)

        print "DiBoson/Y\t %.2f +- %.2f" %(DiBoson/Yield_Sum, Yield_Sum/DiBoson*sqrt( (DiBoson_Error_Yield/DiBoson)*(DiBoson_Error_Yield/DiBoson) + (Err_Yield_Sum/Yield_Sum)* (Err_Yield_Sum/Yield_Sum) ))
        #print "%.2f" %(DiBoson/Yield_Sum)
        #print "%.2f" %(Yield_Sum/DiBoson*sqrt( (DiBoson_Error_Yield/DiBoson)*(DiBoson_Error_Yield/DiBoson) + (Err_Yield_Sum/Yield_Sum)* (Err_Yield_Sum/Yield_Sum) ))

        print "Top/Y\t %.2f +- %.2f" %(Top/Yield_Sum, Yield_Sum/Top*sqrt( (Top_Error_Yield/Top)*(Top_Error_Yield/Top) + (Err_Yield_Sum/Yield_Sum)* (Err_Yield_Sum/Yield_Sum) ))
        #print "%.2f" %(Top/Yield_Sum)
        #print "%.2f" %(Yield_Sum/Top*sqrt( (Top_Error_Yield/Top)*(Top_Error_Yield/Top) + (Err_Yield_Sum/Yield_Sum)* (Err_Yield_Sum/Yield_Sum) ))

        print "DY/Y\t%.2f +- %.2f" %(DY/Yield_Sum, Yield_Sum/DY*sqrt( (DY_Error_Yield/DY)*(DY_Error_Yield/DY) + (Err_Yield_Sum/Yield_Sum)* (Err_Yield_Sum/Yield_Sum) ))
        #print "%.2f" %(DY/Yield_Sum)
        #print "%.2f" %(Yield_Sum/DY*sqrt( (DY_Error_Yield/DY)*(DY_Error_Yield/DY) + (Err_Yield_Sum/Yield_Sum)* (Err_Yield_Sum/Yield_Sum) ))
        #print "\v" 
        Yield_Sum = 0.0 
        Err_Yield_Sum = 0.0 
        for sample in sample_names:
            if sample =="W4JetsToLNu" and selection == "PreselectionTT":
	       print   sample.ljust(15) +" 00.00 +- 0.00"
	       #print   "0.00"
	       #print   "0.00"
               continue
            else:
	       Error_Yield = root.Double()
               hist = input_dir.Get(sample + "_"+ selection + "_amuMass_0")
               first_bin = hist.FindBin(0)
               last_bin  = hist.GetXaxis().GetNbins()
               Yield  = hist.IntegralAndError(first_bin , last_bin , Error_Yield )
               Yield_Sum = Yield_Sum + Yield
               Err_Yield_Sum = sqrt((Err_Yield_Sum*Err_Yield_Sum)+(Error_Yield*Error_Yield))
	       print   sample.ljust(15) + " %.2f +- %.2f" % (Yield, Error_Yield )
	       #print   " %.2f" % (Yield)
	       #print   " %.2f" % (Error_Yield)
	print   "Yield Sum\t %.2f +- %.2f" % (Yield_Sum, Err_Yield_Sum)
	#print   " %.2f" % (Yield_Sum)
	#print   " %.2f" % (Err_Yield_Sum)

