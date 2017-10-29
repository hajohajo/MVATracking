# MVATracking
Tools to retrain BDT classifiers used in Iterative Track Reconstruction using TMVA package

## Retraining BDTs in CMSSW Iterative Tracking

### Setting up environment and cloning repo
```
cmsrel CMSSW_9_3_0_pre3
cmsenv
git clone https://github.com/hajohajo/MVATracking.git
scram b -j 4
```
### Generating training Ntuples

```
cd MVATracking/NtupleMaker/test
```
In createNtuple.sh, change the ALGOS variable to the step you want to generate training tuples for i.e. InitialStep. If you are running InitialStep (the first iteration), create the scripts with
```
./createNtuple.sh
./scripts/submitJobsNtuple.sh
```

This creates batch jobs that will output files needed for retraining the MVA into the outputTuple folder. If you are running some other step, you need to upload the retrained weights done for the other steps by uncommenting the "process.PoolDBESSource" to include the already retrained steps. Also if the retrained steps need readjusting of the cuts, the new cuts should be included here to produce correct training samples for the iterations.

Once the training samples for your iterations have been completed (~1h), you can move to retraining the BDTs

### Retraining the BDTs
```
cd MVATracking/test
```
In TrainBDT.C one has to define the step name and if its prompt or not. Near the end of the file one can tune the parameters of the BDTs for the training. After setting these, run the training (takes anywhere from 30min to 3h depending on the step)
```
root -l TrainBDT.C
```
(In some cases this can cause segfault as destination folder wasn't created fast enough for the output file. In that case just try rerunning it, and everything should be fine.)

After the training, copy and rename the weights to the test folder:
```
cp dataset/MyClassification_BDTG.weights.xml MVASelectorInitialStep_Phase1.xml
```
(The name has to be of the form MVASelector{Step Name here}_Phase1.xml for the converter to find it)

Check that the converter has the step listed there in MVATracking/MVAmethods/bin/runConverter.C. In case this is not the initialStep, you'll need to add the step here. Recompile with scram after modifications. Then running in the test folder:
```
runConverter
```
This converts the .xml to a .root file that can be loaded into a database file with uploadToDB_cff.py. Again when doing something else than the initial step, uncomment suitable parts of the code. Run it with
```
cmsRun uploadToDB_cff.py
```
This creates a GBRWrapper_13TeV_930.db file that can contains the new weights for the iterations included in the uploadToDB_cff.py. It can now be copied back to MVATracking/NtupleMaker/test/ and start training the next iteration, or if all iterations are included, it can be deployed to production.
