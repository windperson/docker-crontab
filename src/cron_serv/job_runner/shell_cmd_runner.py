import subprocess
import sys
import time
import traceback
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
        # noinspection PyBroadException
        try:
            out = subprocess.check_output(args=[command], universal_newlines=True, shell=True)
            if out and len(out) > 0:
                logger.info(out)
                pass
        except subprocess.CalledProcessError as e:
            logger.error("Run sh job failed:\n%s", e.output)
        except:
            logger.error("Run sh job failed with some other error!\n%s", traceback.format_exc())

    return run_sh
