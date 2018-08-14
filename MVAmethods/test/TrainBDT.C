#include <cstdlib>
#include <iostream>
#include <map>
#include <string>

#include "TChain.h"
#include "TFile.h"
#include "TTree.h"
#include "TString.h"
#include "TObjString.h"
#include "TSystem.h"
#include "TROOT.h"

#if not defined(__CINT__) || defined(__MAKECINT__)
#include "TMVA/Tools.h"
#include "TMVA/Factory.h"
#endif

using namespace TMVA;

std::string step = "InitialStep";
bool isPrompt_ = true;

void TrainBDT(const char* outfileName="dataset/BDT_train_output.root")
{
	TMVA::Tools::Instance();

	//Folder where Ntuples for training are
	std::string ntuplePath="../../NtupleMaker/test/outputTuple/";
//	std::string step = "InitialStep";

	//Make sure not to cause biasing by using same
	//files in training and test

	//How many files to read for training
	Int_t const Nmax=2;
	//How many files to read for testing
	Int_t const Ntest=1;

	Int_t const Ntotal=Nmax+Ntest;


	std::cout << "==> Start TMVARegression" << std::endl;


	//Loading the root files. Could do with some cleaning up.
	//Also a hack to skip possible zombie files

	TFile* files[Ntotal];
	TTree* trees[Ntotal];
	TFile* inFile;
	Int_t point = 0;
	for(int i = 0; i<Ntotal; i++)
	{
		if(point>60)
		{
			break;
		}
		TString fileName=Form("%soutput_%s_%d.root",ntuplePath.c_str(),step.c_str(),point);
		files[i] = new TFile(fileName);
		if(files[i]->IsZombie())
		{
			std::cout<<"Zombie!"<<std::endl;
			point++;
			i--;
			continue;
		}
		trees[i] = (TTree*)files[i]->Get("NtupleTree");
		point++;
		
	}

	TFile* outputFile = TFile::Open( outfileName, "RECREATE");
	TMVA::Factory *factory = new TMVA::Factory("MyClassification", outputFile,"!V:!Silent:Color:DrawProgressBar:AnalysisType=Classification");
	TMVA::DataLoader *dataloader;
	dataloader=new TMVA::DataLoader("dataset");


	   //USED VARIABLES
	dataloader->AddVariable("pt",'F');
	dataloader->AddVariable("lostmidfrac",'F');
	dataloader->AddVariable("minlost",'F');
	dataloader->AddVariable("nhits",'F');
	dataloader->AddVariable("relpterr",'F');
	dataloader->AddVariable("eta",'F');
	dataloader->AddVariable("chi2n_no1Dmod",'F');
	dataloader->AddVariable("chi2n",'F');
	dataloader->AddVariable("nlayerslost",'F');
	dataloader->AddVariable("nlayers3D",'F');
	dataloader->AddVariable("nlayers",'F');
	dataloader->AddVariable("ndof",'F');

	//For prompt steps
	if(isPrompt_){
		dataloader->AddVariable("absd0PV",'F');
		dataloader->AddVariable("absdzPV",'F');
		dataloader->AddVariable("absdz",'F');
		dataloader->AddVariable("absd0",'F');
	}

	TCut signal = "fake == 0";
	TCut background = "fake == 1";
	TCut mycut ="";  //Optional precut to training data

	for(int i =0;i<Nmax;i++){
		dataloader->AddTree(trees[i],"Signal",1.0,signal,TMVA::Types::kTraining);
		dataloader->AddTree(trees[i],"Background",1.0,background,TMVA::Types::kTraining);
	}
	for(int i =Nmax;i<Ntotal; i++){
                dataloader->AddTree(trees[i],"Signal",1.0,signal,TMVA::Types::kTesting);
                dataloader->AddTree(trees[i],"Background",1.0,background,TMVA::Types::kTesting);
	}

	//Setting 1.0/pt weight helps in the lowPtTripletStep
//	dataloader->SetWeightExpression( "1.0/pt");


	dataloader->PrepareTrainingAndTestTree(mycut,"SplitMode=Random:NormMode=NumEvents:!V");

	//Defining the method and its hyperparameters for the training
	factory->BookMethod(dataloader, TMVA::Types::kBDT, "BDTG",
                           "!H:!V:VarTransform=I:NTrees=2000::BoostType=Grad:Shrinkage=0.2:NegWeightTreatment=Pray:UseBaggedBoost:GradBaggingFraction=0.5:nCuts=60:MaxDepth=10" );

	factory->TrainAllMethods();
	factory->TestAllMethods();
	factory->EvaluateAllMethods();

	outputFile->Close();

	std::cout << "==> Wrote root file: " << outputFile->GetName() << std::endl;

	delete factory;
}
