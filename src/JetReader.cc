#include "Haamm/HaNaMiniAnalyzer/interface/JetReader.h"


JetReader::JetReader( edm::ParameterSet const& iConfig, edm::ConsumesCollector && iC, bool isData , string SetupDir, string sample ) :
  BaseEventReader< pat::JetCollection >( iConfig , &iC ),
  unc (iConfig.getParameter<int> ("JECUncertainty")),
  jerunc (iConfig.getParameter<int> ("JERUncertainty")),
  btagunc (iConfig.getParameter<int> ("BTagUncertainty")),
  IsData( isData ),
  SampleName(sample ),
  ApplyJER( iConfig.getParameter<bool>( "ApplyJER" ) ),
  JetPtCut( iConfig.getParameter<double>( "JetPtCut" ) ),
  JetEtaCut( iConfig.getParameter<double>( "JetEtaCut" ) ),
  MinNJets( iConfig.getParameter<unsigned int>( "MinNJets" ) ),
  BTagWPL( iConfig.getParameter<double>( "BTagWPL" ) ),
  BTagWPM( iConfig.getParameter<double>( "BTagWPM" ) ),
  BTagWPT( iConfig.getParameter<double>( "BTagWPT" ) ),
  BTagAlgo( iConfig.getParameter<string>( "BTagAlgo" ) ),
  BTagAlgoType( iConfig.getParameter<string>( "BTagAlgoType" ) ),
  BTagAlgoSubTypeA( iConfig.getParameter<string>( "BTagAlgoSubTypeA" ) ),
  BTagAlgoSubTypeB( iConfig.getParameter<string>( "BTagAlgoSubTypeB" ) ),
  BTagWeightShapes( iConfig.getParameter<bool>( "BTagWeightShapes" ) ),
  BTagWeightNonShapes( iConfig.getParameter<bool>( "BTagWeightNonShapes" ) ),
  MinNBJets( iConfig.getParameter<unsigned int>( "MinNBJets" ) ),
  MaxNBJets( iConfig.getParameter<int>( "MaxNBJets" ) ),
  rndJER(new TRandom3( 13611360 ) )
{

 
  BTagCuts = iConfig.getParameter<std::vector<int> > ( "BTagCuts" );
  if(BTagCuts.size() > 2){
    std::cout<<"FATAL ERROR: The current code accepts up to two WP's, one for selection one for veto"<<std::endl;
    return;
  } else if(BTagCuts.size() < 2) 
    BTagCuts.push_back(-1);  

  if( !IsData ){
    if( BTagWeightNonShapes ){
    weighters.push_back(new BTagWeight(BTagAlgoType , 0 , SetupDir, 1 , -1 , BTagWPL, BTagWPM, BTagWPT,-1, btagunc)); 
    //btw1M
    weighters.push_back(new BTagWeight(BTagAlgoType, 1 , SetupDir, 1 , -1 , BTagWPL, BTagWPM, BTagWPT,-1, btagunc));
    //btw1T
    weighters.push_back(new BTagWeight(BTagAlgoType, 2 , SetupDir, 1 , -1 , BTagWPL, BTagWPM, BTagWPT,-1, btagunc));
    //btw1M1L
    weighters.push_back(new BTagWeight(BTagAlgoType, 1, SetupDir, 1, -1, BTagWPL, BTagWPM, BTagWPT, 0,  btagunc, 1, -1));
    //btw1T1L
    weighters.push_back(new BTagWeight(BTagAlgoType, 2, SetupDir, 1, -1, BTagWPL, BTagWPM, BTagWPT, 0,  btagunc, 1, -1));
    //btw1T1M
    weighters.push_back(new BTagWeight(BTagAlgoType, 2, SetupDir, 1, -1, BTagWPL, BTagWPM, BTagWPT, 1,  btagunc, 1, -1));
    //btw2L
    weighters.push_back(new BTagWeight(BTagAlgoType, 0 , SetupDir, 2 , 2 , BTagWPL, BTagWPM, BTagWPT,-1, btagunc));
    //btw2M
    weighters.push_back(new BTagWeight(BTagAlgoType, 1 , SetupDir, 2 , 2 , BTagWPL, BTagWPM, BTagWPT,-1, btagunc));
    //btw2T
    weighters.push_back(new BTagWeight(BTagAlgoType, 2 , SetupDir, 2 , 2 , BTagWPL, BTagWPM, BTagWPT,-1, btagunc));
   }

  if( BTagWeightShapes ){
      BTagWeighterShape = new BTagWeight(BTagAlgoType , BTagAlgo, SetupDir );
    }
    t_Rho_ = (iC.consumes<double>( edm::InputTag( "fixedGridRhoFastjetAll" ) ) );
    resolution = JME::JetResolution( SetupDir + "/MCJetPtResolution.txt" );
    resolution_sf = JME::JetResolutionScaleFactor(SetupDir + "/MCJetSF.txt");
   //For JEC uncertainties for MC
    //jecUnc = new JetCorrectionUncertainty(SetupDir + "/JECUncertainties.txt");
    jecUnc = new JetCorrectionUncertainty(SetupDir + "/Fall17_17Nov2017_V32_MC_Uncertainty_AK4PFchs.txt");
  }
  if (SampleName == "DoubleMuB")      jecUnc = new JetCorrectionUncertainty(SetupDir + "/Fall17_17Nov2017B_V32_DATA_Uncertainty_AK4PFchs.txt");
  else if (SampleName == "DoubleMuC") jecUnc = new JetCorrectionUncertainty(SetupDir + "/Fall17_17Nov2017C_V32_DATA_Uncertainty_AK4PFchs.txt");
  else if (SampleName == "DoubleMuF") jecUnc = new JetCorrectionUncertainty(SetupDir + "/Fall17_17Nov2017F_V32_DATA_Uncertainty_AK4PFchs.txt");
  else                               jecUnc = new JetCorrectionUncertainty(SetupDir + "/Fall17_17Nov2017DE_V32_DATA_Uncertainty_AK4PFchs.txt");


}

