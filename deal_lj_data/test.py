from elasticsearch import Elasticsearch
from elasticsearch import helpers
from es_config import bulk_insert
import time


actions = []

for i in range(10):
    action = {
        "_index": 'wde_mtw_temp',
        "_type": "_doc",
        "_id": i,

        "_source": {
            "hashTagList": [str(i), str(i*i)]
        },
    }
    actions.append(action)
bulk_insert(actions)
actions = []

for i in range(10):
    action = {
        "_index": 'test',
        "_type": "_doc",
        "_id": i,
        "_op_type": 'update',
        "doc": {
            "username": "[1, 2, 3]"
        },
    }
    actions.append(action)
bulk_insert(actions)
