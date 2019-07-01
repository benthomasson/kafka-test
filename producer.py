#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:
    producer [options]

Options:
    -h, --help        Show this page
    --debug            Show debug logging
    --verbose        Show verbose logging
"""
from docopt import docopt
import logging
import sys
from kafka import KafkaProducer

logger = logging.getLogger('producer')


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
    producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
    for i in range(100):
        producer.send('my_favorite_topic', b'hello world')
    producer.flush()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv[1:]))

