import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

#process.source = cms.Source("PoolSource",
    ## replace 'myfile.root' with the source file you want to use
    #fileNames = cms.untracked.vstring(
        #'file:myfile.root'
    #)
#)

#    "InitialStep"
#    "LowPtQuadStep"
#    "HighPtTripletStep"
#    "LowPtTripletStep"
#    "DetachedQuadStep"
#    "DetachedTripletStep"
#    "MixedTripletStep"
#    "PixelLessStep"
#    "TobTecStep"
#    "JetCoreRegionalStep"


process.source = cms.Source("EmptySource",
)
        

process.gbrwrappermaker = cms.EDAnalyzer('MVADBWriter',
                                         files=cms.vstring("MVASelectorInitialStep_Phase1.root",
#								"MVASelectorLowPtQuadStep_Phase1.root",
#								"MVASelectorHighPtTripletStep_Phase1.root",
#								"MVASelectorLowPtTripletStep_Phase1.root",
#								"MVASelectorDetachedQuadStep_Phase1.root",
#								"MVASelectorDetachedTripletStep_Phase1.root",
#								"MVASelectorPixelPairStep_Phase1.root",
#								"MVASelectorMixedTripletStep_Phase1.root",
#								"MVASelectorPixelLessStep_Phase1.root",
#								"MVASelectorTobTecStep_Phase1.root",
#								"MVASelectorJetCoreRegionalStep_Phase1.root"),
					 labels=cms.vstring("MVASelectorInitialStep_Phase1_retrain", 
#								"MVASelectorLowPtQuadStep_Phase1_retrain",
#								"MVASelectorHighPtTripletStep_Phase1_retrain",
#								"MVASelectorLowPtTripletStep_Phase1_retrain",
#								"MVASelectorDetachedQuadStep_Phase1_retrain",
#								"MVASelectorDetachedTripletStep_Phase1_retrain",
#								"MVASelectorPixelPairStep_Phase1_retrain",
#								"MVASelectorMixedTripletStep_Phase1_retrain",
#								"MVASelectorPixelLessStep_Phase1_retrain",
#								"MVASelectorTobTecStep_Phase1_retrain",
#								"MVASelectorJetCoreRegionalStep_Phase1_retrain"),
)

process.load("CondCore.DBCommon.CondDBCommon_cfi")
# output database (in this case local sqlite file)
process.CondDBCommon.connect = 'sqlite_file:GBRWrapper_13TeV_930.db'

process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    process.CondDBCommon,
    timetype = cms.untracked.string('runnumber'),
    toPut = cms.VPSet(
      cms.PSet(
        record = cms.string('MVASelectorInitialStep_Phase1_retrain'),
        tag = cms.string('MVASelectorInitialStep_Phase1_retrain')
      ),
#      cms.PSet(
#        record = cms.string('MVASelectorLowPtQuadStep_Phase1_retrain'),
#        tag = cms.string('MVASelectorLowPtQuadStep_Phase1_retrain')
#      ),
#      cms.PSet(
#        record = cms.string('MVASelectorHighPtTripletStep_Phase1_retrain'),
#        tag = cms.string('MVASelectorHighPtTripletStep_Phase1_retrain')
#      ),
#      cms.PSet(
#        record = cms.string('MVASelectorLowPtTripletStep_Phase1_retrain'),
#        tag = cms.string('MVASelectorLowPtTripletStep_Phase1_retrain')
#      ),
#      cms.PSet(
#        record = cms.string('MVASelectorDetachedQuadStep_Phase1_retrain'),
#        tag = cms.string('MVASelectorDetachedQuadStep_Phase1_retrain')
#      ),
#      cms.PSet(
#        record = cms.string('MVASelectorDetachedTripletStep_Phase1_retrain'),
#        tag = cms.string('MVASelectorDetachedTripletStep_Phase1_retrain')
#      ),
#      cms.PSet(
#        record = cms.string('MVASelectorPixelPairStep_Phase1_retrain'),
#        tag = cms.string('MVASelectorPixelPairStep_Phase1_retrain')
#      ),
#      cms.PSet(
#        record = cms.string('MVASelectorMixedTripletStep_Phase1_retrain'),
#        tag = cms.string('MVASelectorMixedTripletStep_Phase1_retrain')
#      ),
#      cms.PSet(
#        record = cms.string('MVASelectorPixelLessStep_Phase1_retrain'),
#        tag = cms.string('MVASelectorPixelLessStep_Phase1_retrain')
#      ),
#      cms.PSet(
#        record = cms.string('MVASelectorTobTecStep_Phase1_retrain'),
#        tag = cms.string('MVASelectorTobTecStep_Phase1_retrain')
#      ),
#      cms.PSet(
#        record = cms.string('MVASelectorJetCoreRegionalStep_Phase1_retrain'),
#        tag = cms.string('MVASelectorJetCoreRegionalStep_Phase1_retrain')
#      ),
    )
)

process.upload = cms.Path(process.gbrwrappermaker)
