#!/usr/bin/env python
import ROOT as root
nFilesPerJob=3
import sys
import getpass
from ROOT import TFile, TH1
user = getpass.getuser()
if not len(sys.argv) == 3 :
    print "exactly two options are needed : "
    print "%s [working dir] [output dir on eos]" % (sys.argv[0])
    exit()
    #to run ./condor.py in_directory Out_directory

#CheckFailedJobs=True
CheckFailedJobs=False
hname = "Hamb/CutFlowTable/CutFlowTable"

prefix = "out"
OutPath = "/eos/cms/store/user/%s/%s" % (user, sys.argv[2] )

from Samples94.Samples import MiniAOD94Samples as samples
for sample in samples:
    sample.MakeJobs( nFilesPerJob , "%s/%s" % (OutPath , prefix) )

import os
from shutil import copy
from os import listdir
from os.path import isfile, join, splitext, basename

workingdir = sys.argv[1]
while os.path.isdir( "./%s" % (workingdir) ):
    workingdir += "_"
os.mkdir( workingdir )

file_sh = open("%s/Submit.sh" % (workingdir) , "w" )

from subprocess import call
call(["voms-proxy-init" , "--out" , "./%s/.x509up_u%d" % ( workingdir , os.getuid()) , "--voms" , "cms" , "--valid" , "1000:0"])

FailedJobs = {}
if CheckFailedJobs:
    for sample in samples:
        #if not sample.Name.count("GGH") : #for signal sample systs 
        #if not sample.Name.count("DYMG"): #for signal sample systs 
        #    continue

        ListOfFailedJobs = []
        for job_ in sample.Jobs :
            outfile = job_.Output
            job = job_.Index + 1
            if isfile( outfile ) :
                #fileOpen = root.TFile(outfile).IsOpen()
                #if fileOpen:
                #   root.TFile(outfile).Close()
                #   print "===> file %s closed succesfully"%(outfile)
                ff = TFile.Open(outfile)
                if not ff :
                    ListOfFailedJobs.append( str(job) )
                    print job, outfile, "File exist, but can not be opened"
                    continue
                h = ff.Get("%s_%s_0"% ( hname , sample.Name) )
                if not h == None :
                    ntotal = h.GetBinContent(1)
                    if ntotal == 0:
                        if not sample.IsData : #data may be is null because of json
                            print job
                            print outfile + " : Exists with no entry"
                            ListOfFailedJobs.append( str(job))
                else :
                    ListOfFailedJobs.append(str( job ))
                    print job
                    print outfile + " : Exists, without histogram"
                ff.Close()
            else :
                ListOfFailedJobs.append( str(job))
                print job
                print outfile + " : file doesn't exist  "

        FailedJobs[ sample.Name ] = ListOfFailedJobs
    print FailedJobs

file_sh = open("%s/Submit.sh" % (workingdir) , "w" )

