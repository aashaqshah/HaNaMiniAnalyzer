from Haamm.HaNaMiniAnalyzer.Sample import *

import os
Sample.WD = os.path.dirname(os.path.abspath(__file__))
print Sample.WD

MiniAOD94Samples = []

#Data

#B data sets
DoubleMuB94 = Sample("DoubleMuB" , 0 , False ,  "/DoubleMuon/Run2017B-17Nov2017-v1/MINIAOD" )
MiniAOD94Samples.append( DoubleMuB94 )

#C data Sets
DoubleMuC94 = Sample("DoubleMuC" , 0 , False ,  "/DoubleMuon/Run2017C-17Nov2017-v1/MINIAOD" )
MiniAOD94Samples.append( DoubleMuC94 )

#D data Sets
DoubleMuD94 = Sample("DoubleMuD" , 0 , False ,  "/DoubleMuon/Run2017D-17Nov2017-v1/MINIAOD" )
MiniAOD94Samples.append( DoubleMuD94 )

#E data sets
DoubleMuE94 = Sample("DoubleMuE" , 0 , False ,  "/DoubleMuon/Run2017E-17Nov2017-v1/MINIAOD" )
MiniAOD94Samples.append( DoubleMuE94 )

# F data sets
DoubleMuF94 = Sample("DoubleMuF" , 0 , False ,  "/DoubleMuon/Run2017F-17Nov2017-v1/MINIAOD" )
MiniAOD94Samples.append( DoubleMuF94 )

#Monte Carlo's

#WJetsMG94 = Sample( "WJetsMG" , 61526.7 , True , "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM" )
#MiniAOD94Samples.append( WJetsMG94 )

#WJetsToLNu94 = Sample( "WJetsLNu" , 1, True , "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PUMoriond17_94X_mcRun2_asymptotic_v2_ext2-v1/NANOAODSIM" )
#MiniAOD94Samples.append( WJetsToLNu94 )

W3JetsToLNu94 = Sample( "W3JetsToLNu" , 942.3, True , "/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v3/MINIAODSIM" )
MiniAOD94Samples.append( W3JetsToLNu94 )

W4JetsToLNu94 = Sample( "W4JetsToLNu" , 524.2, True , "/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" )
MiniAOD94Samples.append( W4JetsToLNu94 )

DYJetsLowMass94 = Sample( "DYJetsLowMass" , 18610, True ,  "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM" )
MiniAOD94Samples.append( DYJetsLowMass94 )

DYJetsHighMass94 = Sample( "DYJetsHighMass", 7181, True ,  "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1/MINIAODSIM" )
MiniAOD94Samples.append( DYJetsHighMass94 )

TTBar94 = Sample( "TTbar" , 72.1 , True ,  "/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" )
MiniAOD94Samples.append( TTBar94 ) # alternative inclusive sample available


TTTo2L2Nu94 = Sample( "TTTo2L2Nu" , 72.1 , True ,  "/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" )
MiniAOD94Samples.append( TTTo2L2Nu94 )

ZZTo2L2Nu94 = Sample( "ZZTo2L2Nu" , 0.6008 , True ,  "/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" )
MiniAOD94Samples.append( ZZTo2L2Nu94 )

TChannelTbar94 = Sample("TChannelTbar" , 80.95 , False ,  "/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" )
MiniAOD94Samples.append( TChannelTbar94 )

TChannelT94 = Sample("TChannelT" , 136.02 , False ,  "/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" )
MiniAOD94Samples.append( TChannelT94 )

TW94 = Sample("TW" , 34.91 , True ,  "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" )
MiniAOD94Samples.append( TW94 )

TbarW94 = Sample("TbarW" , 34.91 , True ,  "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" )
MiniAOD94Samples.append( TbarW94 )

ZZ94 = Sample( "ZZ" ,  10.32 , False ,  "/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" )
MiniAOD94Samples.append(ZZ94)

WZ94 = Sample( "WZ" ,  22.82 , False ,  "/WZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" )
MiniAOD94Samples.append(WZ94)

#WW94 = Sample( "WW" ,  63.21 , False ,  "/WW_TuneCP5_13TeV-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM")
WW94 = Sample( "WW" ,  118.7, False ,  "/WW_TuneCP5_13TeV-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM")
MiniAOD94Samples.append(WW94)

#GGH1594 = Sample( "GGH15", 43.62*1.7*0.0001,False, "/SUSYGluGluToHToAA_AToMuMu_AToBB_M-15_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM")
#MiniAOD94Samples.append(GGH1594)

#GGH2094 = Sample( "GGH20", 43.62*1.7*0.0001,False, "/SUSYGluGluToHToAA_AToMuMu_AToBB_M-20_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM")
#MiniAOD94Samples.append(GGH2094)

#GGH2594 = Sample( "GGH25",43.62*1.7*0.0001 ,False, "/SUSYGluGluToHToAA_AToMuMu_AToBB_M-25_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM")
#MiniAOD94Samples.append(GGH2594)

#GGH3094 = Sample( "GGH30", 43.62*1.7*0.0001 ,False, "/SUSYGluGluToHToAA_AToMuMu_AToBB_M-30_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM")
#MiniAOD94Samples.append(GGH3094)

#GGH3594 = Sample( "GGH35", 43.62*1.7*0.0001 ,False, "/SUSYGluGluToHToAA_AToMuMu_AToBB_M-35_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM")
#MiniAOD94Samples.append(GGH3594)

#GGH4094 = Sample( "GGH40", 43.62*1.7*0.0001 ,False, "/SUSYGluGluToHToAA_AToMuMu_AToBB_M-40_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM")
#MiniAOD94Samples.append(GGH4094)

#GGH4594 = Sample( "GGH45", 43.62*1.7*0.0001 ,False, "/SUSYGluGluToHToAA_AToMuMu_AToBB_M-45_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM")
#MiniAOD94Samples.append(GGH4594)

#GGH5094 = Sample( "GGH50", 43.62*1.7*0.0001 ,False, "/SUSYGluGluToHToAA_AToMuMu_AToBB_M-50_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM")
#MiniAOD94Samples.append(GGH5094)

#GGH5594 = Sample( "GGH55", 43.62*1.7*0.0001 ,False, "/SUSYGluGluToHToAA_AToMuMu_AToBB_M-55_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM")
#MiniAOD94Samples.append(GGH5594)

#GGH6094 = Sample( "GGH60", 43.62*1.7*0.0001 ,False, "/SUSYGluGluToHToAA_AToMuMu_AToBB_M-60_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM")
#MiniAOD94Samples.append(GGH6094)

