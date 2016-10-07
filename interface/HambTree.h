//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Fri Oct  7 11:10:17 2016 by ROOT version 6.06/01
// from TTree Events/Events
// found on file: eos/cms/store/user/ajafari/Oct5_8020_v2/out_DYJets_14C2C95A-F25C-E611-86B7-0025905C42F2_5.root
//////////////////////////////////////////////////////////

#ifndef HambTree_h
#define HambTree_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
using namespace std;
// Header file for the classes stored in the TTree if any.
#include "vector"
#include "iostream"

class HambTree {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   ULong64_t       EventNumber;
   UInt_t          RunNumber;
   UChar_t         nVertices;
   Float_t         Weight;
   Float_t         puWeight;
   Float_t         bWs_W1L;
   Float_t         bWs_W1M;
   Float_t         bWs_W1T;
   Float_t         bWs_W1L1M;
   Float_t         bWs_W1L1T;
   Float_t         bWs_W1M1T;
   Float_t         bWs_W2L;
   Float_t         bWs_W2M;
   Float_t         bWs_W2T;
   Float_t         hltWeights_mu17mu8;
   Float_t         hltWeights_mu17mu8dz;
   Float_t         met;
   Float_t         metPhi;
   Float_t         metSig;
   Bool_t          passHLT_Mu17Mu8;
   Bool_t          passHLT_Mu17Mu8_DZ;
   Float_t         hltWeight_Mu17Mu8;
   Float_t         hltWeight_Mu17Mu8_DZ;
   vector<float>   *jetsPt;
   vector<float>   *jetsEta;
   vector<float>   *jetsPhi;
   vector<float>   *jetsBtag;
   vector<float>   *jetsFlavour;
   Float_t         nNonTagged;
   Float_t         nLooseNotMed;
   Float_t         nMedNotTight;
   Float_t         nTight;
   vector<float>   *muPt;
   vector<float>   *muEta;
   vector<float>   *muPhi;
   vector<float>   *muIso;
   vector<bool>    *muId;
   vector<bool>    *muCharge;
   vector<bool>    *muHLT;
   Float_t         aMu_pt;
   Float_t         aMu_eta;
   Float_t         aMu_phi;
   Float_t         aMu_mass;
   Float_t         aMu_b1;
   Float_t         aMu_b2;
   Float_t         aMu_w;
   Float_t         aBjetPtOrdered_pt;
   Float_t         aBjetPtOrdered_eta;
   Float_t         aBjetPtOrdered_phi;
   Float_t         aBjetPtOrdered_mass;
   Float_t         aBjetPtOrdered_b1;
   Float_t         aBjetPtOrdered_b2;
   Float_t         aBjetPtOrdered_w;
   Float_t         aBjetBtagOrdered_pt;
   Float_t         aBjetBtagOrdered_eta;
   Float_t         aBjetBtagOrdered_phi;
   Float_t         aBjetBtagOrdered_mass;
   Float_t         aBjetBtagOrdered_b1;
   Float_t         aBjetBtagOrdered_b2;
   Float_t         aBjetBtagOrdered_w;
   Float_t         higgsjetPtOrdered_pt;
   Float_t         higgsjetPtOrdered_eta;
   Float_t         higgsjetPtOrdered_phi;
   Float_t         higgsjetPtOrdered_mass;
   Float_t         higgsjetPtOrdered_b1;
   Float_t         higgsjetPtOrdered_b2;
   Float_t         higgsjetPtOrdered_w;
   Float_t         higgsjetBtagOrdered_pt;
   Float_t         higgsjetBtagOrdered_eta;
   Float_t         higgsjetBtagOrdered_phi;
   Float_t         higgsjetBtagOrdered_mass;
   Float_t         higgsjetBtagOrdered_b1;
   Float_t         higgsjetBtagOrdered_b2;
   Float_t         higgsjetBtagOrdered_w;

   // List of branches
   TBranch        *b_EventNumber;   //!
   TBranch        *b_RunNumber;   //!
   TBranch        *b_nVertices;   //!
   TBranch        *b_W0;   //!
   TBranch        *b_puWeight;   //!
   TBranch        *b_bWs;   //!
   TBranch        *b_hltWeights;   //!
   TBranch        *b_met;   //!
   TBranch        *b_metPhi;   //!
   TBranch        *b_metSig;   //!
   TBranch        *b_passHLT_Mu17Mu8;   //!
   TBranch        *b_passHLT_Mu17Mu8_DZ;   //!
   TBranch        *b_hltWeight_Mu17Mu8;   //!
   TBranch        *b_hltWeight_Mu17Mu8_DZ;   //!
   TBranch        *b_jetsPt;   //!
   TBranch        *b_jetsEta;   //!
   TBranch        *b_jetsPhi;   //!
   TBranch        *b_jetsBtag;   //!
   TBranch        *b_jetsFlavour;   //!
   TBranch        *b_nNonTagged;   //!
   TBranch        *b_nLooseNotMed;   //!
   TBranch        *b_nMedNotTight;   //!
   TBranch        *b_nTight;   //!
   TBranch        *b_muPt;   //!
   TBranch        *b_muEta;   //!
   TBranch        *b_muPhi;   //!
   TBranch        *b_muIso;   //!
   TBranch        *b_muId;   //!
   TBranch        *b_muCharge;   //!
   TBranch        *b_muHLT;   //!
   TBranch        *b_aMu;   //!
   TBranch        *b_aBjetPtOrdered;   //!
   TBranch        *b_aBjetBtagOrdered;   //!
   TBranch        *b_higgsjetPtOrdered;   //!
   TBranch        *b_higgsjetBtagOrdered;   //!

