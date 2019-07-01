#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:
    consumer [options]

Options:
    -h, --help        Show this page
    --debug            Show debug logging
    --verbose        Show verbose logging
"""
from docopt import docopt
import logging
import sys
from kafka import KafkaConsumer

logger = logging.getLogger('consumer')


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parsed_args = docopt(__doc__, args)
    if parsed_args['--debug']:
        logging.basicConfig(level=logging.DEBUG)
    elif parsed_args['--verbose']:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)
    consumer = KafkaConsumer('my_favorite_topic', bootstrap_servers='127.0.0.1:9092', group_id="mygroup", auto_offset_reset='earliest')
    for msg in consumer:
        print(msg)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv[1:]))

