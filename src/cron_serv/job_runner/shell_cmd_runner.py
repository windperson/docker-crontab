import subprocess
import time
from ..logger import ConsoleLogger


def gen_run_sh_job(command, logger=ConsoleLogger('cron_serv.local-runner')):
    """
    Create APScheduler compatible job function for it to schedule to run.
    :param logger: logger for job runner
    :param command: the shell command to execute
    :return: parameter less function
    """

    def run_sh():
        logger.info("run scheduled job {0} at: {1}".format(command, time.strftime("%Y/%m/%d %H:%M:%S")))
        out = subprocess.run(args=[command], universal_newlines=True, stdout=subprocess.PIPE, shell=True)
        if out.stderr and len(out.stderr.splitlines()) > 0:
            logger.info(out.stderr.splitlines())
            pass
        pass

    return run_sh
