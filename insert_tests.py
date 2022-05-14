"""
Usage:
    insert_tests.py
    insert_tests.py requirements
    insert_tests.py -h | --help | --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import json
from datetime import datetime
from docopt import docopt


def insert_benchmark():
    print('POP')


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1')
    insert_benchmark()
