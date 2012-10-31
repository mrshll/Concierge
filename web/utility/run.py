import logging
import os

def run_command(command):
    status = os.system(command)
    if not os.WIFEXITED(status):
        raise Exception("Command '%s' exited in unknown manner", command)
    exit_status = os.WEXITSTATUS(status)
    if exit_status != 0:
        raise Exception("Command '%s' failed." % command)
    logging.info("Command '%s' executed." % command)
