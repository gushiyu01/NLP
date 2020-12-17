from elasticsearch import Elasticsearch
from elasticsearch import helpers


e = Elasticsearch('42.192.137.187:9200', timeout=60, max_retries=10, retry_on_timeout=True)

d = {
    'summary': 'aaa'
}

try:
    e.update(index='gsy', doc_type='_doc', body={"doc": d}, id=99)

except Exception as e:
    print(e)
