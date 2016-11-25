from Haamm.HaNaMiniAnalyzer.Sample import *

import os
Sample.WD = os.path.dirname(os.path.abspath(__file__))
print Sample.WD

MiniAOD80Samples = []

DoubleMuB80 = Sample("DoubleMuB" , 0 , False ,  "/DoubleMuon/Run2016B-PromptReco-v2/MINIAOD" )
MiniAOD80Samples.append( DoubleMuB80 )

DoubleMuC80 = Sample("DoubleMuC" , 0 , False ,  "/DoubleMuon/Run2016C-PromptReco-v2/MINIAOD" )
MiniAOD80Samples.append( DoubleMuC80 )

DoubleMuD80 = Sample("DoubleMuD" , 0 , False ,  "/DoubleMuon/Run2016D-PromptReco-v2/MINIAOD" )
MiniAOD80Samples.append( DoubleMuD80 )

WJetsMG80 = Sample( "WJetsMG" , 61526.7 , False , "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext1-v1/MINIAODSIM" )
MiniAOD80Samples.append( WJetsMG80 )

DYJets80 = Sample( "DYJets" , 6025.2 , True ,  "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM" )
MiniAOD80Samples.append( DYJets80 )

DYJetsLowMass80 = Sample( "DYJetsLowMass" , 18610.0 , True ,  "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM" )
MiniAOD80Samples.append( DYJetsLowMass80 )

TTBar80 = Sample( "TTbar" , 831.80 , False ,  "/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext3-v1/MINIAODSIM" )
MiniAOD80Samples.append( TTBar80 )

TChannel80 = Sample("TChannel" , 70.3 , True ,  "/ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14_ext1-v1/MINIAODSIM" )
MiniAOD80Samples.append( TChannel80 )

TW80 = Sample("TW" , 35.6 , False ,  "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/MINIAODSIM" )
MiniAOD80Samples.append( TW80 )

TbarW80 = Sample("TbarW" , 35.6 , False ,  "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM" )
MiniAOD80Samples.append( TbarW80 )

QCDMuEnriched80 = Sample( "QCDMuEnriched" , 381304 , False , "/QCD_Pt-20toInf_MuEnrichedPt15_TuneCUETP8M1_13TeV_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM" )

MiniAOD80Samples.append(QCDMuEnriched80)

ZZ80 = Sample( "ZZ" ,  15.4*2*0.071 , True ,  "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM" )

MiniAOD80Samples.append(ZZ80)

WZ80 = Sample( "WZ" ,  44.9*0.068 , True ,  "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM" )

MiniAOD80Samples.append(WZ80)

WW80 = Sample( "WW" ,  118.7 , False ,  "/WW_TuneCUETP8M1_13TeV-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM")

MiniAOD80Samples.append(WW80)

GGH1580 = Sample( "GGH15", 100*43.62*1.7*0.0001,False, "/SUSYGluGluToHToAA_AToMuMu_AToBB_M-15_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM")
MiniAOD80Samples.append(GGH1580)

GGH2080 = Sample( "GGH20", 100*43.62*1.7*0.0001,False, "/SUSYGluGluToHToAA_AToMuMu_AToBB_M-20_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM")
MiniAOD80Samples.append(GGH2080)

GGH2580 = Sample( "GGH25",100*43.62*1.7*0.0001 ,False, "/SUSYGluGluToHToAA_AToMuMu_AToBB_M-25_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM")
MiniAOD80Samples.append(GGH2580)

GGH3080 = Sample( "GGH30", 100*43.62*1.7*0.0001 ,False, "/SUSYGluGluToHToAA_AToMuMu_AToBB_M-30_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM")
MiniAOD80Samples.append(GGH3080)

GGH3580 = Sample( "GGH35", 100*43.62*1.7*0.0001 ,False, "/SUSYGluGluToHToAA_AToMuMu_AToBB_M-35_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM")
MiniAOD80Samples.append(GGH3580)

GGH4080 = Sample( "GGH40", 100*43.62*1.7*0.0001 ,False, "/SUSYGluGluToHToAA_AToMuMu_AToBB_M-40_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM")
MiniAOD80Samples.append(GGH4080)

GGH4580 = Sample( "GGH45", 100*43.62*1.7*0.0001 ,False, "/SUSYGluGluToHToAA_AToMuMu_AToBB_M-45_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM")
MiniAOD80Samples.append(GGH4580)

GGH5080 = Sample( "GGH50", 100*43.62*1.7*0.0001 ,False, "/SUSYGluGluToHToAA_AToMuMu_AToBB_M-50_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM")
MiniAOD80Samples.append(GGH5080)

GGH5580 = Sample( "GGH55", 100*43.62*1.7*0.0001 ,False, "/SUSYGluGluToHToAA_AToMuMu_AToBB_M-55_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM")
MiniAOD80Samples.append(GGH5580)

GGH6080 = Sample( "GGH60", 100*43.62*1.7*0.0001 ,False, "/SUSYGluGluToHToAA_AToMuMu_AToBB_M-60_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM")
MiniAOD80Samples.append(GGH6080)

DYBB107080 = Sample( "DYBB1070", 6.316 ,False, "/DYBBJetsToLL_M-10To70_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM")
MiniAOD80Samples.append(DYBB107080)
