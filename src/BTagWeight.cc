#include "Haamm/HaNaMiniAnalyzer/interface/BTagWeight.h"

float BTagWeight::weightShape(pat::JetCollection jets , int syst){
  if(WPT != -100 )
    return -100.0;

  float csvWgtHF = 1., csvWgtLF = 1., csvWgtC = 1.;
  //cout << "In the weightShape method -----------------"<<endl;
  for( unsigned int iJet=0; iJet<jets.size(); iJet++ ){ 
    bool doubleUnc = false;
    float csv = jets[iJet].bDiscriminator(algo);
    float jetPt = jets[iJet].pt();
    // if(jetPt < 20){
    //   doubleUnc = true;
    // }
    float jetAbsEta = fabs(jets[iJet].eta());
    int flavor = jets[iJet].hadronFlavour();
    //cout <<"Jet number "<<iJet+1 <<" >>>>>>>>>>>>>> Syst: "<< Systs[syst]<<endl;
    //cout<<"csv\tjetPt\tjetAbsEta\tflavor"<<endl;
    //cout<<csv<<"\t"<<jetPt<<"\t"<<jetAbsEta<<"\t"<<flavor<<endl;
    
    if (abs(flavor) == 5 ){    //HF  
      float iCSVWgtHF = 1;
      if(isSystMatchFlavor(fabs(flavor), syst))
	iCSVWgtHF = reader->eval_auto_bounds(Systs[syst],BTagEntry::FLAV_B, jetAbsEta, jetPt, csv);  
      else
	iCSVWgtHF = reader->eval_auto_bounds(Systs[0],BTagEntry::FLAV_B, jetAbsEta, jetPt, csv);  
      // if(doubleUnc && syst != 0 ){
      // 	float centralSF = reader->eval_auto_bounds(Systs[0],BTagEntry::FLAV_B, jetAbsEta, jetPt, csv);
      // 	iCSVWgtHF = iCSVWgtHF-centralSF+iCSVWgtHF;
      // }
      if( iCSVWgtHF!=0 ) csvWgtHF *= iCSVWgtHF;
    } else if( abs(flavor) == 4 ){  //C
      float iCSVWgtC = 1;
      if(isSystMatchFlavor(fabs(flavor), syst))
	iCSVWgtC = reader->eval_auto_bounds(Systs[syst],BTagEntry::FLAV_C, jetAbsEta, jetPt, csv);
      else
	iCSVWgtC = reader->eval_auto_bounds(Systs[0],BTagEntry::FLAV_C, jetAbsEta, jetPt, csv);
      // if(doubleUnc && syst != 0 ){
      // 	float centralSF = reader->eval_auto_bounds(Systs[0],BTagEntry::FLAV_C, jetAbsEta, jetPt, csv);
      // 	iCSVWgtC = iCSVWgtC-centralSF+iCSVWgtC;
      // }
      if( iCSVWgtC!=0 ) csvWgtC *= iCSVWgtC;   
    } else { //LF
      float iCSVWgtLF = 1;
      if(isSystMatchFlavor(fabs(flavor), syst))
	iCSVWgtLF = reader->eval_auto_bounds(Systs[syst],BTagEntry::FLAV_UDSG, jetAbsEta, jetPt, csv);
      else
	iCSVWgtLF = reader->eval_auto_bounds(Systs[0],BTagEntry::FLAV_UDSG, jetAbsEta, jetPt, csv);
      // if(doubleUnc && syst != 0 ){
      // 	float centralSF = reader->eval_auto_bounds(Systs[0],BTagEntry::FLAV_UDSG, jetAbsEta, jetPt, csv);
      // 	iCSVWgtLF = iCSVWgtLF-centralSF+iCSVWgtLF;
      // }

      if( iCSVWgtLF!=0 ) csvWgtLF *= iCSVWgtLF;
    }
    //cout<<"bf\tcf\tlf"<<endl;
    //cout<<csvWgtHF <<"\t"<< csvWgtC <<"\t"<< csvWgtLF<<endl;
  }
  //if((csvWgtHF * csvWgtC * csvWgtLF)>5)throw 1000;

  return csvWgtHF * csvWgtC * csvWgtLF;
}


