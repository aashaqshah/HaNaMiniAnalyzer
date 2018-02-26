import FWCore.ParameterSet.Config as cms

process = cms.Process("HaNa")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("RecoMET/METProducers.METSignificance_cfi")
process.load("RecoMET/METProducers.METSignificanceParams_cfi")
##____________________________________________________________________________||
process.load('Configuration.StandardSequences.Services_cff')
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
#process.load("JetMETCorrections.Modules.JetResolutionESProducer_cfi")
#from CondCore.DBCommon.CondDBSetup_cfi import *

#process.jer = cms.ESSource("PoolDBESSource",
#      CondDBSetup,
#      toGet = cms.VPSet(
#         # Pt Resolution
#         cms.PSet(
#            record = cms.string('JetResolutionRcd'),
#            tag    = cms.string('JR_MC_PtResolution_Summer15_25nsV6_AK4PFchs'),
#            label  = cms.untracked.string('AK4PFchs_pt')
#            ),
#
#         # Phi Resolution
#         cms.PSet(
#            record = cms.string('JetResolutionRcd'),
#            tag    = cms.string('JR_MC_PhiResolution_Summer15_25nsV6_AK4PFchs'),
#            label  = cms.untracked.string('AK4PFchs_phi')
#            ),
#
#         # Scale factors
#         cms.PSet(
#            record = cms.string('JetResolutionScaleFactorRcd'),
#            tag    = cms.string('JR_DATAMCSF_Summer15_25nsV6_AK4PFchs'),
#            label  = cms.untracked.string('AK4PFchs')
#            ),
#         ),
#      connect = cms.string('sqlite:Summer15_25nsV6.db')
#      )

#process.es_prefer_jer = cms.ESPrefer('PoolDBESSource', 'jer')

##____________________________________________________________________________||
process.TFileService = cms.Service("TFileService", fileName = cms.string("histo.root") )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )
process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
                            fileNames = cms.untracked.vstring()
)

process.load("Haamm.HaNaMiniAnalyzer.Hamb_cfi")
#process.TTH 

import FWCore.ParameterSet.VarParsing as opts
options = opts.VarParsing ('analysis')
options.register('sync',
                 0,
		 #1,
                 opts.VarParsing.multiplicity.singleton,
                 opts.VarParsing.varType.int ,
                 "")
options.register('sample',
		 'TTbar',
                 opts.VarParsing.multiplicity.singleton,
                 opts.VarParsing.varType.string,
                 'Sample to analyze')
options.register('job',
                 0,
                 opts.VarParsing.multiplicity.singleton,
                 opts.VarParsing.varType.int ,
                 "number of the job")
options.register('nFilesPerJob',
                 1,
                 opts.VarParsing.multiplicity.singleton,
                 opts.VarParsing.varType.int ,
                 "number of the files pre job")
options.register('output',
                 "out",
                 opts.VarParsing.multiplicity.singleton,
                 opts.VarParsing.varType.string ,
                 "could be root://eoscms//eos/cms/store/user/hbakhshi/out")

options.parseArguments()


theSample = None
import os

if options.sync == 0 :
    #from Samples80.Samples import MiniAOD80Samples as samples
    from Samples94.Samples import MiniAOD94Samples as samples


    for sample in samples:
        if sample.Name == options.sample :
            theSample = sample

    if not theSample.Name == options.sample:
        raise NameError("The correct sample is not found %s !+ %s" % (sample.Name , options.sample) )

    if theSample == None:
        raise NameError("Sample with name %s wasn't found" % (options.sample))
else:
    from Haamm.HaNaMiniAnalyzer.Sample import *
    theSample = Sample( "Sync" , "Sync" , 100 , False , 0 , "" )
    #theSample.Files = ['/store/mc/RunIIFall15MiniAODv2/TT_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext3-v1/00000/0C5BB11A-E2C1-E511-8C02-002590A831B6.root']
    theSample.Files = ['/store/mc/RunIISpring16MiniAODv2/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/001AFDCE-C33B-E611-B032-0025905D1C54.root']
    #theSample.Files = ['/store/data/Run2016C/DoubleMuon/MINIAOD/PromptReco-v2/000/275/658/00000/0498AA19-863B-E611-A9B3-02163E0138A8.root']
    options.nFilesPerJob = 1
    options.output = "out" 
    options.job = 0

process.Hamb.sample = theSample.Name
process.Hamb.LHE.useLHEW = theSample.LHEWeight
process.Hamb.isData = theSample.IsData
process.Hamb.Jets.BTagCuts = cms.vint32(0,-1)
process.Hamb.DiMuon.MuonLeadingPtCut = cms.double(20)

if not ( options.job < theSample.MakeJobs( options.nFilesPerJob , options.output ) ):
    raise NameError("Job %d is not in the list of the jobs of sample %s with %d files per run" % (options.job , options.sample , options.nFilesPerJob ) )
job = theSample.Jobs[ options.job ]

process.source.fileNames.extend( job.Inputs )
process.TFileService.fileName = job.Output

process.maxEvents.input = options.maxEvents

#from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
#runMetCorAndUncFromMiniAOD(process, isData = theSample.IsData)

