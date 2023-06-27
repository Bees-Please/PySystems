from datetime import datetime
from datetime import date
import pytz
import os

'''
V1.1b
- Fixed timestamps display bug as they where not updating
- Added milliseconds
- Added object return with **kwargs for returning args with the specific message
    - See Lobster class
- Changed debug mode to be on by default, as this lib is for debugging
- Added function this_moment() to get the current time to be used outside of the lib
'''

# Time type setting
mt_tz = pytz.timezone('America/Phoenix')
today = date.today()
NOW_AZ = datetime.now(mt_tz).strftime("%H.%M.%S")
TODAY_AZ = date.today().strftime("%Y_%d_%m")
LS = "[" + NOW_AZ + "] "
fileName = "logs\log-" + TODAY_AZ + "_" + NOW_AZ + ".txt"

# Default print is just white
HEAD = '\033[95m'  # Header purple/ query
OKBL = '\033[94m'  # Verbose blue
OKCY = '\033[96m'  # Debug cyan
OKGR = '\033[92m'  # Good green
WARN = '\033[93m'  # Yellow warning
FAIL = '\033[91m'  # Fail red
END = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


# Create log directory if it doesn't already exist,
# chose this wording to not alarm anyone in the case
# they see the message.
def log_init():
    try:
        os.mkdir("logs")
        print(OKGR + LS + "Created log directory" + END)
    except:
        print(OKGR + LS + "Found log directory" + END)


# Create the log file .txt itself, error not verbose
# fix later?
def create_log():
    # This log only happens for this instance
    # We're doing this verbosely even though the parent function has this
    # for the sake of information.
    try:
        log_file = open(fileName, "x")
    except:
        lprint("Error opening log, opening in append mode", "w")
        log_file = open(fileName, "a")
    finally:
        lprint("Log file created: " + os.getcwd() + "\\" + fileName, "i")
        log_file.close()

    lwrite("Log created successfully, hi there!", "s", True)
    if debug_mode:
        lwrite("Debug mode is ON", "d")


# Possible status':
#   s = critical success
#       Text will be green
#       Use for critical successes
#
#   i = info
#       Text will be white
#       Use for passing information
#
#   d = debug
#       Text will be cyan
#       Use for passing debug statements
#
#   w = warn
#       Text will be yellow
#       Use for warnings of possible failures
#
#   e = critical failure
#       Text will be red
#       Use for critical failures
#
#   B = bold
#       Text will be bold
#       Use when needed
#
#   U = underline
#       Text will be underlined
#       Use when needed

# If you see purple text, you didn't specify a status.
def lwrite(msg, status, no_print=False):
    severity = "NONE"
    if status == 's':
        severity = "SUCCESS"
    elif status == 'i':
        severity = "INFO"
    elif status == 'd':
        severity = "DEBUG"
    elif status == 'w':
        severity = "WARNING"
    elif status == 'e':
        severity = "ERROR"
    else:
        severity = "NONE"

    logFile = open(fileName, "a")
    logFile.writelines(
        this_moment() + "[" + severity + "] " + msg + "\n" if not no_print else LS + "[" + severity + "] " + "[NOT PRINTED] " + msg + "\n")
    if not no_print:
        lprint(msg, status)
    logFile.close()


def lprint(msg, status):
    if status == 's':
        print(OKGR + this_moment() + msg + END)
    elif status == 'i':
        print(this_moment() + msg)
        # What, did you think I had something special here?
    elif status == 'd':
        if debug_mode:
            print(OKCY + this_moment() + msg + END)
    elif status == 'w':
        print(WARN + this_moment() + msg + END)
    elif status == 'e':
        print(FAIL + this_moment() + msg + END)
    else:
        print(HEAD + this_moment() + msg + END)


def tb_log_init(mode=True):
    global debug_mode
    debug_mode = mode
    log_init()
    create_log()


def this_moment():
    return "[" + datetime.now(pytz.timezone('America/Phoenix')).strftime("%H.%M.%S.%f")[:-3] + "] "


class Lobster(object):
    def __init__(self, msg, sev="i", *args, **kwargs):
        self.sev = sev
        self.msg = msg
        self.kwargs = kwargs
        self.args = args
        self.str = msg

    def get_kwarg(self, kw):
        return self.kwargs[kw]

    def get_args(self):
        return self.args

    def set_kwarg(self, kw, value):
        self.kwargs.update({kw: value})

    def set_msg(self, msg):
        self.msg = msg

    def set_sev(self, sev):
        self.sev = sev

    def lwrite(self, msg=None, sev=None):
        if msg is None:
            lwrite(self.msg, self.sev)
        else:
            lwrite(msg, sev)