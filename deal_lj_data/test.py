from elasticsearch import Elasticsearch
from elasticsearch import helpers
from es_config import bulk_insert
import time


actions = []

for i in range(10):
    action = {
        "_index": 'gsy',
        "_type": "_doc",
        "_id": i,

        "_source": {
            "s": i*i
        },
    }
    actions.append(action)
bulk_insert(actions)
# actions = []
#
# for i in range(10):
#     action = {
#         "_index": 'gsy',
#         "_type": "_doc",
#         "_id": i,
#         "_op_type": 'update',
#         "doc": {
#             "emotion": i*i
#         },
#     }
#     actions.append(action)
# bulk_insert(actions)
print(int(int(1579407050000)/1000))
