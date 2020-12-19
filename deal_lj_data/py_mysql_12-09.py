from pymongo import MongoClient
from mysql_config import get_mysql_connection_cursor
from decimal import Decimal
from es_config import bulk_insert


batch_size = 1000


def get_all_count(doc_type):

    cursor = get_mysql_connection_cursor()
    sql = 'SELECT COUNT(1) FROM t_index_article WHERE `doc_type` = %s'
    p = (doc_type, )
    cursor.execute(sql, p)
    rows = cursor.fetchone()
    return rows[0]


def get_data_by_page(page_num, page_size, doc_type):

    cursor = get_mysql_connection_cursor()
    sql = 'select `doc_id`, `attitude_index`, `sentiment`, `heat` ' \
          'from `t_index_article` ' \
          'where `pt` > "2020-12-09 23:49:03" and `doc_type` = %(doc_type)s ' \
          'limit %(page_num)s, %(page_size)s '
    p = {
        "page_num": page_num,
        "page_size": page_size,
        "doc_type": doc_type
    }
    cursor.execute(sql, p)
    rows = cursor.fetchall()
    return rows


def get_data(doc_type, indexName):

    # 数据总量
    total_count = get_all_count(doc_type)
    print('数据总量', total_count)
    if total_count <= 0:
        return
    # 总页数
    total_page = total_count / batch_size
    print('总页数', total_page)
    for i in range(int(total_page) + 1):    # 遍历每一页
        # 起始位置
        start = batch_size * i
        print('第' + str(i) + '页')
        # 查询数据
        lists = []
        result_list = get_data_by_page(start, batch_size, doc_type)
        for tt in result_list:
            try:
                # print(tt)
                if tt[0] is None or tt[0] is '':
                    continue
                # `doc_id`, `attitude_index`, `sentiment`, `heat`
                action = {
                    "_index": indexName,
                    "_type": '_doc',
                    "_id": tt[0],
                    "_op_type": 'update',
                    "doc": {
                        "attitudeIndex": tt[1],
                        "emotionalTendency": tt[2],
                        "heatDegree": tt[3],
                    },
                }
                lists.append(action)
            except Exception as e:
                print(e)
                continue

        insert = bulk_insert(lists)
        print(insert)
    print('over')


get_data('tw', 'wde_mtw_temp')
