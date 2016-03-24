import argparse
import sys
from docker_cron.logger import ConsoleLogger
from docker_cron.docker_cron import init_scheduler


def parse_commandline(logger):
    parser = argparse.ArgumentParser(description='A cron replacement scheduler');
    parser.add_argument('-f', '--crontab_paths', nargs='+', help='crontab file(s) path')
    args = parser.parse_args()
    crontab_paths = args.crontab_paths
    if crontab_paths:
        logger.info("read crontabs:" + ",".join(crontab_paths))
        return crontab_paths
    else:
        parser.print_help()
        sys.exit(1)


def main():
    logger = ConsoleLogger()
    init_scheduler(parse_commandline(logger), logger)
    pass


if __name__ == '__main__':
    main()
