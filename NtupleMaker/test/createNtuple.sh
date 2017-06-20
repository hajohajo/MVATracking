#!/bin/bash

MAINDIR=$PWD
SCRIPTDIR=$PWD/scripts
OUTPUTDIR=$PWD/outputTuple
LOGDIR=$MAINDIR/logs
CMSDIR=$CMSSW_BASE/src

condorFile=$SCRIPTDIR/submitJobsNtuple.sh
ALGOS=(InitialStep)

mkdir -p $SCRIPTDIR

mkdir -p $OUTPUTDIR


if [ -e $condorFile ]
then
	rm -rf $condorFile
fi
touch $condorFile
chmod a+x $condorFile

filelist=eoslist.txt

#Create batch job submission scripts for each ntuple

i=0
while read line in filelist
	do
	for algo in "${ALGOS[@]}"
		do
			runScript=$SCRIPTDIR/runJobsNtuple_${algo}_${i}.sh
			if [ -e $runScript ]
				then
				rm -rf $runScript
			fi
			touch $runScript
			chmod a+x $runScript

			echo "#BSUB -o $LOGDIR/tuple_${algo}_${i}.out" >> $runScript
			echo "#BSUB -e $LOGDIR/tuple_${algo}_${i}.err" >> $runScript
			echo "#BSUB -L /bin/bash" >> $runScript
			echo "cd $CMSDIR" >> $runScript
			echo "export SCRAM_ARCH=$SCRAM_ARCH" >> $runScript
			echo 'eval `scramv1 runtime -sh`' >> $runScript
			echo "cd $MAINDIR" >> $runScript


			echo "cmsRun runTuple_${algo}.py $line $i $algo" >> $runScript    
			echo "bsub -R \"pool>30000\" -q 1nd < $runScript" >> $condorFile
		done
		let i++
done < $filelist

