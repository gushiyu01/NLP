from pymongo import MongoClient
from es_config import bulk_insert
from bson.objectid import ObjectId
import time

batch_size = 1000


def get_connection():
    """
    获取连接
    :return: connection
    """
    client = MongoClient('10.61.2.172', 27017)
    db = client.admin
    db.authenticate('root', '123456')
    connection = client['lj6']
    return connection


# 带条件统计 count_documents({'dt': handle_date})
def get_all_count(collection_name):
    """
    获取集合中的数据总量
    :param collection_name:
    :return:
    """
    con = get_connection()
    return con[collection_name].estimated_document_count()


def get_data_by_page(skip, collection_name):
    """
    分页获取数据
    :param skip:
    :param collection_name:
    :return:
    """
    con = get_connection()
    return con[collection_name].find().limit(batch_size).skip(skip)


def get_data(collection_name):
    """
    获取集合内的全部数据
    :param collection_name:
    :return:
    """
    # 数据总量
    total_count = get_all_count(collection_name)
    print('数据总量', total_count)
    if total_count <= 0:
        return
    # 总页数
    total_page = total_count / batch_size
    print('总页数', total_page)
    start_time = time.time()
    for i in range(int(total_page) + 1):    # 遍历每一页
        # 起始位置
        start = batch_size * i
        # 查询数据
        lists = []
        result_list = get_data_by_page(start, collection_name)
        print('第'+str(i)+'页')
        for tt in result_list:

            ss = str(ObjectId(tt.get('_id')))

            try:
                if ss is "":
                    continue
                body = {
                    '_index': 'wde_jwnews_temp',
                    '_type': '_doc',
                    '_id': ss,
                    '_source': {
                        'themeId': tt.get('theme_id'),
                        'language': tt.get('lang'),
                        'content': tt.get('cont'),
                        'spec': tt.get('_spec'),
                        'sourceCont': tt.get('source_cont'),
                        'extractVersion': tt.get('_ex'),
                        'videoList': tt.get('lvideo'),
                        'replyNum': tt.get('nrply'),
                        'readNum': tt.get('nrd'),
                        'pictureList': tt.get('lpic'),
                        'channelId': tt.get('_ch'),
                        'publishTime': tt.get('pt'),
                        'siteName': tt.get('i_sn'),
                        'siteId': tt.get('i_sid'),
                        'boardName': tt.get('i_bn'),
                        'boardId': tt.get('i_bid'),
                        'keywordList': ','.join(tt.get('lkey')),
                        'url': tt.get('url'),
                        'abstracts': tt.get('abstr'),
                        'appDataProvider': tt.get('adp'),
                        'author': tt.get('author'),
                        'gatherTime': tt.get('gt'),
                        'title': tt.get('title')
                    }
                }
            except Exception as e:
                print(e)
                continue
            lists.append(body)
        print(len(lists))
        res = bulk_insert(lists)
        print(res)
    print('over')
    print(time.time() - start_time)


get_data('WDE_JwNews_Temp')
