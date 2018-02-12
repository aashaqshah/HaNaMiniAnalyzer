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

#WJetsMG94 = Sample( "WJetsMG" , 61526.7 , False , "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM" )
#MiniAOD94Samples.append( WJetsMG94 )

DYJetsH100T20094 = Sample( "DYJetsH100T200" , 203.3 , False ,  "/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" )
MiniAOD94Samples.append( DYJetsH100T20094 )

DYJetsH200T40094 = Sample( "DYJets200T400" , 52.46 , False ,  "/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" )
MiniAOD94Samples.append( DYJetsH200T40094 )

DYJetsH400T60094 = Sample( "DYJets400T600" , 5.539 , False ,  "/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM" )
MiniAOD94Samples.append( DYJetsH400T60094 )

DYJetsH600TInf94 = Sample( "DYJets600TInf" , 1.885 , False ,  "/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" )
MiniAOD94Samples.append( DYJetsH600TInf94 )

#DYJetsLowMass94 = Sample( "DYJetsLowMass" , 18610.0 , True ,  "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM" )
#MiniAOD94Samples.append( DYJetsLowMass94 )

#TTBar94 = Sample( "TTbar" , 831.80 , False ,  "/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM" )
#MiniAOD94Samples.append( TTBar94 )

#TChannelTbar94 = Sample("TChannelTbar" , 81 , True ,  "/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM" )
#MiniAOD94Samples.append( TChannelTbar94 )

#TChannelT94 = Sample("TChannelT" , 136 , True ,  "/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM" )
#MiniAOD94Samples.append( TChannelT94 )

#TW94 = Sample("TW" , 35.6 , False ,  "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM" )
#MiniAOD94Samples.append( TW94 )

#TbarW94 = Sample("TbarW" , 35.6 , False ,  "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM" )
#MiniAOD94Samples.append( TbarW94 )

ZZ94 = Sample( "ZZ" ,  10.32 , True ,  "/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" )
MiniAOD94Samples.append(ZZ94)

WZ94 = Sample( "WZ" ,  22.82 , True ,  "/WZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" )
MiniAOD94Samples.append(WZ94)

WW94 = Sample( "WW" ,  63.21 , True ,  "/WW_TuneCP5_13TeV-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM")
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

