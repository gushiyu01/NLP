# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2020/7/28 17:23

@author: syy_ysk

QQ: 1538918352
'''

from elasticsearch import Elasticsearch
from elasticsearch import helpers
from config import config_lda as config

def get_data(start_time, end_time):
    # start_time = '2020-04-03T00:00:00'
    query_dsl = {
        "query": {
            "range": {
                "publishtime": {
                    "gte": start_time,  # >=start
                    "lte": end_time  # <=end
                }
            }
        },
    }
    return query_dsl


def get_data_from_es(es_conn, start_time, end_time):
    host_list = es_conn['host_list']

    es = Elasticsearch(host_list)
    size = 10000
    query = es.search(index=es_conn['es_index'], doc_type=es_conn['doc_type'], body=get_data(start_time, end_time), size = size, scroll='5m')
    results = query['hits']['hits']  # es查询出的结果第一页
    total = query['hits']['total']  # es查询出的结果总量
    scroll_id = query['_scroll_id']  # 游标用于输出es查询出的所有结果
    for i in range(0, int(total / 10000) + 1):
        # scroll参数必须指定否则会报错
        query_scroll = es.scroll(scroll_id=scroll_id, scroll='5m')['hits']['hits']
        results += query_scroll
    data = []
    for one_re in results:
        data_one = {}
        data_one['_id'] = one_re['_id']
        data_one['_index'] = one_re['_index']
        data_one['_type'] = one_re['_type']
        data_one['typekey'] = one_re['_source']['typekey']
        data_one['summary'] = one_re['_source']['summary']
        data.append(data_one)
    return data


def updatas_es(es_conn, df):
    host_list = es_conn['host_list']

    es = Elasticsearch(host_list)
    actions = []
    for index, row in df.iterrows():
        action = {
            "_index": row['_index'],
            "_type": row['_type'],
            "_id": row['_id'],
            "_op_type": 'update',
            "doc": {
                "typekey": row['typekey'],
                "eventid": row['lda_id'],
            },
        }
        actions.append(action)

    up_actions = [actions[i:i + 1000] for i in range(0, len(actions), 1000)]
    for s_actions in up_actions:
        helpers.bulk(es, s_actions, raise_on_error=True)
        print('写入成功')


def updata_es(es_conn, data):
    host_list = es_conn['host_list']

    es = Elasticsearch(host_list)
    es.update(index='analyse_all', doc_type='_doc', id= data['_key'], body={"doc":{"eventid": data['lda_id']}})

if __name__ == '__main__':
    data = get_data_from_es(config['es_conn'], '2020-04-03T00:00:00', '2020-04-05T00:00:00')
    print(len(data))