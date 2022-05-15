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
from docopt import docopt
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
from consts import INDEX_NAME, ROOT_DIR
from common import get_connection, create_index, bulk_index


def insert_benchmark(conn: Elasticsearch, batch_sizes: list):
    for size in batch_sizes:
        index = f"{INDEX_NAME}_{size}"
        create_index(conn, index)
        print(f"Batch size {size}")
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
                    bulk_index(conn, docs, index=index, chunk_size=size)
                    docs = []
                    count = 0
                docs.append({
                    "_op_type": "index",
                    "_id": doc["recordid"],
                    "_source": doc["fields"],
                })
                count += 1
            if len(docs) > 0:
                batch_count += 1
                print(f"Inserting batch #{batch_count}")
                bulk_index(conn, docs, index=index, chunk_size=size)
                total += len(docs)
                docs = []
            print(f"Total {total}")


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1')
    a = 100
    length = 9
    r = 2
    batch_sizes = [a * r ** (n - 1) for n in range(1, length + 1)]
    insert_benchmark(get_connection(), batch_sizes=batch_sizes)
