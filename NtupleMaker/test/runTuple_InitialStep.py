# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2017 --conditions auto:phase1_2017_design -s RAW2DIGI,L1Reco,RECO --datatier GEN-SIM-RECO -n 10 --geometry Extended2017 --eventcontent FEVTDEBUGHLT --no_exec --filein file:step2.root --fileout file:step3.root
import FWCore.ParameterSet.Config as cms
import sys
from Configuration.StandardSequences.Eras import eras


process = cms.Process('RECO',eras.Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.Validation_cff')
process.load('DQMOffline.Configuration.DQMOfflineMC_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(sys.argv[2]),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(False),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(0)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(1048576),
    fileName = cms.untracked.string('file:TTBarWithRelVal.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.load("SimGeneral.TrackingAnalysis.trackingParticles_cfi")
#process.load("DQMServices.Components.EDMtoMEConverter_cff")

usePhase1 = True

##Uncomment suitable portions based on what weights are already retrained and saved to the .db file
#process.load("CondCore.CondDB.CondDB_cfi")
## input database (in this case local sqlite file)
#process.CondDB.connect = 'sqlite_file:./GBRWrapper_13TeV_102.db'
#process.PoolDBESSource = cms.ESSource("PoolDBESSource",
#    process.CondDB,
#    DumpStat=cms.untracked.bool(True),
#    toGet = cms.VPSet(
#      cms.PSet(
#        record = cms.string('GBRWrapperRcd'),
#        label = cms.untracked.string('MVASelectorInitialStep_Phase1_retrain'),
#        tag = cms.string('MVASelectorInitialStep_Phase1_retrain')
#      ),
#      cms.PSet(
#        record = cms.string('GBRWrapperRcd'),
#        label = cms.untracked.string('MVASelectorLowPtQuadStep_Phase1'),
#        tag = cms.string('MVASelectorLowPtQuadStep_Phase1')
#      ),
#      cms.PSet(
#        record = cms.string('GBRWrapperRcd'),
#        label = cms.untracked.string('MVASelectorHighPtTripletStep_Phase1'),
#        tag = cms.string('MVASelectorHighPtTripletStep_Phase1')
#      ),
#      cms.PSet(
#        record = cms.string('GBRWrapperRcd'),
#        label = cms.untracked.string('MVASelectorLowPtTripletStep_Phase1'),
#        tag = cms.string('MVASelectorLowPtTripletStep_Phase1')
#      ),
#      cms.PSet(
#        record = cms.string('GBRWrapperRcd'),
#        label = cms.untracked.string('MVASelectorDetachedQuadStep_Phase1'),
#        tag = cms.string('MVASelectorDetachedQuadStep_Phase1')
#      ),
#      cms.PSet(
#        record = cms.string('GBRWrapperRcd'),
#        label = cms.untracked.string('MVASelectorDetachedTripletStep_Phase1'),
#        tag = cms.string('MVASelectorDetachedTripletStep_Phase1')
#      ),
#      cms.PSet(
#        record = cms.string('GBRWrapperRcd'),
#        label = cms.untracked.string('MVASelectorMixedTripletStep_Phase1'),
#        tag = cms.string('MVASelectorMixedTripletStep_Phase1')
#      ),
#      cms.PSet(
#        record = cms.string('GBRWrapperRcd'),
#        label = cms.untracked.string('MVASelectorPixelLessStep_Phase1'),
#        tag = cms.string('MVASelectorPixelLessStep_Phase1')
#      ),
#      cms.PSet(
#        record = cms.string('GBRWrapperRcd'),
#        label = cms.untracked.string('MVASelectorTobTecStep_Phase1'),
#        tag = cms.string('MVASelectorTobTecStep_Phase1')
#      ),
#      cms.PSet(
#        record = cms.string('GBRWrapperRcd'),
#        label = cms.untracked.string('MVASelectorJetCoreRegionalStep_Phase1'),
#        tag = cms.string('MVASelectorJetCoreRegionalStep_Phase1')
#      ),
    )
)

#Replace the weights of initialStep BDT classifier by uncommenting
#process.initialStep.mva.GBRForestLabel = 'MVASelectorInitialStep_Phase1_retrain'


process.load("SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi")

# Additional output definition
process.myAnalyzer = cms.EDAnalyzer("NtupleMaker",
				    isPhase1 = cms.bool(usePhase1),
				    source=cms.string("initialStepTracks"),
                                    simSource=cms.InputTag("mix","MergedTrackTruth"),
                                    beamspot = cms.InputTag("offlineBeamSpot"),
                                    vertices = cms.InputTag("firstStepPrimaryVertices"),
                                    outfile=cms.string('./outputTuple/output_'+sys.argv[4]+"_"+sys.argv[3]+'.root'),
                                    associator=cms.string("quickTrackAssociatorByHits"),
                                    )


# Other statements
process.mix.playback = True
process.mix.digitizers = cms.PSet()
for a in process.aliases: delattr(process, a)
process.RandomNumberGeneratorService.restoreStateLabel=cms.untracked.string("randomEngineStateProducer")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2018_realistic', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
#process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction*process.tpClusterProducer*process.quickTrackAssociatorByHits*process.myAnalyzer)
#process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
#process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step)
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step)

print sys.argv

# End of customisation functions

