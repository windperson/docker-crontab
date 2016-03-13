import argparse
from .scheduler import CronScheduler


parser = argparse.ArgumentParser();
parser.add_argument('-f', nargs='*', help='crontab file(s) path')
