#include <TFile.h>
#include "TMVA/Reader.h"
#include "TMVA/Factory.h"
#include "TMVA/Tools.h"
#include "CondFormats/EgammaObjects/interface/GBRForest.h"
#include "TMVA/MethodBDT.h"
#include "TMVA/IMethod.h"
#include <TString.h>
//#include "Cintex/Cintex.h"

class BDTConverter{
 public:
  BDTConverter(TString weightsFileName, TString outFileName);
  BDTConverter(const BDTConverter&);
  virtual ~BDTConverter();

  virtual void addVariable(TString);
  virtual void convert();

 private:
  TMVA::Reader* tmvaReader_;
  std::vector<float> variables_;
  std::vector<TString> variableNames_;
  TString weightsFileName_;
  TString outFileName_;
  GBRForest* outForest_;

};
