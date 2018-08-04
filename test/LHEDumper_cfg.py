import FWCore.ParameterSet.Config as cms
# cmsRun LHEDumper_cfg.py sample=GGH20 nFilesPerJob=1 job=0  
process = cms.Process("HaNa")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
##____________________________________________________________________________||
process.load('Configuration.StandardSequences.Services_cff')
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
from Configuration.AlCa.GlobalTag import GlobalTag

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
                            fileNames = cms.untracked.vstring()
)

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

if not ( options.job < theSample.MakeJobs( options.nFilesPerJob , options.output ) ):
    raise NameError("Job %d is not in the list of the jobs of sample %s with %d files per run" % (options.job , options.sample , options.nFilesPerJob ) )
job = theSample.Jobs[ options.job ]

process.source.fileNames.extend( job.Inputs )
process.maxEvents.input = options.maxEvents

process.writer = cms.EDAnalyzer('LHEWriter',
                                moduleLabel = cms.untracked.InputTag('externalLHEProducer'))
process.p2 = cms.Path( process.writer )


