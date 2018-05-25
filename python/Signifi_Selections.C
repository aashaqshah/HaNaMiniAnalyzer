#include "TFile.h"
#include "TH1F.h"
#include "TTreeReader.h"
#include "TTreeReaderValue.h"


void Signifi_Selections(){

//TH1D *myHist = new TH1D("h1","Significance",200,0,200);

TFile *MyFile = new TFile("significance.root","READ");

if (MyFile->IsOpen()) printf ("Siginificance file Openend Successfully \n");

TCanvas *c1 = new TCanvas("c1", " ",100,128,820,380);
c1->Range(-99.10914,-0.003082714,566.8152,0.02051032);
c1->SetFillColor(0);
c1->SetBorderMode(0);
c1->SetBorderSize(2);
c1->SetLeftMargin(0.1488294);
c1->SetBottomMargin(0.130662);
c1->SetFrameBorderMode(0);
c1->SetFrameBorderMode(0);
c1->cd();
gStyle->SetOptStat(0000);
TH1D *myHist_25 = new TH1D("h1"," ",6,0,6);
TH1D *myHist_50 = new TH1D("h2"," ",6,0,6);

TTreeReader myReader("Significance", MyFile);

//char selection[] ={"PreselectionLL", "PreselectionMM", "PreselectionTT"};
//char selectionPost[] ={"LL", "MM", "TT"};
//TH1D *Mu1_s25_Pt_LL = (TH1D*)MyFile->Get(selection[i]"/Mu1/Significances/SoSqrtB/ROC_"selection[i]"_Mu1Pt_Signal25_SoSqrtB");

//TDirectory *dir1 = MyFile->GetDirectory("PreselectionLL/Mu1/Significances/SoSqrtB");
TH1D *Mu1_s25_Pt_LL = (TH1D*)MyFile->Get("PreselectionLL/Mu1/Significances/SoSqrtB/ROC_PreselectionLL_Mu1Pt_Signal25_SoSqrtB");
TH1D *Mu1_s50_Pt_LL = (TH1D*)MyFile->Get("PreselectionLL/Mu1/Significances/SoSqrtB/ROC_PreselectionLL_Mu1Pt_Signal50_SoSqrtB");
TH1D *Mu1_s25_Pt_ML = (TH1D*)MyFile->Get("PreselectionML/Mu1/Significances/SoSqrtB/ROC_PreselectionML_Mu1Pt_Signal25_SoSqrtB");
TH1D *Mu1_s50_Pt_ML = (TH1D*)MyFile->Get("PreselectionML/Mu1/Significances/SoSqrtB/ROC_PreselectionML_Mu1Pt_Signal50_SoSqrtB");
TH1D *Mu1_s25_Pt_TL = (TH1D*)MyFile->Get("PreselectionTL/Mu1/Significances/SoSqrtB/ROC_PreselectionTL_Mu1Pt_Signal25_SoSqrtB");
TH1D *Mu1_s50_Pt_TL = (TH1D*)MyFile->Get("PreselectionTL/Mu1/Significances/SoSqrtB/ROC_PreselectionTL_Mu1Pt_Signal50_SoSqrtB");
TH1D *Mu1_s25_Pt_MM = (TH1D*)MyFile->Get("PreselectionMM/Mu1/Significances/SoSqrtB/ROC_PreselectionMM_Mu1Pt_Signal25_SoSqrtB");
TH1D *Mu1_s50_Pt_MM = (TH1D*)MyFile->Get("PreselectionMM/Mu1/Significances/SoSqrtB/ROC_PreselectionMM_Mu1Pt_Signal50_SoSqrtB");
TH1D *Mu1_s25_Pt_TM = (TH1D*)MyFile->Get("PreselectionTM/Mu1/Significances/SoSqrtB/ROC_PreselectionTM_Mu1Pt_Signal25_SoSqrtB");
TH1D *Mu1_s50_Pt_TM = (TH1D*)MyFile->Get("PreselectionTM/Mu1/Significances/SoSqrtB/ROC_PreselectionTM_Mu1Pt_Signal50_SoSqrtB");
TH1D *Mu1_s25_Pt_TT = (TH1D*)MyFile->Get("PreselectionTT/Mu1/Significances/SoSqrtB/ROC_PreselectionTT_Mu1Pt_Signal25_SoSqrtB");
TH1D *Mu1_s50_Pt_TT = (TH1D*)MyFile->Get("PreselectionTT/Mu1/Significances/SoSqrtB/ROC_PreselectionTT_Mu1Pt_Signal50_SoSqrtB");
//TDirectory *dir2 = MyFile->GetDirectory("PreselectionLL/Mu2/Significances/SoSqrtB");
//dir->cd();
//gDirectory->pwd();

Mu1_s25_Pt_LL->GetYaxis()->SetTitle("Significance");
Mu1_s25_Pt_LL->GetYaxis()->CenterTitle();
Mu1_s25_Pt_LL->GetXaxis()->SetTitleOffset(1.3);
Mu1_s25_Pt_LL->GetYaxis()->SetDecimals();
//TH1D* h2 = (TH1D*)dir->Get("ROC_PreselectionLL_Mu1Pt_Signal25_SoSqrtB");
//TH1D* h2  = (TH1D*)dir->Get("ROC_PreselectionLL_Mu1Pt_Signal25_SoSqrtB");
//Long64_t nentries = h2->GetEntries();

//cout<<"Entries"<<nentries<<endl;
//TTreeReaderValue<Float_t> sig(myReader, h2);
//printf ("working properly again\n");
//while (myReader.Next()) {
//      cout<<"sig is "<<*sig<<endl;
//      myHist->Fill(*sig);
//                      }
//int Max_bin = Mu1_s25_Pt->GetMaximumBin();
//cout<<"Max bin "<<Max_bin<<endl;
//myHist->SetBinContent(1, Max_bin);
int bin_25_LL =  Mu1_s25_Pt_LL->GetXaxis()->FindBin(10);
int bin_50_LL =  Mu1_s50_Pt_LL->GetXaxis()->FindBin(10);
int bin_25_ML =  Mu1_s25_Pt_ML->GetXaxis()->FindBin(10);
int bin_50_ML =  Mu1_s50_Pt_ML->GetXaxis()->FindBin(10);
int bin_25_TL =  Mu1_s25_Pt_TL->GetXaxis()->FindBin(10);
int bin_50_TL =  Mu1_s50_Pt_TL->GetXaxis()->FindBin(10);
int bin_25_MM =  Mu1_s25_Pt_MM->GetXaxis()->FindBin(10);
int bin_50_MM =  Mu1_s50_Pt_MM->GetXaxis()->FindBin(10);
int bin_25_TM =  Mu1_s25_Pt_TM->GetXaxis()->FindBin(10);
int bin_50_TM =  Mu1_s50_Pt_TM->GetXaxis()->FindBin(10);
int bin_25_TT =  Mu1_s25_Pt_TT->GetXaxis()->FindBin(10);
int bin_50_TT =  Mu1_s50_Pt_TT->GetXaxis()->FindBin(10);
double bin_cont_25_LL =  Mu1_s25_Pt_LL->GetBinContent(bin_25_LL);
double bin_cont_50_LL =  Mu1_s50_Pt_LL->GetBinContent(bin_50_LL);
double bin_cont_25_ML =  Mu1_s25_Pt_ML->GetBinContent(bin_25_ML);
double bin_cont_50_ML =  Mu1_s50_Pt_ML->GetBinContent(bin_50_ML);
double bin_cont_25_TL =  Mu1_s25_Pt_TL->GetBinContent(bin_25_TL);
double bin_cont_50_TL =  Mu1_s50_Pt_TL->GetBinContent(bin_50_TL);
double bin_cont_25_MM =  Mu1_s25_Pt_MM->GetBinContent(bin_25_MM);
double bin_cont_50_MM =  Mu1_s50_Pt_MM->GetBinContent(bin_50_MM);
double bin_cont_25_TM =  Mu1_s25_Pt_TM->GetBinContent(bin_25_TM);
double bin_cont_50_TM =  Mu1_s50_Pt_TM->GetBinContent(bin_50_TM);
double bin_cont_25_TT =  Mu1_s25_Pt_TT->GetBinContent(bin_25_TT);
double bin_cont_50_TT =  Mu1_s50_Pt_TT->GetBinContent(bin_50_TT);
cout <<"Max Sig. for LL "<<bin_cont_25_LL<<endl;
cout <<"Max Sig. for ML "<<bin_cont_25_ML<<endl;
cout <<"Max Sig. for TL "<<bin_cont_25_TL<<endl;
cout <<"Max Sig. for MM "<<bin_cont_25_MM<<endl;
cout <<"Max Sig. for TM "<<bin_cont_25_TM<<endl;
cout <<"Max Sig. for TT "<<bin_cont_25_TT<<endl;
myHist_25->SetBinContent(1, bin_cont_25_LL);
myHist_50->SetBinContent(1, bin_cont_50_LL);
myHist_25->SetBinContent(2, bin_cont_25_ML);
myHist_50->SetBinContent(2, bin_cont_50_ML);
myHist_25->SetBinContent(3, bin_cont_25_TL);
myHist_50->SetBinContent(3, bin_cont_50_TL);
myHist_25->SetBinContent(4, bin_cont_25_MM);
myHist_50->SetBinContent(4, bin_cont_50_MM);
myHist_25->SetBinContent(5, bin_cont_25_TM);
myHist_50->SetBinContent(5, bin_cont_50_TM);
myHist_25->SetBinContent(6, bin_cont_25_TT);
myHist_50->SetBinContent(6, bin_cont_50_TT);

//myHist->GetXaxis()->SetLabelSize(0);
myHist_25->GetXaxis()->SetBinLabel(1, "LL");
myHist_25->GetXaxis()->SetBinLabel(2, "ML");
myHist_25->GetXaxis()->SetBinLabel(3, "TL");
myHist_25->GetXaxis()->SetBinLabel(4, "MM");
myHist_25->GetXaxis()->SetBinLabel(5, "TM");
myHist_25->GetXaxis()->SetBinLabel(6, "TT");
myHist_25->GetXaxis()->SetLabelSize(0.085);
myHist_25->GetYaxis()->SetLabelSize(0.050);
//myHist_25->GetXaxis()->SetTickLength(0);
myHist_25->GetYaxis()->SetNdivisions(508);
myHist_25->GetYaxis()->SetDecimals();
myHist_25->GetYaxis()->SetTitle("Significance");
myHist_25->GetYaxis()->SetTitleSize(0.065);
myHist_25->GetXaxis()->SetTitleSize(0.065);
myHist_25->GetYaxis()->SetTitleOffset(0.8);
myHist_25->GetXaxis()->SetTitleOffset(0.9);
myHist_25->GetYaxis()->CenterTitle();
myHist_25->GetXaxis()->CenterTitle();
myHist_25->SetLineColor(kRed);
myHist_50->SetLineColor(kBlue);
myHist_25->SetLineWidth(3);
myHist_50->SetLineWidth(3);
myHist_25->GetXaxis()->SetTitle("Selections");
myHist_25->GetXaxis()->SetNdivisions(500);
myHist_25->SetMinimum(0.003);
myHist_25->SetMaximum(0.025);
myHist_25->Draw();
myHist_50->Draw("SAME");
//Mu1_s25_Pt_LL->Draw();
//Mu1_s50_Pt->Draw("SAME");

//Mu1_s25_Pt_LL->GetXaxis()->SetRangeUser(0, 150);
//Mu1_s50_Pt->GetXaxis()->SetRangeUser(0, 150);
//gStyle->SetLegendBorderSize(0);
   TLegend *leg = new TLegend(0.7102689,0.7033898,0.8777506,0.8502825,NULL,"brNDC");
   //TLegend *leg = new TLegend(0.5936455,0.7160279,0.8913043,0.8641115,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("NULL","Signal Samples","h");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("NULL","Sample25","l");
   entry->SetLineColor(kRed);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(kRed);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("NULL","Sample50","l");
   entry->SetLineColor(kBlue);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(kBlue);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   leg->Draw();
   c1->Modified();
   c1->SaveAs("Significance_Selection.png");

//MyFile->Close();
//delete MyFile;
//leg->Draw(); 
//c1->Modified();
}
