#include "MVATracking/MVAmethods/interface/BDTConverter.h"
#include <TString.h>
int main(int argc, char** argv)
{
/*
    Names of the iterations

    PROMPTS
    "InitialStep"
    "LowPtQuadStep"
    "HighPtTripletStep"
    "LowPtTripletStep"
    NON PROMPTS
    "DetachedQuadStep"
    "DetachedTripletStep"
    "MixedTripletStep"
    "PixelLessStep"
    "TobTecStep"
    "JetCoreRegionalStep"
*/

  std::string name = "InitialStep";

  //Select if step is prompt or not
  bool isPrompt = true;

  std::cout<<argc<<std::endl;
  if(argc == 1){

    //PROMPT ITERATIONS
    if(isPrompt){
      TString wfname = TString::Format("./MVASelector%s_Phase1.xml",name.c_str());
      TString rfname = TString::Format("./MVASelector%s_Phase1.root",name.c_str());
      BDTConverter* converter = new BDTConverter(wfname,rfname);   
      
      converter->addVariable("pt");
      converter->addVariable("lostmidfrac");
      converter->addVariable("minlost");
      converter->addVariable("nhits");
      converter->addVariable("relpterr");
      converter->addVariable("eta");
      converter->addVariable("chi2n_no1Dmod");
      converter->addVariable("chi2n");
      converter->addVariable("nlayerslost");
      converter->addVariable("nlayers3D");
      converter->addVariable("nlayers");
      converter->addVariable("ndof");
      converter->addVariable("absd0PV");
      converter->addVariable("absdzPV");
      converter->addVariable("absdz");
      converter->addVariable("absd0");
      
      converter->convert();
    }

    //NON-PROMT ITERATIONS
    else{
      TString wfname = TString::Format("./MVASelector%s_Phase1.xml",name.c_str());
      TString rfname = TString::Format("./MVASelector%s_Phase1.root",name.c_str());
      BDTConverter* converter = new BDTConverter(wfname,rfname);   
      
      converter->addVariable("pt");
      converter->addVariable("lostmidfrac");
      converter->addVariable("minlost");
      converter->addVariable("nhits");
      converter->addVariable("relpterr");
      converter->addVariable("eta");
      converter->addVariable("chi2n_no1Dmod");
      converter->addVariable("chi2n");
      converter->addVariable("nlayerslost");
      converter->addVariable("nlayers3D");
      converter->addVariable("nlayers");
      converter->addVariable("ndof");
      
      converter->convert();
    }


  }else if(argc == 3){
    TString wfname = TString::Format("%s",argv[1]);
    TString rfname = wfname;
    rfname.ReplaceAll(".xml",".root");
    BDTConverter* converter = new BDTConverter(wfname,rfname);

    converter->addVariable("pt");
    converter->addVariable("lostmidfrac");
    converter->addVariable("minlost");
    converter->addVariable("nhits");
    converter->addVariable("relpterr");
    converter->addVariable("eta");
    converter->addVariable("chi2n_no1Dmod");
    converter->addVariable("chi2n");
    converter->addVariable("nlayerslost");
    converter->addVariable("nlayers3D");
    converter->addVariable("nlayers");
    converter->addVariable("ndof");
    TString mvatype = TString::Format("%s",argv[2]);
    if(mvatype == "Prompt"){
      converter->addVariable("absd0PV");
      converter->addVariable("absdzPV");
      converter->addVariable("absdz");
      converter->addVariable("absd0");
    }
    converter->convert();
  }
}
