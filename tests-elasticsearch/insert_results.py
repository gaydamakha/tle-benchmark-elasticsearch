"""
Usage:
    insert_results.py
    insert_results.py requirements
    insert_results.py -h | --help | --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import os
from docopt import docopt
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
from consts import INDEX_NAME, ROOT_DIR
from common import get_index_stats
from datetime import datetime

load_dotenv()

es = Elasticsearch(os.environ.get('KIBANA_HOST'), basic_auth=(
    os.environ.get('ELASTICSEARCH_USER'), os.environ.get('ELASTICSEARCH_PASSWORD')))


def get_insert_results(batch_sizes: list):
    with open(str(int(datetime.now().replace(microsecond=0).timestamp())) + '_insert_results.csv', 'w') as f:
        for size in batch_sizes:
            index = f"{INDEX_NAME}_{size}"
            stats = get_index_stats(index)
            operations = stats['primaries']['bulk']['total_operations']
            total_time = stats['primaries']['bulk']['total_time_in_millis']
            operations_per_second = (operations / total_time) * 1000
            res = ','.join([index, str(operations),
                            str(total_time), str(operations_per_second)])
            print(res)
            f.write(res + '\n')


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1')
    a = 100
    length = 9
    r = 2
    batch_sizes = [a * r ** (n - 1) for n in range(1, length + 1)]
    get_insert_results(batch_sizes=batch_sizes)
