"""
Usage:
    insert_tests.py
    insert_tests.py requirements
    insert_tests.py -h | --help | --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import ijson
import os
from datetime import datetime
from docopt import docopt
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
from consts import INDEX_NAME, ROOT_DIR

load_dotenv()

es = Elasticsearch(os.environ.get('ELASTICSEARCH_HOST'), basic_auth=(
    os.environ.get('ELASTICSEARCH_USER'), os.environ.get('ELASTICSEARCH_PASSWORD')))


def create_index(name: str):
    if not es.indices.exists(index=INDEX_NAME):
        es.indices.create(index=INDEX_NAME)


def insert_benchmark(bulk_sizes: list):
    # create_index()
    for size in bulk_sizes:
        print(f"Bunch size {size}")
        total = 0
        batch_count = 0
        count = 0
        docs = []
        with open(ROOT_DIR + "/resources/data/fr-esr-atlas_regional-effectifs-d-etudiants-inscrits.json", 'rb') as f:
            for doc in ijson.items(f, "item"):
                if count >= size:
                    total += count
                    batch_count += 1
                    print(f"Inserting batch #{batch_count}")
                    # TODO: insert to elasticsearch and measure
                    docs = []
                    count = 0
                docs.append(doc)
                count += 1

            if len(docs) > 0:
                batch_count += 1
                print(f"Inserting batch #{batch_count}")
                # TODO: insert to elasticsearch and measure
                total += len(docs)
                docs = []
            print(f"Total {total}")


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1')
    a = 100
    length = 9
    r = 2
    bulk_sizes = [a * r ** (n - 1) for n in range(1, length + 1)]
    insert_benchmark(bulk_sizes=bulk_sizes)

# Inserting batch 370195
# 370195000

# Inserting batch 371095
# 37109500