#Only when GGH or VBF samples are needed.
for sample in samples:
#    if not sample.Name.count("VBF"):
#        continue
    if CheckFailedJobs:
        if len(FailedJobs[ sample.Name ]) > 0:
            loop = 0
	    os.mkdir( "%s/%s" % (workingdir , sample.Name) )
	    copy( "SetupAndRun_condor.sh" , "./%s/%s" % (workingdir , sample.Name) )
	    file = open("%s/%s/Submit.cmd" % (workingdir , sample.Name) , "w" )
	    print >> file, "executable              = %s/%s/%s/SetupAndRun_condor.sh" % (os.getcwd() , workingdir , sample.Name)
	    print >> file, "output                  = $(ClusterId)_$(ProcId).out"
	    print >> file, "error                   = $(ClusterId)_$(ProcId).err"
	    print >> file, "log                     = $(ClusterId)_$(ProcId).log"
	    print >> file, '+JobFlavour             = "tomorrow"'
	    print >> file, "environment             = CONDORJOBID=$(ProcId)"
	    #print >> file, "environment             = CONDORJOBID = FailedJobs[sample.Name][$(ProcId)]" 
	    print >> file, "notification            = Error"
	    #print >> file, "arguments               = %(vomsaddress)s %(scram)s %(cmsver)s %(gitco)s %(sample)s %(out)s %(outdir)s %(nFilesPerJob)d" % { 
	    #print >> file, "arguments               = '%(sample)s%(countor)s[%(list)s]'  %(vomsaddress)s %(scram)s %(cmsver)s %(gitco)s  %(sample)s  %(out)s %(outdir)s %(nFilesPerJob)d" % { 
            #print >> file, "arguments               = %(sample)s%(countor)s[%(list)s] %(vomsaddress)s %(scram)s %(cmsver)s %(gitco)s %(sample)s  %(out)s %(outdir)s %(nFilesPerJob)d" % {
            print >> file, "arguments               = %(list)s %(vomsaddress)s %(scram)s %(cmsver)s %(gitco)s %(sample)s  %(out)s %(outdir)s %(nFilesPerJob)d" % {
	        "vomsaddress":"%s/%s/.x509up_u%d" % (os.getcwd() , workingdir , os.getuid()) ,
	        "scram":os.getenv("SCRAM_ARCH") ,
	        "cmsver":os.getenv("CMSSW_VERSION"),
	        "gitco":"CMSSW_104X" ,
	        "sample":sample.Name ,
	        "out":prefix,
	        "outdir":OutPath,
                #"countor":"RS",
                "list":",".join( FailedJobs[sample.Name] ),                 
	        "nFilesPerJob":nFilesPerJob
	        }
	    print >> file, "queue %d" % (len(FailedJobs[sample.Name]))

	    print >> file, ""

	    file.close()

	    print >> file_sh, "cd %s" % (sample.Name)
	    print >> file_sh, "condor_submit -batch-name %s Submit.cmd" % (sample.Name)
	    print >> file_sh, "cd .."
    else:
	initlen = len(sample.Jobs)
        steps = range( 0 , initlen , 3000)
        if not steps[-1] == initlen :
            steps.append( initlen )
        print "%s : %d"% ( sample.Name , initlen )
        print steps
        for i in range( 0 , len(steps)-1):

          os.mkdir( "%s/%s" % (workingdir , sample.Name) )
          copy( "SetupAndRun_condor.sh" , "./%s/%s" % (workingdir , sample.Name) )

          file = open("%s/%s/Submit.cmd" % (workingdir , sample.Name) , "w" )
          print >> file, "executable              = %s/%s/%s/SetupAndRun_condor.sh" % (os.getcwd() , workingdir , sample.Name)
          print >> file, "output                  = $(ClusterId)_$(ProcId).out"
          print >> file, "error                   = $(ClusterId)_$(ProcId).err"
          print >> file, "log                     = $(ClusterId)_$(ProcId).log"
          print >> file, '+JobFlavour             = "tomorrow"'
          print >> file, "environment             = CONDORJOBID=$(ProcId)"
          print >> file, "notification            = Error"
          print >> file, ""
          #print >> file, "arguments               = %(vomsaddress)s %(scram)s %(cmsver)s %(gitco)s %(sample)s %(out)s %(outdir)s %(nFilesPerJob)d" % {
          print >> file, "arguments               = %(sub)s %(vomsaddress)s %(scram)s %(cmsver)s %(gitco)s %(sample)s  %(out)s %(outdir)s %(nFilesPerJob)d" % {
            "vomsaddress":"%s/%s/.x509up_u%d" % (os.getcwd() , workingdir , os.getuid()) ,
            "scram":os.getenv("SCRAM_ARCH") ,
            "cmsver":os.getenv("CMSSW_VERSION"),
            "gitco":"CMSSW_104X" ,
            "sample":sample.Name ,
            "out":prefix,
            "outdir":OutPath,
            "nfiles":steps[i+1],
            "sub": "SUBMIT",
            "init":steps[i]+1,
            "countor":i,
            "nFilesPerJob":nFilesPerJob
            }
          print >> file, "queue %d" % (len(sample.Jobs))

          print >> file, ""

          file.close()

          print >> file_sh, "cd %s" % (sample.Name)
          print >> file_sh, "condor_submit -batch-name %s Submit.cmd" % (sample.Name)
          print >> file_sh, "cd .."

print "to submit the jobs, you have to run the following commands :"
print "cd %s" % (workingdir)
print "source Submit.sh"
file_sh.close()



