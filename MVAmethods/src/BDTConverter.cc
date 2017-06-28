#include "MWalker/TrackAnalyzer/interface/BDTConverter.h"

BDTConverter::BDTConverter(TString weightsFileName, TString outFileName) 
{
  tmvaReader_ = new TMVA::Reader("!Color:Silent");
  weightsFileName_ = weightsFileName;
  outFileName_ = outFileName;
  outForest_ = NULL;
}
BDTConverter::BDTConverter(const BDTConverter& bc)
{
  tmvaReader_ = bc.tmvaReader_;
  weightsFileName_ = bc.weightsFileName_;
  outFileName_ = bc.outFileName_;
  if(bc.outForest_)outForest_ = bc.outForest_;
}
BDTConverter::~BDTConverter()
{
  delete tmvaReader_;
  if(outForest_)delete outForest_;
}

void BDTConverter::addVariable(TString varName)
{
  variables_.push_back(0.0);
  tmvaReader_->AddVariable(varName,&variables_[variables_.size()-1]);
}

void BDTConverter::convert()
{
  tmvaReader_->BookMVA("BDTG",weightsFileName_);
  TFile *ofile = new TFile(outFileName_,"RECREATE");
  //ROOT::Cintex::Cintex::Enable();
  TMVA::IMethod* meth=tmvaReader_->FindMVA("BDTG");
  TMVA::MethodBDT* bdt=dynamic_cast<TMVA::MethodBDT*>(meth);
  GBRForest *ogbreb= new GBRForest(bdt);
  //ogbreb->Write();
  ofile->WriteObject(ogbreb, "GBRForest");
  ofile->Close();
}
