import subprocess
import time
from ..logger import ConsoleLogger


def gen_run_sh_job(command):
    """
    Create APScheduler compatible job function for it to schedule to run.
    :param command: the shell command to execute
    :return: parameter less function
    """
    def run_sh():
        logger = ConsoleLogger()
        logger.info("run scheduled job at: " + time.strftime("%Y/%m/%d %H:%M:%S"))
        out = subprocess.run(args=[command], universal_newlines=True, stdout=subprocess.PIPE, shell=True)
        logger.info(out.stdout.splitlines())
        pass

    return run_sh
