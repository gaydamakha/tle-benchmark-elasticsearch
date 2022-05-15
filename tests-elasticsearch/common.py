import os
import json
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from collections import deque
import os
from consts import INDEX_NAME, ROOT_DIR
import requests
from elasticsearch.helpers import parallel_bulk, BulkIndexError

load_dotenv()

elasticsearch_host = os.environ.get('ELASTICSEARCH_HOST')
kibana_host = os.environ.get('KIBANA_HOST')
user = os.environ.get('ELASTICSEARCH_USER')
password = os.environ.get('ELASTICSEARCH_PASSWORD')


def get_connection() -> Elasticsearch:
    return Elasticsearch(elasticsearch_host, basic_auth=(user, password))


def create_index(conn: Elasticsearch, name: str):
    if conn.indices.exists(index=name):
        conn.indices.delete(index=name)
    conn.indices.create(index=name, mappings={
        "properties": {
            "annee_universitaire": {
                "type": "keyword"
            }
        }
    })


def bulk_index(conn: Elasticsearch, docs: list, index: str, chunk_size: int):
    try:
        deque(parallel_bulk(conn, actions=docs, index=index,
              chunk_size=chunk_size), maxlen=0)
    except BulkIndexError as e:
        for error in e.errors:
            print(error['index']['error']['reason'])


def get_index_stats(name: str):

    response = requests.get(
        kibana_host + "/api/index_management/stats/" + name, auth=(user, password))
    return json.loads(response.text)['stats']
