# Developped by Robin Lehn & Sebastien Glass
# Project Voice Recognition - Advanced Operating System

# Functionalities : logs all by the current os processes
# How to call it with jasper : "Jasper" - "Log all the processes"
import os
import re
import subprocess
import datetime


WORDS = ["PROCESSUS", "LOG"]


def handle(text, mic, profile):
    
    # create the log folder if not exists
    now = datetime.datetime.now()
    dirpath = r'~/processusLogs/'
	# permits access to home via the ~
    dirpath = os.path.expanduser(dirpath)
    if not os.path.exists(dirpath):os.makedirs(dirpath)

	# create open the log file
    f = open(dirpath + 'processusLogs_'+now.strftime("%Y-%m-%d %H:%M")+'.log', 'w')

	# get all the current processes
    ps = subprocess.Popen("ps -e", shell=True, stdout=subprocess.PIPE)
    nb  = subprocess.Popen("ps -e | wc -l", shell=True, stdout=subprocess.PIPE)

	# write in the file
    f.write(ps.stdout.read())
    f.write(nb.stdout.read()+ "processes")
    mic.say("processes have been logged in the file")
	


def isValid(text):
    """
        Returns True if the input is related to jokes/humor.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\blog \w*processes\b', text, re.IGNORECASE))
