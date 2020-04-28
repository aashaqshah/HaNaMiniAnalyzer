#!/bin/bash
export X509_USER_PROXY=$2
source /cvmfs/cms.cern.ch/cmsset_default.sh
voms-proxy-info
export SCRAM_ARCH=$3
echo "Given architechture is: ==========================="
echo $SCRAM_ARCH
scramv1 project CMSSW $4
cd $4/src/
export SCRAM_ARCH=$3
echo "Given architechture within CMS directory is: ==========================="
echo $SCRAM_ARCH
eval `scramv1 runtime -sh`
scram b
mkdir Haamm/
cd Haamm
echo "Given architechture before cloning git: ==========================="
echo $SCRAM_ARCH
git clone -b $5 https://github.com/aashaqshah/HaNaMiniAnalyzer/
cd HaNaMiniAnalyzer/
git checkout $5
scram b
cd test
if [ ! -z "$LSB_JOBINDEX" ];
then
    echo $LSB_JOBINDEX
    export FILEID=`expr $LSB_JOBINDEX - 1`
    echo $FILEID
else
    if [ ! -z "$CONDORJOBID" ];
    then
	export FILEID=$CONDORJOBID
	echo $FILEID

        if [[ "$1" == "SUBMIT" ]] ; then
         echo $FILEID
        else
         FailedJobIDs=$1
         fileNumber=$FILEID
         counter=-1;
         file_zero=0;
         Ids=$(echo $FailedJobIDs | tr "," "\n")
         for Id in $Ids
          do
           counter=$[$counter +1]
           if [ "$fileNumber" -eq "$counter" ];then
              echo "fileNumber = $fileNumber";
              echo "counter = $counter";
              echo "Id = $Id";
              FILEID=$[$Id -1];
              echo "Failed File Id is $FILEID"
           fi
          done
        fi
     fi
fi

echo "Running the ntupler"

echo "cmsRun Hamb_cfg.py sample=$6 job=$FILEID output=$7 maxEvents=-1 nFilesPerJob=$9"

cmsRun Hamb_cfg.py sample=$6 job=$FILEID output=$7 maxEvents=-1 nFilesPerJob=$9

echo "I am not sure if the code ran succesfully"

outfilename=`ls $7*$6*.root`
outfilenames=`ls *$7*$6*.root`

ls -l $outfilenames


#if [[ $7 == eos* ]] ;
if [[ $8 == eos* ]] ;
then
    #first try to copy to /eos
    if [[ -d "/eos" && -x "/eos" ]]; then
	mkdir -p /$8

	if [ -f  /$8/$outfilename ]; then
	    echo "the file exists, is being renamed"
	    rm -f /$8/${outfilename}_
		rm -f /$8/$outfilename
	fi

	COUNTER2=0
	while [ ! -f  /$8/$outfilename ]
	do
	    if [ $COUNTER2 -gt 20 ]; then
		break
	    fi
	    cp $outfilenames /$8/
	    let COUNTER2=COUNTER2+1
	    echo ${COUNTER2}th Try
	    sleep 10
	done

	if [ -f  /$8/$outfilename ]; then
	    echo "The file was copied succesfully via the /eos mounting point on machine"
	    rm $outfilenames
	    exit 0
	fi
    fi

    eos mkdir -p /$8
    if [ $? -eq 0 ] || [ $? -eq 17 ] ;
    then
	for file in *$7*$6*.root; do
	    eoscp  $file /$8/$file
	done 
    fi

    COPIED=0
    for file in *$7*$6*.root; do
	eos ls /$8/$file
	if [ $? -ne 0 ];
	then
	    echo $file is not copied via the eoscp method
	    let COPIED=COPIED+1
	fi
    done 
    
    if [ $COPIED -eq 0 ];
    then
	rm $outfilenames
	exit 0
    fi

    #third try : to copy via mounting eos in local directory
    echo is mounting eos
    mkdir eos


    COUNTER1=0
    /afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select -b fuse mount eos
    mountpoint eos
    while [ $? -ne 0 ]; 
    do
	if [ $COUNTER1 -gt 20 ]; then
	    break
	fi
	/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select -b fuse mount eos
	let COUNTER1=COUNTER1+1
	echo ${COUNTER1}th Try to mount eos
	sleep 10
	mountpoint eos
    done

    mountpoint eos
    if [ $? -ne 0 ]; then
	echo Eos not mounted after 20 tries
	exit 1
    fi

    mkdir -p $8

    if [ -f  $8/$outfilename ]; then
	echo "the file exists, is being renamed"
	rm -f $8/${outfilename}_
	mv $8/$outfilename $8/${outfilename}_
    fi

    COUNTER2=0
    while [ ! -f  $8/$outfilename ]
    do
	if [ $COUNTER2 -gt 20 ]; then
	    break
	fi
	cp $outfilenames $8/
	let COUNTER2=COUNTER2+1
	echo ${COUNTER2}th Try
	sleep 10
    done

    if [ ! -f  $8/$outfilename ]; then
	echo "The file was not copied to destination after 20 tries"
	exit 1
    fi


    /afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select -b fuse umount eos
    rm -rf eos
else
    mkdir -p $8


    if [ -f  $8/$outfilename ]; then
	echo "the file exists, is being renamed"
	rm -f $8/${outfilename}_
	mv $8/$outfilename $8/${outfilename}_
    fi

    COUNTER2=0
    while [ ! -f  $8/$outfilename ]
    do
	if [ $COUNTER2 -gt 20 ]; then
	    break
	fi
	cp $outfilenames $8/
	let COUNTER2=COUNTER2+1
	echo ${COUNTER2}th Try
	sleep 10
    done

    if [ ! -f  $8/$outfilename ]; then
	echo "The file was not copied to destination after 20 tries"
	exit 1
    fi
    rm $outfilenames
fi
