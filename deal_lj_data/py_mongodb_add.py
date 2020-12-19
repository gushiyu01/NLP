from pymongo import MongoClient
from es_config import bulk_insert
import time

batch_size = 5000


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

    # 查询条件
    # my_query = {"theme_id": "ht000000"}

    # 哪些字段不展示
    # {'rname': 0, 'pt': 0}
    # 展示哪些字段
    # {'rname': 1, 'pt': 1}

    # return con[collection_name].find(my_query, {'rname': 1, 'pt': 1}).limit(batch_size).skip(skip)
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
    print('开始时间', start_time)
    for i in range(int(total_page) + 1):    # 遍历每一页
        # 起始位置
        start = batch_size * i
        print('第'+str(i)+'页')
        # 查询数据
        lists = []
        result_list = get_data_by_page(start, collection_name)
        for tt in result_list:
            try:
                if tt.get('_key') is "":
                    continue
                body = {
                    '_index': 'wde_mtw_temp',
                    '_type': '_doc',
                    '_id': tt.get('_key'),
                    '_source': {
                        'rootForwardNum': tt.get('nfwd'),
                        'themeId': tt.get('theme_id'),
                        'language': tt.get('lang'),
                        'screenName': tt.get('uname'),
                        # 'atUserScreenNameList': ','.join(tt.get('wb_lat_sname')),
                        'content': tt.get('cont'),
                        'spec': tt.get('_spec'),
                        'likeNum': tt.get('nlike'),
                        'rootLikeNum': tt.get('wb_r_nlike'),
                        'messageType': tt.get('wb_msg_type'),
                        'sourceCont': tt.get('source_cont'),
                        'extractVersion': tt.get('_ex'),
                        'videoList': tt.get('lvideo'),
                        'replyNum': tt.get('nrply'),
                        'pictureList': tt.get('lpic'),
                        'channelId': tt.get('_ch'),
                        'rootReplyNum': tt.get('wb_r_nrply'),
                        'publishTime': int(int(tt.get('pt'))/1000),
                        'fansNum': tt.get('nfans'),
                        'audioList': tt.get('laudio'),
                        'friendsNum': tt.get('nfri'),
                        'messageId': tt.get('tw_mid'),
                        'rootMessageId': tt.get('wb_r_mid'),
                        'rootUserId': tt.get('wb_r_uid'),
                        'userId': tt.get('sname'),
                        'url': tt.get('url'),
                        'forwardNum': tt.get('nfwd'),
                        'appDataProvider': tt.get('adp'),
                        'clientRemark': tt.get('client_remark'),
                        'gatherTime': int(int(tt.get('gt'))/1000),
                        'location': tt.get('loc'),
                        'hashTagList': tt.get('wb_lhashtag')
                    }
                }
            except Exception as e:
                print(e)
            lists.append(body)
        print(len(lists))
        res = bulk_insert(lists)
        print(res)
    print('over')
    print('总耗时', time.time() - start_time)


get_data('WDE_mtw_Add_quchong')
