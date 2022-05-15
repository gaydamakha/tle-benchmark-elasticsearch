"""
Usage:
    insert_tests.py
    insert_tests.py requirements
    insert_tests.py -h | --help | --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

from datetime import datetime
import json
from docopt import docopt
from elasticsearch import Elasticsearch
from consts import INDEX_NAME
from common import get_connection


def search_benchmark(conn: Elasticsearch, batch_sizes: list):
    index = f"{INDEX_NAME}_100"
    with open(str(int(datetime.now().replace(microsecond=0).timestamp())) + '_search_results.csv', 'w') as f:
        for size in batch_sizes:
            if not conn.indices.exists(index=index):
                print(f"index {index} does not exist")
                continue
            print(f"Batch size {size}")
            searches = ''
            query = {
                "query": {
                    "bool": {
                        "must": [
                            {
                                "match": {
                                    "sexe": "2"
                                }
                            },
                            {
                                "match": {
                                    "geo_nom": "Caen"
                                }
                            }
                        ]
                    }
                }
            }

            for i in range(0, size):
                searches += ('{}\n' + json.dumps(query) + '\n')
            response = conn.msearch(
                index=index, searches=[searches])
            took = str(response.body['took'])
            print(took)
            f.write(','.join([str(size), took]) + '\n')


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1')
    a = 100
    length = 9
    r = 2
    batch_sizes = [a * r ** (n - 1) for n in range(1, length + 1)]
    search_benchmark(get_connection(), batch_sizes=batch_sizes)
