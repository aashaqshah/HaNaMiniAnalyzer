import json
import ROOT
import array
from ROOT import TH1, TFile, TH2
import os, math

f = open('RunBCDEF_SF_ID.json', 'r')
j = json.load(f)
fOut = TFile.Open("MuonIDSF.root" , "RECREATE")

ID = ["Tight", "Medium" , "Loose", "Soft", "HighPt", "MediumPrompt", "TrkHighPt"]
for id in ID:
    if id == "Tight" or id =="Medium" or id == "Loose" or id == "Soft" or id =="MediumPrompt":
       output_dir = "MC_NUM_%sID_DEN_genTracks_PAR_pt_eta" % (id)
       input_dir = "NUM_%sID_DEN_genTracks" %(id)
       sub_input_dir = "abseta_pt"
    else:
       output_dir = "MC_NUM_%sID_DEN_genTracks_PAR_pt_eta" % (id)
       input_dir = "NUM_%sID_DEN_genTracks" %(id)
       sub_input_dir = "abseta_pair_newTuneP_probe_pt"
    print "Processing %s ID related information"%(id)
    ROOT.gStyle.SetOptStat(0)
    #Canvas_Eff = ROOT.TCanvas(output_dir, output_dir)
    Canvas_Eff = ROOT.TCanvas("pt_abseta_ratio","pt_abseta_ratio")
    Canvas_Eff.cd()
    ptBins = array.array('d' , [20. , 25., 30. , 40. , 50. , 60. , 120.])
    etaBins = array.array( 'd' , [0.0 , 0.9 , 1.2 , 2.1 , 2.4 ] )
    h = ROOT.TH2D("pt_abseta_ratio" , "pt_abseta_ratio", 6 , ptBins , 4 , etaBins )
    #h = ROOT.TH2D("pt_abseta_ratio" , "pt_abseta_ratio" , 6 , ptBins , 4 , etaBins )
    h.GetXaxis().SetTitle("muon p_{T} (GeV/c)")
    h.GetXaxis().CenterTitle()
    h.GetYaxis().SetTitle("muon |#eta|")
    h.GetYaxis().CenterTitle()
    h.SetLabelColor(1)
    h.GetXaxis().SetLabelFont(62)
    h.GetYaxis().SetLabelFont(62)
    h.SetLabelOffset(0.005)
    h.SetLabelSize(0.04)
    h.GetXaxis().SetTitleSize(0.06)
    h.SetTitleOffset(1)
    h.SetTitleSize(0.04)

    if id == "Tight" or id =="Medium" or id == "Loose" or id == "Soft" or id =="MediumPrompt":
        ptBinNames = [ "pt:[20.00,25.00]",
                     "pt:[25.00,30.00]",
                     "pt:[30.00,40.00]",
                     "pt:[40.00,50.00]" ,
                     "pt:[50.00,60.00]",
                     "pt:[60.00,120.00]"]
        etaBinNames = ["abseta:[0.00,0.90]",
                     "abseta:[0.90,1.20]",
                     "abseta:[1.20,2.10]",
                     "abseta:[2.10,2.40]"]
    else:
        ptBinNames = [ "pair_newTuneP_probe_pt:[20.00,25.00]",
                       "pair_newTuneP_probe_pt:[25.00,30.00]",
                       "pair_newTuneP_probe_pt:[30.00,40.00]",
                       "pair_newTuneP_probe_pt:[40.00,50.00]" ,
                       "pair_newTuneP_probe_pt:[50.00,60.00]",
                       "pair_newTuneP_probe_pt:[60.00,120.00]"]
        etaBinNames = ["abseta:[0.00,0.90]",
                       "abseta:[0.90,1.20]",
                       "abseta:[1.20,2.10]",
                       "abseta:[2.10,2.40]"]

    for ptBinId in range(0 , len(ptBinNames) ):
       for etaBinId in range(0 , len(etaBinNames) ):
           #value = j["NUM_MediumID_DEN_genTracks"]["abseta_pt"][etaBinNames[etaBinId] ][ptBinNames[ptBinId] ]["value"]
           #error = j["NUM_MediumID_DEN_genTracks"]["abseta_pt"][etaBinNames[etaBinId] ][ptBinNames[ptBinId] ]["error"]
           #value = j[input_dir]["abseta_pt"][etaBinNames[etaBinId] ][ptBinNames[ptBinId] ]["value"]
           value = j[input_dir][sub_input_dir][etaBinNames[etaBinId] ][ptBinNames[ptBinId] ]["value"]
           error = j[input_dir][sub_input_dir][etaBinNames[etaBinId] ][ptBinNames[ptBinId] ]["error"]
           #error = j[input_dir]["abseta_pt"][etaBinNames[etaBinId] ][ptBinNames[ptBinId] ]["error"]
           etaLowestValue = etaBins[ etaBinId ]
           ptLowestValue = ptBins[ ptBinId ]
           bin_id = h.FindBin( ptLowestValue , etaLowestValue )
           h.SetBinContent( bin_id , value )
           h.SetBinError( bin_id , error )
           h.Draw("COLZ" "TEXT" "E")
           
    fOut.mkdir( output_dir ).cd()
    Canvas_Eff.Write()
    print "Created Histogram for %s ID"%(id)
    if(Canvas_Eff):
       Canvas_Eff.Close()
fOut.Close()
print "Saved 'MuonIDSF.root' file in current working directory"
message =raw_input('\nHit the Enter Key to exit the program! ')
print(message)
print "Thank You and Good Bye.!\n\n "
#fOut.Close()
exit()

