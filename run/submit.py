#!/usr/bin/env python
from numpy import linspace 
from params import params 
import os.path 
import sys 

if __name__=='__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-run", action='store_true', help="Run or not")
    parser.add_argument("-waitfor", type=int, help="wait for this job for finish")
    input = parser.parse_args()
    #default parameters 

    jobdir='../jobs/'
    
    textoutput = 1 # 
    Maxorder = 1024
    
    #this import might overwrite the above default parameters 
    #########################################################
    import socket
    machinename = socket.gethostname()
    if 'brutus' in machinename:
        from config.brutus import * 
    elif 'rosa' in machinename:
        from config.rosa import * 
    elif 'monch' in machinename:
        from config.monch import * 
    else:
        print 'where am I ?', machinename 
        sys.exit(1)
    #########################################################

    cmd = ['mkdir', '-p', resfolder]
    subprocess.check_call(cmd)
    

    jobid = input.waitfor 
    for L, W in zip(Llist, Wlist):
        for V in Vlist:
               
                           inputfile = params(latticename, L , W,  
                                              V=V, BETA= BETA,  
                                              Maxorder = Maxorder, itime_max = itime_max,  
                                              RECALC_PERIOD = RECALC_PERIOD, 
                                              WRAP_REFRESH_PERIOD = WRAP_REFRESH_PERIOD, 
                                              SWEEPS=SWEEPS, THERMALIZATION=THERMALIZATION , 
                                              NBLOCKS = NBLOCKS, STEPS_PER_BLOCK = STEPS_PER_BLOCK,
                                              folder=resfolder, textoutput=textoutput)

               
                           bin = prog + ' ' + inputfile 
               
                           args = {}
                           jobname = jobdir + os.path.basename(inputfile).replace('.in','')
               
                           jobid = submitJob(bin,args,jobname,wtime,ncores=ncores,run=input.run, wait=None)
