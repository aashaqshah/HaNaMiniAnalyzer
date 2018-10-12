import FWCore.ParameterSet.Config as cms
Hamb = cms.EDFilter('TreeHamb',
                     LHE = cms.PSet ( useLHEW = cms.bool( False ),
                                      Input = cms.InputTag("externalLHEProducer")
                                      ),

                     HLT_Mu17Mu8 = cms.PSet( Input = cms.InputTag( "TriggerResults","","HLT" ), 
                                     HLT_To_Or = cms.vstring(),
                                     PrintTrigNamesPerRun = cms.bool( False )
                                     ),
                     HLT_Mu17Mu8_DZ = cms.PSet( Input = cms.InputTag( "TriggerResults","","HLT" ), 
                                       HLT_To_Or = cms.vstring(),
                                       PrintTrigNamesPerRun = cms.bool( False )
                                     ),
                     Vertex = cms.PSet( Input = cms.InputTag( "offlineSlimmedPrimaryVertices" ),
                                        pileupSrc = cms.InputTag("slimmedAddPileupInfo"),
                                        PUDataFileName = cms.string("pileUpData.root")
                                        ),
                     DiMuon = cms.PSet( Input = cms.InputTag("slimmedMuons"),
                                        MuonLeadingPtCut = cms.double(18),
                                        MuonSubLeadingPtCut = cms.double(9),
                                        MuonIsoCut = cms.double( 0.25 ),  # VeryTightRelIso=0.10, TightRelIso=0.15, MediumRelIso=0.20,
                                                                          # LooseRelIso=0.25, VeryLooseRelIso=0.4  
                                                                          # LooseRelTkIso=0.10, TightRelTkIso =0.05
                                                                          #Cut based have not been defined yet for 2017 data.
                                        MuonEtaCut = cms.double( 2.4 ),
                                        DiMuLowMassCut = cms.double(10.0),  # Remove the dimu lower bound
                                        DiMuCharge = cms.int32( -1 ),
                                        MuonID = cms.int32( 1 ),            # 0:no id, 1:Loose, 2:Medium, 3:tight, 4:soft, 
                                                                            # 5:HighPt, 6:MediumPrompt, 7:TrkHighPt 
                                        DiMuZMassWindow = cms.double( 200 ), # 70-->Remove the dimu upper bound 
                                        #DiMuZMassWindow = cms.double( 70 ), # 70-->Remove the dimu upper bound 
					isHamb = cms.bool(True),
					isSignalStudy = cms.bool(False),
                                        HLTUnc = cms.int32(0)
                                        ),

                     MET = cms.PSet( Input = cms.InputTag("slimmedMETs"),
                                     Cut = cms.double(100.),
                                     Uncertainty = cms.int32(-1)
                                     #http://cmsdoxygen.web.cern.ch/cmsdoxygen/CMSSW_8_4_0_patch2/doc/html/db/deb/classpat_1_1MET.html#a5c8ea7c9575730bedb6f1639140a7422
                                     #enum  	METUncertainty {
                                     #   JetResUp =0, JetResDown =1, JetEnUp =2, JetEnDown =3,
                                     #   MuonEnUp =4, MuonEnDown =5, ElectronEnUp =6, ElectronEnDown =7,
                                     #   TauEnUp =8, TauEnDown =9, UnclusteredEnUp =10, UnclusteredEnDown =11,
                                     #   PhotonEnUp =12, PhotonEnDown =13, NoShift =14, METUncertaintySize =15,
                                     #   JetResUpSmear =16, JetResDownSmear =17, METFullUncertaintySize =18
                                     # }                                   
                                     #oldjets = cms.InputTag("slimmedJets"),
				     #metsig = cms.InputTag("METSignificance:METSignificance:HaNa")	
                                     ),
                     Jets = cms.PSet( Input = cms.InputTag("slimmedJets"),
                                      ApplyJER = cms.bool( False ),
                                      JECUncertainty = cms.int32(0),
                                      JERUncertainty = cms.int32(0),
                                      JetPtCut = cms.double( 12. ),
                                      JetEtaCut = cms.double( 2.4 ),
                                      BTagAlgo = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
                                      BTagAlgoType = cms.string("CSVv2"),
                                      BTagAlgoSubTypeA = cms.string(" "), #To be overwritten in DeepCSV Algo
                                      BTagAlgoSubTypeB = cms.string(" "), #To be overwritten in DeepCSV Algo
                                      BTagWPL = cms.double(  0.5803  ),
                                      BTagWPM = cms.double(  0.8838  ),
                                      BTagWPT = cms.double(  0.9693 ),
                                      #Which WP to use in selection: 0,1,2 ---> L, M, T
                                      # -1 ---> no requirement
                                      BTagCuts = cms.vint32(1,-1), # supporting up to two working point, the second is for veto
                                      BTagUncertainty = cms.int32(0),
                                      MinNJets = cms.uint32( 2 ),
                                      MinNBJets = cms.uint32( 0 ),
                                      #MinNBJets = cms.uint32( 2 ),
				      MaxNBJets = cms.int32( -1 ),
                                      BTagWeightShapes = cms.bool( True ),
                                      BTagWeightNonShapes = cms.bool( False )
                                      ),
                     
                     sample = cms.string("WJetsMG"),
                     isData = cms.bool( False ),
                     SetupDir = cms.string("Setup94"),
		     		 StoreEventNumbers = cms.bool( True ),
		     		 forOptimization = cms.untracked.bool(False)
)
