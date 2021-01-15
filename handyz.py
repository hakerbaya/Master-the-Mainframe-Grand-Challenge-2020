#!/usr/bin/env python3

# Python Tool to submit, cancel or get relevant Job Information using ZOAU Util.
# This Tool is very handy for Beginners, specifically new mainframers.
# Tool  Created by Mubashir Ahmad
# Github: @hakerbaya
# Enjoy Hacking 2021.

# See CLI tool options
# -d | --dateset  : to submit a dataset, dataset must contain JCL
#- o | --options  : cancel,list-dds,or check status of job Options: cancel, list-dds, cc-status


# Example Usage:
# handyz.py : Return List Of Jobs
# handyz.py <USERID> : Return List Of Jobs
# handyz.py <USERID> -d "<DATASET_NAME>" : Submits Job, it must be JCL  <DATASET_NAME> : "MTM2020.PUBLIC.JCL(CHK)"
# handyz.py <USERID> <JOBID> -o <OPTION_NAME> : Choose Option Name in a list:
#                                               list-dds, cancel, submit, cc-status

# Examples
# handyz.py z00162
# handyz.py z00162 JOB02811 -o cc-status     : Get STATUS of JOB
# handyz.py z00162 -d "MTM2020.PUBLIC.JCL(CHK)"


from zoautil_py import Datasets, Jobs
from termcolor import cprint
from datetime import datetime
from prettytable import PrettyTable
import click
import subprocess

# Global Variables
jobList = []
listDDs = []
dataSetjobId=''
x=PrettyTable()
x.field_names = ["Owner", "Name", "Id", "Status","Return"]
y=PrettyTable()
y.field_names = ["Stepname","Procstep","Dataset","Format"]

time_dur = str(subprocess.check_output(['uptime']))[13:-3]
time_dur_arr = time_dur.split(', ')
timedur_day = time_dur_arr[0][1:]
timedur_hour = time_dur_arr[1].split(':')[0]
timedur_min = time_dur_arr[1].split(':')[1]


@click.command()
@click.argument('username', default=str(subprocess.check_output(['whoami']))[2:-3])
@click.option('-d','--dataset',help='Submit a dataset <USER.JCL(HELLO)>')
@click.argument('jobid',required=False)
@click.option('-o','--option',type=click.Choice(['cc-status','cancel','list-dds'],case_sensitive=False),help='submit Job, check status or delete job')

# The CLI Options

def cliTool(option,username,jobid,dataset):
 cprint("""
                                                   ___    
    //    / /                                         / / 
   //___ / /  ___       __      ___   /              / /  
  / ___   / //   ) ) //   ) ) //   ) / //   / /     / /   
 //    / / //   / / //   / / //   / / ((___/ /     / /    
//    / / ((___( ( //   / / ((___/ /      / /     / /___

*********************************************************
    Handy tool to submit, cancel, get JOBs Information.
                    
    (o_o)
      |     Happy Hacking :) @Mubashir Ahmad | hakerbaya
    /   \           
*********************************************************

""", "cyan", attrs=['bold'])
 # Get other system details
 now = datetime.now()
 user_name = str(subprocess.check_output(['whoami']))[2:-3]
 print("Welcome back " + user_name)
 detailsDict = {
  'Uptime': '{} {} hrs {} mins'.format(timedur_day, timedur_hour, timedur_min), 
  'Date & Time': now.strftime("%d/%m/%Y %H:%M:%S")
 }

 for detail in detailsDict.items():
   cprint('{:}: '.format(detail[0]), 'green', end='')
   cprint(detail[1], 'blue')
 # Add newline
 print('')
 if(username):
   jobList = Jobs.list(owner=username)
   try:
    for obj in jobList:
        x.add_row([obj['owner'],obj['name'],obj['id'],obj['status'],obj['return']])
    cprint(x,'yellow')
   except:
    cprint("""
          Oops (^-^)
          *** Job list not found *** 
          """, "red",attrs=["blink","bold"])
 # New Line
 print("")
 
 # JOBID- To Check CC-STATUS - SUBMIT JOB - LIST-DDS - CANCEL JOB
 if(jobid):
   # Get DDs associated with Job id
   if(option=="list-dds"):
     try:
       listDDs=Jobs.list_dds(jobid)
       for obj in listDDs:
         y.add_row([obj['stepname'],obj['procstep'],obj['dataset'],obj['format']])
       print("Job DDs")
       print("=======>")
       cprint(y,'green')
     except:
       cprint("Invalid Job id, Try again :(","red",attrs=["bold"])
    
   # Get CCSTATUS accociated with Job id
   if(option == 'cc-status'):
     try:
       jobObj = Jobs.list(job_id=jobid)
       ccstatus = jobObj[0]['status']+jobObj[0]['return']
       print("Job Status")
       print("==========>")
       cprint(jobid+ ": "+ ccstatus,"green",attrs=['bold'])
     except:
       cprint("Invalid Job id, Try again :(","red",attrs=["bold"])
    
   # Cancel any Job- returns 0 -int if successfull, other wise non-zero
   if(option=="cancel"):
     try:
       jobCancelStatus = Jobs.cancel(jobid)
       if(jobCancelStatus == 0):
         cprint("Job Cancelled","green",attrs=['bold'])
       else:
         cprint("Something went wrong, Job Failed to Cancel","red",attrs=['bold'])
     except:
       cprint("Invalid Job id, Try again :(","red",attrs=["bold"])

# Submit a dataset containing JCL
 if(username):
    if(dataset):
      dataSetjobId = Jobs.submit(dataset)
      try:
        if(dataSetjobId):
              cprint("""
              *************************
              \u2713 Dataset Submitted
              *************************
              ""","green")
      except:
        cprint("""
              *************************
              \u274C Dataset not found
              *************************
              """,'red')
                 
      
if __name__ == '__main__':
  cliTool()  
    