const pat::JetCollection* JetReader::GetAllJets(){
  return handle.product() ;
}


JetReader::SelectionStatus JetReader::Read( const edm::Event& iEvent , pat::DiObjectProxy* diLepton ){
  BaseEventReader< pat::JetCollection >::Read( iEvent );
  for(int iComb = 0; iComb < 9; iComb++)
	weights[iComb] = 1.;

  if( (!IsData) && ApplyJER ){
    iEvent.getByToken(t_Rho_ ,rho);
    Rho = *rho;
  }


  selectedJets.clear();
  selectedBJets.clear();
  selectedJetsSortedByB.clear();

  nNonTagged = 0;
  nLooseNotMed = 0;
  nMedNotTight = 0;
  nTight = 0;

  for ( pat::Jet j : *handle) {
    if( !IsData && ApplyJER ){
      float pt = JER(j , Rho, jerunc);
      reco::Candidate::LorentzVector tmp(j.p4());
      tmp.SetPx( tmp.X()*pt/tmp.Pt() );
      tmp.SetPy( tmp.Y()*pt/tmp.Pt() );
      j.setP4(tmp);
    }
    double jetPt = j.pt();
    if (!IsData && unc != 0 ){
      jecUnc->setJetEta(j.eta());
      jecUnc->setJetPt(j.pt()); // here you must use the CORRECTED jet pt
      double uncVal = jecUnc->getUncertainty(true);
      jetPt = jetPt * (1+uncVal*unc) ; // unc = +1(up), or -1(down)
    }
    if (jetPt < JetPtCut) continue;
    if ( fabs(j.eta() ) > JetEtaCut ) continue;
    //if ( !JetLooseID( j ) ) continue;
    if ( !JetTightID( j ) ) continue;
    if( diLepton ){
      double dr0 = reco::deltaR( j.p4() , diLepton->cand1().p4() );
      double dr1 = reco::deltaR( j.p4() , diLepton->cand2().p4() );
      if( dr0 < 0.4 || dr1 < 0.4 ) continue ;
    }

    selectedJets.push_back(j);
    selectedJetsSortedByB.push_back(j);
 
    float btagval;    
    if (BTagAlgoType == "CSVv2") 
        btagval = j.bDiscriminator( BTagAlgo );
    else 
        btagval = j.bDiscriminator(BTagAlgoSubTypeA) + j.bDiscriminator(BTagAlgoSubTypeB);
  // std::cout << std::setprecision(5) << std::fixed;
  // std::cout<<"BTag Value for Discriminator\t"<<BTagAlgoType<<"\tis\t" <<btagval<<std::endl;

   if(btagval < BTagWPL) nNonTagged++;
   else if(btagval < BTagWPM) nLooseNotMed++;
   else if(btagval < BTagWPT) nMedNotTight++;
   else nTight++;

    if(BTagCuts[0] == 0) {
      if(btagval > BTagWPL) selectedBJets.push_back(j);
    } else if (BTagCuts[0] == 1) {
      if(btagval > BTagWPM) selectedBJets.push_back(j);
    } else if (BTagCuts[0] == 2) {
      if(btagval > BTagWPT) selectedBJets.push_back(j);
    } else
	selectedBJets.push_back(j);

  }
  
  ptSort<pat::Jet> mySort; 
  std::sort(selectedJets.begin(),selectedJets.end(),mySort);
  std::sort(selectedBJets.begin(),selectedBJets.end(),mySort);
  btagSort<pat::Jet> myBsort(BTagAlgo);
  std::sort(selectedJetsSortedByB.begin(),selectedJetsSortedByB.end(),myBsort);
 
    
  if( selectedJets.size() < MinNJets ) return JetReader::NotEnoughJets ;
  if(  selectedBJets.size() < MinNBJets ) return JetReader::NotEnoughBJets;
  if(!IsData){
    if( BTagWeightNonShapes ){
      for(int iComb = 0; iComb < 9; iComb++)
	if(iComb < 3 || iComb > 5){
	  //cout<<"-- "<<iComb <<", weight"<<endl;
	  weights[iComb] = weighters[iComb]->weight(selectedJets);
	} else {
	  //cout<<"-- "<<iComb <<", weightExclusive"<<endl;
	  weights[iComb] = weighters[iComb]->weightExclusive(selectedJets);
	}
    }
    if( BTagWeightShapes ){
      shape_weights[0]=BTagWeighterShape->weightShape(selectedJets , 0);
      if( btagunc != 0){
	for( int isyst = 1 ; isyst < 10 ; isyst ++){
	  shape_weights[isyst*2-1]=BTagWeighterShape->weightShape(selectedJets , isyst);
	  shape_weights[isyst*2]=BTagWeighterShape->weightShape(selectedJets , -1*(isyst) );
	}
      }
    }
  }
  return JetReader::Pass;
}

