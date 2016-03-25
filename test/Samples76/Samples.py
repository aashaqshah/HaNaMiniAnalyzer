from Haamm.HaNaMiniAnalyzer.Sample import *

import os
Sample.WD = os.path.dirname(os.path.abspath(__file__))
print Sample.WD

MiniAOD76Samples = []

SingleMu76 = Sample( "SingleMu" , "Data" , 0 , False , 0 , "/SingleMuon/Run2015D-16Dec2015-v1/MINIAOD" )
#MiniAOD76Samples.append( SingleMu76 )

DoubleMu76 = Sample("DoubleMu" , "Data" , 0 , False , 0 , "/DoubleMuon/Run2015D-16Dec2015-v1/MINIAOD" )
MiniAOD76Samples.append( DoubleMu76 )

WJetsMG76 = Sample( "WJetsMG" , "VJets" , 61526.7 , False , 0 , "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM" )
MiniAOD76Samples.append( WJetsMG76 )

DYJets76 = Sample( "DYJets" , "VJets" , 6025.2 , True , 0 , "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext4-v1/MINIAODSIM" )
MiniAOD76Samples.append( DYJets76 )

TTBar76 = Sample( "TTbar" , "Top" , 831.76 , False , 0 , "/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext3-v1/MINIAODSIM" )
MiniAOD76Samples.append( TTBar76 )

TChannel76 = Sample("TChannel" , "Top" , 70.3 , True , 0 , "/ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/MINIAODSIM" )
MiniAOD76Samples.append( TChannel76 )

TW76 = Sample("TW" , "Top" , 35.6 , False , 0 , "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM" )
MiniAOD76Samples.append( TW76 )

TbarW76 = Sample("TbarW" , "Top" , 35.6 , False , 0 , "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM" )
MiniAOD76Samples.append( TbarW76 )

QCDMuEnriched76 = Sample( "QCDMuEnriched" , "QCD" , 381304 , False , 0 , "/QCD_Pt-20toInf_MuEnrichedPt15_TuneCUETP8M1_13TeV_pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM" )

MiniAOD76Samples.append(QCDMuEnriched76)

