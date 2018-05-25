#include "TFile.h"
#include "TH1F.h"
#include "TTreeReader.h"
#include "TTreeReaderValue.h"


void Signifi_plotter(){

//TH1D *myHist = new TH1D("h1","Significance",200,0,200);

TFile *MyFile = new TFile("significance.root","READ");

if (MyFile->IsOpen()) printf ("Siginificance file Openend Succesfully \n");

TCanvas *c1 = new TCanvas("c1", " ",100,128,600,600);
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
TH1D *myHist = new TH1D("h1","Significance",400,0,400);

TTreeReader myReader("Significance", MyFile);

//TDirectory *dir1 = MyFile->GetDirectory("PreselectionLL/Mu1/Significances/SoSqrtB");
TH1D *Mu1_s25_Pt = (TH1D*)MyFile->Get("PreselectionLL/Mu1/Significances/SoSqrtB/ROC_PreselectionLL_Mu1Pt_Signal25_SoSqrtB");
TH1D *Mu1_s50_Pt = (TH1D*)MyFile->Get("PreselectionLL/Mu1/Significances/SoSqrtB/ROC_PreselectionLL_Mu1Pt_Signal50_SoSqrtB");
//TDirectory *dir2 = MyFile->GetDirectory("PreselectionLL/Mu2/Significances/SoSqrtB");
//dir->cd();
//gDirectory->pwd();
Mu1_s25_Pt->SetLineColor(kRed);
Mu1_s50_Pt->SetLineColor(kBlue);

Mu1_s25_Pt->GetYaxis()->SetTitle("Significance");
Mu1_s25_Pt->GetYaxis()->CenterTitle();
Mu1_s25_Pt->GetXaxis()->SetTitleOffset(1.3);
Mu1_s25_Pt->GetYaxis()->SetDecimals();
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
Mu1_s25_Pt->Draw();
Mu1_s50_Pt->Draw("SAME");

Mu1_s25_Pt->GetXaxis()->SetRangeUser(0, 150);
Mu1_s50_Pt->GetXaxis()->SetRangeUser(0, 150);
gStyle->SetLegendBorderSize(0);
//TLegend *leg = new TLegend(0.1137124,0.5464135,0.4548495,0.8881857,NULL,"brNDC");
   TLegend *leg = new TLegend(0.5936455,0.7160279,0.8913043,0.8641115,NULL,"brNDC");
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
   c1->SaveAs("Significance_threshold.png");

//MyFile->Close();
//delete MyFile;
leg->Draw(); 
c1->Modified();
}