float JetReader::JER( pat::Jet jet , double rho , int syst ){
  JME::JetParameters parameters_1;
  parameters_1.setJetPt(jet.pt());
  parameters_1.setJetEta(jet.eta());
  parameters_1.setRho( rho );
  //float sf = resolution_sf.getScaleFactor(parameters_1);
  float sf = resolution_sf.getScaleFactor(parameters_1,Variation(jerunc));

  const reco::GenJet*  genjet =  jet.genJet ();
  float ret = jet.pt();
  if( genjet != NULL && genjet->pt() > 0 ){
    ret = max(0., genjet->pt() + sf*( jet.pt() - genjet->pt() ) );
  }else{
    float r = resolution.getResolution(parameters_1);
    ret = rndJER->Gaus( jet.pt() , r*sqrt( sf*sf - 1) );
  }
  return ret;
}

bool JetReader::JetTightID( pat::Jet j ){
  float NHF = j.neutralHadronEnergyFraction ();
  float NEMF = j.neutralEmEnergyFraction ();
  int NumConst = j.numberOfDaughters ();
  float eta = j.eta();
  float CHF = j.chargedHadronEnergyFraction ( ) ;
  float CHM = j.chargedMultiplicity ();
  //float CEMF = j.chargedEmEnergyFraction (); //Not used in 94X any where and hence commented.
  int NumNeutralParticle = j.neutralMultiplicity ( );
  bool TightJetID1 = (NEMF<0.90 && NHF<0.90 && NumConst>1) && ((abs(eta)<=2.4 && CHF>0.0 && CHM>0.0) || abs(eta)>2.4) && abs(eta)<=2.7;
  bool TightJetID2 = (NEMF<0.99 && NEMF>0.02 && NumNeutralParticle>2) && (abs(eta)>2.7 && abs(eta)<=3.0) ;
  bool TightJetID3 = (NEMF<0.90 && NHF>0.02 && NumNeutralParticle>10 && abs(eta)>3.0 ) ;
  return TightJetID1 || TightJetID2 || TightJetID3;
}
