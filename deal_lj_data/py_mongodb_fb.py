from pymongo import MongoClient
from es_config import bulk_insert
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
    #
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
            try:
                if tt.get('fb_mid') is "":
                    print(tt)
                    continue
                body = {
                    '_index': 'wde_mfb_temp',
                    '_type': '_doc',
                    '_id': tt.get('fb_mid'),
                    '_source': {
                        'rootForwardNum': tt.get('nfwd'),
                        'themeId': tt.get('theme_id'),
                        'language': tt.get('lang'),
                        'screenName': tt.get('sname'),
                        'atUserScreenNameList': ','.join(tt.get('fb_lat_sname')),
                        'content': tt.get('cont'),
                        'spec': tt.get('_spec'),
                        'likeNum': tt.get('nlike'),
                        'rootLikeNum': tt.get('fb_r_nlike'),
                        'messageType': tt.get('fb_msg_type'),
                        'sourceCont': tt.get('source_cont'),
                        'extractVersion': tt.get('_ex'),
                        'videoList': tt.get('lvideo'),
                        'replyNum': tt.get('nrply'),
                        'pictureList': tt.get('lpic'),
                        'channelId': tt.get('_ch'),
                        'rootReplyNum': tt.get('fb_r_nrply'),
                        'publishTime': tt.get('pt'),
                        'fansNum': tt.get('nfans'),
                        'audioList': tt.get('laudio'),
                        'friendsNum': tt.get('nfri'),
                        'messageId': tt.get('tw_mid'),
                        'rootMessageId': tt.get('fb_r_mid'),
                        'rootUserId': tt.get('fb_r_uid'),
                        'userId': tt.get('uid'),
                        'url': tt.get('fb_url'),
                        'forwardNum': tt.get('nfwd'),
                        'appDataProvider': tt.get('adp'),
                        'clientRemark': tt.get('client_remark'),
                        'gatherTime': tt.get('gt'),
                        'location': tt.get('loc'),
                        'hashTagList': tt.get('fb_lhashtag')
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


get_data('WDE_mfb_Temp')