float BTagWeight::weight(pat::JetCollection jets/*, int ntag*/){
  if( WPT == -100 )
    return -100;
	//if (!filter(ntag)){
      		//   std::cout << "nThis event should not pass the selection, what is it doing here?" << std::endl;
        //	return 0;
	//}
	int njetTags = jets.size();
	int comb = 1 << njetTags;
	float pMC = 0;
	float pData = 0;
	for (int i = 0; i < comb; i++){
		float mc = 1.;
      		float data = 1.;
      		int ntagged = 0;
      		for (int j = 0; j < njetTags; j++){
	  		bool tagged = ((i >> j) & 0x1) == 1;
			float eff = this->MCTagEfficiency(jets[j],WPT);
			float sf = this->TagScaleFactor(jets[j]);
	  		if (tagged){
	      			ntagged++;
				mc *= eff;
				data *= (eff*sf);
				//mc *= jetTags[j].eff;
				//data *= jetTags[j].eff * jetTags[j].sf;
			} else {
			        mc*=(1-eff);
                		data*=(1-sf*eff);
				//mc *= (1. - jetTags[j].eff);
				//data *= (1. - jetTags[j].eff * jetTags[j].sf);
            		}
        	}

      		if (filter(ntagged)){
			//std::cout << mc << " " << data << endl;
			pMC += mc;
			pData += data;
	        }
	}
	if (pMC == 0) return 0;
	return pData / pMC;
}



float BTagWeight::weightExclusive(pat::JetCollection jets){
//This function takes into account cases where you have n b-tags and m vetoes, but they have different thresholds.
    if(WPL == -1){
	std::cout<<"FATAL ERROR: Provide the second btag WP!!!!"<<std::endl;
	return 0;
    } //https://twiki.cern.ch/twiki/pub/CMS/BTagSFMethods/latex3766350f938279e8ab2cee576fcba0d7.png
    std::vector<float> effL, effT, sfL, sfT;
    for (auto j : jets){
	effL.push_back(this->MCTagEfficiency(j,WPL));
	sfL.push_back(this->TagScaleFactor(j,(WPL != -1)));
	effT.push_back(this->MCTagEfficiency(j,WPT));
	sfT.push_back(this->TagScaleFactor(j));
    }
    int njetTags = jets.size();
    int comb = 1 << njetTags;
    float pMC = 0;
    float pData = 0;

    for (int i = 0; i < comb; i++){
      	int ntagged = 0;
        float wNonTaggedData = 1;
        float wNonTaggedMC = 1;
	std::vector<unsigned int> taggedIndecies;
      	for (int j = 0; j < njetTags; j++){
		bool tagged = ((i >> j) & 0x1) == 1;
	  	if (tagged){
	      		ntagged++;
			taggedIndecies.push_back(j);
		} else {
			wNonTaggedMC*=(1.-effL[j]);
                	wNonTaggedData*=(1.-sfL[j]*effL[j]);
            	}
       	}
	
	int combTagged = 1 << ntagged;
	for (int iTagged = 0; iTagged < combTagged; iTagged++){
		int nLoose = 0;
		float wTaggedData = 1;
                float wTaggedMC = 1;
	      	for (int jTagged = 0; jTagged < ntagged; jTagged++){
			bool tight = ((iTagged >> jTagged) & 0x1) == 1;	
			unsigned int realIndex = taggedIndecies[jTagged];

			if (tight){
				wTaggedMC*=(effT[realIndex]);
                		wTaggedData*=(sfT[realIndex]*effT[realIndex]);
			} else {
				nLoose++;
				wTaggedMC*=(effT[realIndex] - effL[realIndex]);
                		wTaggedData*=(sfT[realIndex]*effT[realIndex] - sfL[realIndex]*effL[realIndex]);
			}
		}
		if( filter( ntagged-nLoose , nLoose ) ){
			pMC += ( wNonTaggedMC*wTaggedMC );
			pData += (wNonTaggedData*wTaggedData) ;
		}
	}
    }
    if (pMC == 0) return 0;
    return pData / pMC;

}
//*************************************************************************