   HambTree(TTree *tree=0, TString dirName = "/Hamb/Trees", TString treeName = "Events", TFile * f = 0);
   virtual ~HambTree();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef HambTree_cxx
HambTree::HambTree(TTree *tree, TString dirName, TString treeName, TFile * f) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {  
	if(f == 0){
		cout<<"FATAL ERROR! Provide a valid tree or input file ... "<<endl;
		return;
	}
   	TDirectory * dir = (TDirectory*)f->Get(dirName);
      	dir->GetObject(treeName,tree);

   }
   Init(tree);
}

HambTree::~HambTree()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t HambTree::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t HambTree::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void HambTree::Init(TTree *tree)
{

   // Set object pointer
   jetsPt = 0;
   jetsEta = 0;
   jetsPhi = 0;
   jetsBtag = 0;
   jetsFlavour = 0;
   muPt = 0;
   muEta = 0;
   muPhi = 0;
   muIso = 0;
   muId = 0;
   muCharge = 0;
   muHLT = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("EventNumber", &EventNumber, &b_EventNumber);
   fChain->SetBranchAddress("RunNumber", &RunNumber, &b_RunNumber);
   fChain->SetBranchAddress("nVertices", &nVertices, &b_nVertices);
   fChain->SetBranchAddress("Weight", &Weight, &b_W0);
   fChain->SetBranchAddress("puWeight", &puWeight, &b_puWeight);
   fChain->SetBranchAddress("bWs", &bWs_W1L, &b_bWs);
   fChain->SetBranchAddress("hltWeights", &hltWeights_mu17mu8, &b_hltWeights);
   fChain->SetBranchAddress("met", &met, &b_met);
   fChain->SetBranchAddress("metPhi", &metPhi, &b_metPhi);
   fChain->SetBranchAddress("metSig", &metSig, &b_metSig);
   fChain->SetBranchAddress("passHLT_Mu17Mu8", &passHLT_Mu17Mu8, &b_passHLT_Mu17Mu8);
   fChain->SetBranchAddress("passHLT_Mu17Mu8_DZ", &passHLT_Mu17Mu8_DZ, &b_passHLT_Mu17Mu8_DZ);
   fChain->SetBranchAddress("hltWeight_Mu17Mu8", &hltWeight_Mu17Mu8, &b_hltWeight_Mu17Mu8);
   fChain->SetBranchAddress("hltWeight_Mu17Mu8_DZ", &hltWeight_Mu17Mu8_DZ, &b_hltWeight_Mu17Mu8_DZ);
   fChain->SetBranchAddress("jetsPt", &jetsPt, &b_jetsPt);
   fChain->SetBranchAddress("jetsEta", &jetsEta, &b_jetsEta);
   fChain->SetBranchAddress("jetsPhi", &jetsPhi, &b_jetsPhi);
   fChain->SetBranchAddress("jetsBtag", &jetsBtag, &b_jetsBtag);
   fChain->SetBranchAddress("jetsFlavour", &jetsFlavour, &b_jetsFlavour);
   fChain->SetBranchAddress("nNonTagged", &nNonTagged, &b_nNonTagged);
   fChain->SetBranchAddress("nLooseNotMed", &nLooseNotMed, &b_nLooseNotMed);
   fChain->SetBranchAddress("nMedNotTight", &nMedNotTight, &b_nMedNotTight);
   fChain->SetBranchAddress("nTight", &nTight, &b_nTight);
   fChain->SetBranchAddress("muPt", &muPt, &b_muPt);
   fChain->SetBranchAddress("muEta", &muEta, &b_muEta);
   fChain->SetBranchAddress("muPhi", &muPhi, &b_muPhi);
   fChain->SetBranchAddress("muIso", &muIso, &b_muIso);
   fChain->SetBranchAddress("muId", &muId, &b_muId);
   fChain->SetBranchAddress("muCharge", &muCharge, &b_muCharge);
   fChain->SetBranchAddress("muHLT", &muHLT, &b_muHLT);
   fChain->SetBranchAddress("aMu", &aMu_pt, &b_aMu);
   fChain->SetBranchAddress("aBjetPtOrdered", &aBjetPtOrdered_pt, &b_aBjetPtOrdered);
   fChain->SetBranchAddress("aBjetBtagOrdered", &aBjetBtagOrdered_pt, &b_aBjetBtagOrdered);
   fChain->SetBranchAddress("higgsjetPtOrdered", &higgsjetPtOrdered_pt, &b_higgsjetPtOrdered);
   fChain->SetBranchAddress("higgsjetBtagOrdered", &higgsjetBtagOrdered_pt, &b_higgsjetBtagOrdered);
   Notify();
}

Bool_t HambTree::Notify()
{

   return kTRUE;
}

void HambTree::Show(Long64_t entry)
{
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t HambTree::Cut(Long64_t entry)
{
   return 1;
}

void HambTree::Loop()
{

   if (fChain == 0) return;

   Long64_t nentries = fChain->GetEntriesFast();

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;
   }
}

#endif // #ifdef HambTree_cxx
