from pymongo import MongoClient
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
    if total_count <= 0:
        return
    # 总页数
    total_page = total_count / batch_size
    start_time = time.time()
    print(start_time)
    for i in range(int(total_page) + 1):# 遍历每一页
        # 起始位置
        start = batch_size * i
        # 查询数据
        # lists = []
        result_list = get_data_by_page(start, collection_name)
        # lists = list(result_list)
        # for tt in result_list:
        #     lists.append(tt)

        # print(len(lists))
        # return result_list
    end_time = time.time()
    print(end_time - start_time)
# res1 = get_all_count('WDE_JwNews_Temp')
# res2 = get_all_count('WDE_mfb_Temp')
# res3 = get_all_count('WDE_mtw_Temp')
# res4 = get_data_by_page(10, 'WDE_mtw_Temp')
#
# print(res1)
# print(res2)
# print(res3)
# for item in res4:
#     print(item['_id'])


get_data('WDE_mfb_Temp')
