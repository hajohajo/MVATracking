#BSUB -o /afs/cern.ch/work/j/jhavukai/private/GitMVATracking/CMSSW_9_2_0/src/MVATracking/NtupleMaker/test/logs/tuple_InitialStep_0.out
#BSUB -e /afs/cern.ch/work/j/jhavukai/private/GitMVATracking/CMSSW_9_2_0/src/MVATracking/NtupleMaker/test/logs/tuple_InitialStep_0.err
#BSUB -L /bin/bash
cd /afs/cern.ch/work/j/jhavukai/private/GitMVATracking/CMSSW_9_2_0/src
export SCRAM_ARCH=slc6_amd64_gcc530
eval `scramv1 runtime -sh`
cd /afs/cern.ch/work/j/jhavukai/private/GitMVATracking/CMSSW_9_2_0/src/MVATracking/NtupleMaker/test
cmsRun runTuple_InitialStep.py root://eoscms.cern.ch//eos/cms/store/relval/CMSSW_9_2_0/RelValTTbar_13/GEN-SIM-DIGI-RAW/PU25ns_91X_upgrade2017_realistic_v5_PU50-v1/10000/085D5AAF-9E40-E711-B12A-0025905A609E.root 0 InitialStep
