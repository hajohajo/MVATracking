// system include files
#include <memory>
#include <vector>
#include <string>
#include <iostream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "TFile.h"
#include "CondFormats/EgammaObjects/interface/GBRForest.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
//#include "CondCore/DBOutputService/interface/PoolDBOutputService.h"
//#include "CondCore/DBCommon/interface/CoralServiceManager.h"

#include "CondCore/DBOutputService/interface/PoolDBOutputService.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "CondFormats/DataRecord/interface/GBRWrapperRcd.h"


//
// class declaration
//

class MVADBWriter : public edm::EDAnalyzer {
   public:
      explicit MVADBWriter(const edm::ParameterSet&);
      ~MVADBWriter();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  std::vector<std::string> files_;
  std::vector<std::string> labels_;
      // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
MVADBWriter::MVADBWriter(const edm::ParameterSet& iConfig)

{
  files_ = iConfig.getParameter<std::vector<std::string> >("files");
  labels_ = iConfig.getParameter<std::vector<std::string> >("labels");

   //now do what ever initialization is needed

}


MVADBWriter::~MVADBWriter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
MVADBWriter::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   if(files_.size() != labels_.size()){
     std::cerr<<"bad!!!!"<<std::endl;
     return;
   }

   edm::Service<cond::service::PoolDBOutputService> poolDbService;

   for(int i = 0; i < (int)files_.size(); i++){
     TFile infile(files_[i].c_str());
     GBRForest* gbr = (GBRForest*)infile.Get("GBRForest");
     if(poolDbService.isAvailable()){
       poolDbService->writeOne(gbr,poolDbService->beginOfTime(),labels_[i]);
     }
   }


}

// ------------ method called once each job just before starting event loop  ------------
void 
MVADBWriter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
MVADBWriter::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
MVADBWriter::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
MVADBWriter::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
MVADBWriter::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
MVADBWriter::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
MVADBWriter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(MVADBWriter);
