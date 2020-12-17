from elasticsearch import Elasticsearch
from elasticsearch import helpers


e = Elasticsearch('42.192.137.187:9200', timeout=60, max_retries=10, retry_on_timeout=True)
# print(e.info())
# print(e.index(index='gsy', doc_type='_doc', body=body, id=110))


def bulk_insert(l):
    return helpers.bulk(e, l, stats_only=False)[0]