float BTagWeight::MCTagEfficiency(pat::Jet jet, int WP){
  int flavor = fabs(jet.hadronFlavour());
  if(flavor == 5){
    if(WP==0) return 0.38; //L
    if(WP==1) return 0.58; //M
    if(WP==2) return 0.755;//T
  }
  if(flavor == 4){
    if(WP==0) return 0.015; //L
    if(WP==1) return 0.08; //M
    if(WP==2) return 0.28;//T
  }
  if(flavor != 4){
    if(WP==0) return 0.0008; //L
    if(WP==1) return 0.007; //M
    if(WP==2) return 0.079;//T
 }
  return 1.0;
}

float BTagWeight::TagScaleFactor(pat::Jet jet, bool LooseWP ){

	float MinJetPt = 20.;
	float MaxBJetPt = 670., MaxLJetPt = 1000.;
        float JetPt = jet.pt(); bool DoubleUncertainty = false;
	int flavour = fabs(jet.hadronFlavour());
	if(flavour == 5) flavour = BTagEntry::FLAV_B;
	else if(flavour == 4) flavour = BTagEntry::FLAV_C;
	else flavour = BTagEntry::FLAV_UDSG;
	
	// if(flavour != BTagEntry::FLAV_UDSG){
	//    if (JetPt>MaxBJetPt)  { // use MaxLJetPt for  light jets
        // 	JetPt = MaxBJetPt; 
        // 	DoubleUncertainty = true;
      	//    }
	// } else {
	//    if (JetPt>MaxLJetPt)  { // use MaxLJetPt for  light jets
        //         JetPt = MaxBJetPt;
        //         DoubleUncertainty = true;
        //    }
	// }
	// if(JetPt<MinJetPt){
	//    JetPt = MinJetPt;
	//    DoubleUncertainty = true;
	// }

	float jet_scalefactor = 1;
	float jet_scalefactorCent = 1;

	if((BTagEntry::JetFlavor)flavour != BTagEntry::FLAV_UDSG){
	  jet_scalefactor = reader->eval_auto_bounds( Systs[syst], BTagEntry::FLAV_B, jet.eta(), JetPt); 
	  // if(DoubleUncertainty && syst != 0)
	  //   jet_scalefactorCent = reader->eval_auto_bounds( Systs[0], BTagEntry::FLAV_B, jet.eta(), JetPt);
	  if(LooseWP){
		  jet_scalefactor = readerExc->eval_auto_bounds( Systs[syst], BTagEntry::FLAV_B, jet.eta(), JetPt);
		  // if(DoubleUncertainty && syst != 0)
		  //   jet_scalefactorCent= readerExc->eval_auto_bounds( Systs[0], BTagEntry::FLAV_B, jet.eta(), JetPt);
	  }
	} else {
	  jet_scalefactor = reader->eval_auto_bounds(Systs[syst], BTagEntry::FLAV_UDSG, jet.eta(), JetPt);
	  // if(DoubleUncertainty && syst != 0)
	  //   jet_scalefactorCent = reader->eval_auto_bounds( Systs[0], BTagEntry::FLAV_UDSG, jet.eta(), JetPt);
	  if(LooseWP){
		  jet_scalefactor = readerExc->eval_auto_bounds(Systs[syst], BTagEntry::FLAV_UDSG, jet.eta(), JetPt);
		  // if(DoubleUncertainty && syst != 0)
		  //   jet_scalefactorCent = readerExc->eval_auto_bounds( Systs[0], BTagEntry::FLAV_UDSG, jet.eta(), JetPt);
	  }
	}


	// if(DoubleUncertainty && syst != 0){
	//   jet_scalefactor = jet_scalefactor - jet_scalefactorCent + jet_scalefactor; 
	// }
	return jet_scalefactor;
}

