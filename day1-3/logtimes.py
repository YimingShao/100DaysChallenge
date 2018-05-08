#Yiming shao, 2018/04/12

'''Extract datetimes from log entries and calculate the time
    between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    my_ary = [None]*1000;
    i = 0;
    for character in line:
        if character.isdigit():
            my_ary[i]=character
            i+=1
    my_year = int(my_ary[0]+my_ary[1]+my_ary[2]+my_ary[3])
    my_month = int(my_ary[4]+my_ary[5])
    my_day = int(my_ary[6]+my_ary[7])
    my_hour = int(my_ary[8]+my_ary[9])
    my_min = int(my_ary[10]+my_ary[11])
    my_sec = int(my_ary[12]+my_ary[13])
    return datetime(my_year,my_month,my_day,my_hour,my_min,my_sec)



def time_between_shutdowns(loglines):
    i=0;
    for events in loglines:
        if SHUTDOWN_EVENT in events:
            if i==0:
                firstdate = convert_to_datetime(events)
                i = 1
            if i==1:
                lastdate = convert_to_datetime(events)
    return (lastdate - firstdate)


