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
                                         files=cms.vstring("MVASelectorInitialStep_Phase1.root"),
#,"MVASelectorLowPtQuadStep_Phase1.root","MVASelectorHighPtTripletStep_Phase1.root",
#							"MVASelectorLowPtTripletStep_Phase1.root","MVASelectorDetachedQuadStep_Phase1.root",
#							"MVASelectorDetachedTripletStep_Phase1.root","MVASelectorMixedTripletStep_Phase1.root",
#							"MVASelectorPixelLessStep_Phase1.root","MVASelectorTobTecStep_Phase1.root",
#							"MVASelectorJetCoreRegionalStep_Phase1.root"),
					 labels=cms.vstring("MVASelectorInitialStep_Phase1"),
#,"MVASelectorLowPtQuadStep_Phase1","MVASelectorHighPtTripletStep_Phase1",
#							"MVASelectorLowPtTripletStep_Phase1","MVASelectorDetachedQuadStep_Phase1","MVASelectorDetachedTripletStep_Phase1",
#							"MVASelectorMixedTripletStep_Phase1","MVASelectorPixelLessStep_Phase1","MVASelectorTobTecStep_Phase1",
#							"MVASelectorJetCoreRegionalStep_Phase1"),
)

process.load("CondCore.DBCommon.CondDBCommon_cfi")
# output database (in this case local sqlite file)
process.CondDBCommon.connect = 'sqlite_file:GBRWrapper_13TeV_922.db'

process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    process.CondDBCommon,
    timetype = cms.untracked.string('runnumber'),
    toPut = cms.VPSet(
      cms.PSet(
        record = cms.string('MVASelectorInitialStep_Phase1'),
        tag = cms.string('MVASelectorInitialStep_Phase1')
      ),
#      cms.PSet(
#        record = cms.string('MVASelectorLowPtQuadStep_Phase1'),
#        tag = cms.string('MVASelectorLowPtQuadStep_Phase1')
#      ),
#      cms.PSet(
#        record = cms.string('MVASelectorHighPtTripletStep_Phase1'),
#        tag = cms.string('MVASelectorHighPtTripletStep_Phase1')
#      ),
#      cms.PSet(
#        record = cms.string('MVASelectorLowPtTripletStep_Phase1'),
#        tag = cms.string('MVASelectorLowPtTripletStep_Phase1')
#      ),
#      cms.PSet(
#        record = cms.string('MVASelectorDetachedQuadStep_Phase1'),
#        tag = cms.string('MVASelectorDetachedQuadStep_Phase1')
#      ),
#      cms.PSet(
#        record = cms.string('MVASelectorDetachedTripletStep_Phase1'),
#        tag = cms.string('MVASelectorDetachedTripletStep_Phase1')
#      ),
#      cms.PSet(
#        record = cms.string('MVASelectorMixedTripletStep_Phase1'),
#        tag = cms.string('MVASelectorMixedTripletStep_Phase1')
#      ),
#      cms.PSet(
#        record = cms.string('MVASelectorPixelLessStep_Phase1'),
#        tag = cms.string('MVASelectorPixelLessStep_Phase1')
#      ),
#      cms.PSet(
#        record = cms.string('MVASelectorTobTecStep_Phase1'),
#        tag = cms.string('MVASelectorTobTecStep_Phase1')
#      ),
#      cms.PSet(
#        record = cms.string('MVASelectorJetCoreRegionalStep_Phase1'),
#        tag = cms.string('MVASelectorJetCoreRegionalStep_Phase1')
#      ),
  )
)

process.upload = cms.Path(process.gbrwrappermaker)
