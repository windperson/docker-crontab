import argparse
import signal
import time
from .scheduler import CronScheduler
from .logger import ConsoleLogger


class GracefulKiller:
    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.kill_now = True
        pass


logger = ConsoleLogger()
parser = argparse.ArgumentParser(description='A cron replacement scheduler');
parser.add_argument('-f', '--crontab_paths', nargs='*', help='crontab file(s) path')
args = parser.parse_args()
crontab_paths = args.crontab_paths
logger.info("read crontabs:" + ",".join(crontab_paths))
scheduler = CronScheduler()
scheduler.read_crontabs(args.crontab_paths)
scheduler_killer = GracefulKiller()
logger.info("start scheduler")
scheduler.start_scheduler()
while True:
    if scheduler_killer.kill_now:
        scheduler.stop_scheduler()
        break
    else:
        time.sleep(0.5)
    pass
