#!/usr/bin/env python

import sys
import argparse
import logging

from .colorize import Configuration
from .colorize import Colorize
from . import APP


def logging_setup(args):
    def set_format(logger, format, level=logging.INFO):
        formatter = logging.Formatter(format, args.datefmt)
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(level)
    logger = logging.getLogger('colorize.main')
    shlogger = logging.getLogger('colorize.shell')

    set_format(logger, '%(message)s')
    set_format(shlogger, args.format)


def main():
    parser = argparse.ArgumentParser(
        prog=APP.program,
        description=APP.description,
        )
    parser.add_argument('command', nargs='*',
                        help='Command to be executed')
    parser.add_argument('-f', '--format', default='%(message)s',
                        help='Configures both stdout and stderr')
    parser.add_argument('--date-format', dest="datefmt",
                        default='%m-%d %H:%M:%S',
                        help='Set the date format')

    args = parser.parse_args()

    logging_setup(args)

    conf = Configuration()
    conf.process()
    colorize = Colorize(conf)
    colorize.process(args.command)
    sys.exit(colorize.return_code)


if __name__ == '__main__':
    main()
