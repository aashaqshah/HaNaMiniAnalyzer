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
#
#WJetsMG94 = Sample( "WJetsMG" , 61526.7 , True , "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM" )
#MiniAOD94Samples.append( WJetsMG94 )
#
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

##TTbar94 = Sample( "TTbar" , 72.1 , True ,  "/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" )
##MiniAOD94Samples.append( TTbar94 ) # alternative inclusive sample available
#

TTTo2L2Nu94 = Sample( "TTTo2L2Nu" , 72.1 , True ,  "/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" )
#TTTo2L2Nu94 = Sample( "TTTo2L2Nu" , 831 , True ,  "/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" )
MiniAOD94Samples.append( TTTo2L2Nu94 )
#
#ZZTo2L2Nu94 = Sample( "ZZTo2L2Nu" , 0.6008 , True ,  "/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM" )
#MiniAOD94Samples.append( ZZTo2L2Nu94 )

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
#
GGH1594 = Sample( "GGH15", 48.5800*1.7*0.0001,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_Toa01a01_M15_Tomumubb/")
MiniAOD94Samples.append(GGH1594)

GGH2094 = Sample( "GGH20", 48.5800*1.7*0.0001,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_Toa01a01_M20_Tomumubb/")
MiniAOD94Samples.append(GGH2094)

GGH2594 = Sample( "GGH25",48.5800*1.7*0.0001 ,False,  "/eos/cms/store/user/aashah/Samples94/ggh01_M125_Toa01a01_M25_Tomumubb/")
MiniAOD94Samples.append(GGH2594)

GGH3094 = Sample( "GGH30", 48.5800*1.7*0.0001 ,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_Toa01a01_M30_Tomumubb/")
MiniAOD94Samples.append(GGH3094)

GGH3594 = Sample( "GGH35", 48.5800*1.7*0.0001 ,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_Toa01a01_M35_Tomumubb/")
MiniAOD94Samples.append(GGH3594)

GGH4094 = Sample( "GGH40", 48.5800*1.7*0.0001 ,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_Toa01a01_M40_Tomumubb/")
MiniAOD94Samples.append(GGH4094)

GGH4594 = Sample( "GGH45", 48.5800*1.7*0.0001 ,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_Toa01a01_M45_Tomumubb/")
MiniAOD94Samples.append(GGH4594)

GGH5094 = Sample( "GGH50", 48.5800*1.7*0.0001 ,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_Toa01a01_M50_Tomumubb/")
MiniAOD94Samples.append(GGH5094)

GGH5594 = Sample( "GGH55", 48.5800*1.7*0.0001 ,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_Toa01a01_M55_Tomumubb/")
MiniAOD94Samples.append(GGH5594)

GGH6094 = Sample( "GGH60", 48.5800*1.7*0.0001 ,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_Toa01a01_M60_Tomumubb/")
MiniAOD94Samples.append(GGH6094)

VBF2094 = Sample( "VBF20", 3.7820*1.7*0.0001 ,False, "/eos/cms/store/user/aashah/Samples94/vbfh01_M125_Toa01a01_M20_Tomumubb/")
MiniAOD94Samples.append(VBF2094)

VBF3094 = Sample( "VBF30", 3.7820*1.7*0.0001 ,False, "/eos/cms/store/user/aashah/Samples94/vbfh01_M125_Toa01a01_M30_Tomumubb/")
MiniAOD94Samples.append(VBF3094)

VBF4094 = Sample( "VBF40", 3.7820*1.7*0.0001 ,False, "/eos/cms/store/user/aashah/Samples94/vbfh01_M125_Toa01a01_M40_Tomumubb/")
MiniAOD94Samples.append(VBF4094)

VBF5094 = Sample( "VBF50", 3.7820*1.7*0.0001 ,False, "/eos/cms/store/user/aashah/Samples94/vbfh01_M125_Toa01a01_M50_Tomumubb/")
MiniAOD94Samples.append(VBF5094)

VBF6094 = Sample( "VBF60", 3.7820*1.7*0.0001 ,False, "/eos/cms/store/user/aashah/Samples94/vbfh01_M125_Toa01a01_M60_Tomumubb/")
MiniAOD94Samples.append(VBF6094)

GGHbbtt2094 = Sample( "GGHbbtt20", 48.5800*1.7*0.0001,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_Toa01a01_M20_Tobbtautau/")
MiniAOD94Samples.append(GGHbbtt2094)

GGHbbtt4094 = Sample( "GGHbbtt40", 48.5800*1.7*0.0001,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_Toa01a01_M40_Tobbtautau/")
MiniAOD94Samples.append(GGHbbtt4094)

GGHbbtt6094 = Sample( "GGHbbtt60", 48.5800*1.7*0.0001,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_Toa01a01_M60_Tobbtautau/")
MiniAOD94Samples.append(GGHbbtt6094)

GGHmmtt2094 = Sample( "GGHmmtt20", 48.5800*1.7*0.0001,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_Toa01a01_M20_Tomumutautau/")
MiniAOD94Samples.append(GGHmmtt2094)

GGHmmtt4094 = Sample( "GGHmmtt40", 48.5800*1.7*0.0001,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_Toa01a01_M40_Tomumutautau/")
MiniAOD94Samples.append(GGHmmtt4094)

GGHmmtt6094 = Sample( "GGHmmtt60", 48.5800*1.7*0.0001,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_Toa01a01_M60_Tomumutautau/")
MiniAOD94Samples.append(GGHmmtt6094)

#Crossection h->Za->2m2b
#h->Za = 10 %, Z->bb = 15% benchmark, a->mm = 3 * 10^-3 (from BR plotter (basically model dependent) 
# so 48.5 *0.10 *0.15* 3*0.001 = 0.0021

#Za0394 = Sample( "Za03", 48.5800*0.10*0.15*3*0.001 ,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_ToZa01_M91M03_Tomumubb")
#MiniAOD94Samples.append(Za0394)
#
#Za0694 = Sample( "Za06", 48.5800*0.10*0.15*3*0.001 ,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_ToZa01_M91M06_Tomumubb")
#MiniAOD94Samples.append(Za0694)
#
#Za0994 = Sample( "Za09", 48.5800*0.10*0.15*3*0.001 ,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_ToZa01_M91M09_Tomumubb")
#MiniAOD94Samples.append(Za0994)

Za1294 = Sample( "Za12", 48.5800*0.10*0.15*3*0.001 ,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_ToZa01_M91M12_Tomumubb")
MiniAOD94Samples.append(Za1294)

Za1594 = Sample( "Za15", 48.5800*0.10*0.15*3*0.001 ,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_ToZa01_M91M15_Tomumubb")
MiniAOD94Samples.append(Za1594)

Za2094 = Sample( "Za20", 48.5800*0.10*0.15*3*0.001 ,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_ToZa01_M91M20_Tomumubb")
MiniAOD94Samples.append(Za2094)

Za2594 = Sample( "Za25", 48.5800*0.10*0.15*3*0.001 ,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_ToZa01_M91M25_Tomumubb")
MiniAOD94Samples.append(Za2594)

Za3094 = Sample( "Za30", 48.5800*0.10*0.15*3*0.001 ,False, "/eos/cms/store/user/aashah/Samples94/ggh01_M125_ToZa01_M91M30_Tomumubb")
MiniAOD94Samples.append(Za3094)