if theSample.IsData :
    #process.Hamb.MET.Input = "slimmedMETsMuEGClean"
    
    import FWCore.PythonUtilities.LumiList as LumiList
    process.source.lumisToProcess = LumiList.LumiList(filename = (process.Hamb.SetupDir.value() + '/JSON.txt')).getVLuminosityBlockRange()
    #process.GlobalTag.globaltag = '80X_dataRun2_Prompt_ICHEP16JEC_v0
    process.GlobalTag.globaltag = '80X_dataRun2_2016SeptRepro_v7'
    if (theSample.Name is 'DoubleMuH2') or (theSample.Name is 'DoubleMuH3'):
	process.GlobalTag.globaltag = '80X_dataRun2_Prompt_v16'
    
    
    #process.p = cms.Path( process.fullPatMetSequence+process.METSignificance + process.Hamb )
    process.p = cms.Path( process.Hamb )
    for v in range(0 , 8):
        process.Hamb.HLT_Mu17Mu8_DZ.HLT_To_Or.append( 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v%d' % (v) )
        process.Hamb.HLT_Mu17Mu8_DZ.HLT_To_Or.append( 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v%d' % (v) )
        process.Hamb.HLT_Mu17Mu8_DZ.HLT_To_Or.append( 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v%d' % (v) )   #2017 Trigger
        process.Hamb.HLT_Mu17Mu8_DZ.HLT_To_Or.append( 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v%d' % (v) ) #2017 Trigger
        process.Hamb.HLT_Mu17Mu8.HLT_To_Or.append( 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v%d' % (v) )
        process.Hamb.HLT_Mu17Mu8.HLT_To_Or.append( 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v%d' % (v) )
        process.Hamb.HLT_Mu17Mu8.HLT_To_Or.append( 'HLT_IsoMu24_v%d' % (v) )

else :
    #from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD

   # If you only want to re-correct and get the proper uncertainties
    #runMetCorAndUncFromMiniAOD(process,
    #                           isData=False
    #                           )
    process.Hamb.MET.Input = "slimmedMETs"

    process.Hamb.Jets.ApplyJER = True
    process.GlobalTag.globaltag = '94X_mc2017_realistic_v12'
    from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import *
    #process.patJetCorrFactorsReapplyJEC = updatedPatJetCorrFactors.clone(
    #     src = cms.InputTag("slimmedJets"),
    #     levels = ['L1FastJet', 
    #               'L2Relative', 
    #               'L3Absolute'],
    #     payload = 'AK4PFchs' ) # Make sure to choose the appropriate levels and payload here!

    #process.patJetsReapplyJEC = updatedPatJets.clone(
    #     jetSource = cms.InputTag("slimmedJets"),
    #     jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsReapplyJEC"))
    #     )

    #process.Hamb.Jets.Input = "patJetsReapplyJEC"
    # process.METSignificance.srcPfJets = "patJetsReapplyJEC"
    #  + process.METSignificance
    process.p = cms.Path( process.Hamb)
    #process.p = cms.Path( process.fullPatMetSequence + process.Hamb)
    if options.sync == 0 :
        for v in range(0 , 8 ):
            process.Hamb.HLT_Mu17Mu8_DZ.HLT_To_Or.append( 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v%d' % (v) )
            process.Hamb.HLT_Mu17Mu8_DZ.HLT_To_Or.append( 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v%d' % (v) )
            process.Hamb.HLT_Mu17Mu8_DZ.HLT_To_Or.append( 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v%d' % (v) )  
            process.Hamb.HLT_Mu17Mu8_DZ.HLT_To_Or.append( 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v%d' % (v) )
            process.Hamb.HLT_Mu17Mu8.HLT_To_Or.append( 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v%d' % (v) )
            process.Hamb.HLT_Mu17Mu8.HLT_To_Or.append( 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v%d' % (v) )
            process.Hamb.HLT_Mu17Mu8.HLT_To_Or.append( 'HLT_IsoMu24_v%d' % (v) )

    if theSample.DSName.count( "_reHLT_" ):
	process.Hamb.HLT_Mu17Mu8_DZ.Input = cms.InputTag( "TriggerResults","","HLT2" )
	process.Hamb.HLT_Mu17Mu8.Input = cms.InputTag( "TriggerResults","","HLT2" )
process.outp1=cms.OutputModule("PoolOutputModule",
   outputCommands = cms.untracked.vstring('keep *'), 
   fileName = cms.untracked.string(job.Output2),
   SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring('p')  )
)
process.HambDeepCSV = process.Hamb.clone()
process.HambDeepCSV.Jets.BTagAlgo = "pfDeepCSVJetTags:probb + pfDeepCSVJetTags:probbb"
process.HambDeepCSV.Jets.BTagWPL = 0.1522
process.HambDeepCSV.Jets.BTagWPM = 0.4941
process.HambDeepCSV.Jets.BTagWPT = 0.8001
process.HambDeepCSV.Jets.BTagAlgoType = "DeepCSV"
process.HambDeepCSV.Jets.BTagAlgoSubTypeA = "pfDeepCSVJetTags:probb"
process.HambDeepCSV.Jets.BTagAlgoSubTypeB = "pfDeepCSVJetTags:probbb"

process.p2 = cms.Path( process.HambDeepCSV )

process.ep = cms.EndPath( process.outp1 )

