import argparse
import os
import sys
from cron_serv.logger import ConsoleLogger
from cron_serv.cron_serv import init_scheduler


def is_valid_file(parser, arg):
    if not os.path.isfile(arg):
        parser.error('The file {} does not exist!'.format(arg))
    else:
        # File exists so return the filename
        return arg


def parse_commandline(logger):
    parser = argparse.ArgumentParser(description='A cron replacement scheduler')
    parser.add_argument('-f', '--crontab_paths', nargs='+', help='crontab file(s) path',
                        type=lambda path: is_valid_file(parser, path))
    args = parser.parse_args()
    crontab_paths = args.crontab_paths
    if crontab_paths:
        logger.info("read crontabs: %s", ", ".join(crontab_paths))
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
