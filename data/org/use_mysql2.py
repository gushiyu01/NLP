# -*- coding: utf-8 -*-
import MySQLdb
import json
import time

conn = MySQLdb.connect(
    db='politician_kb',
    host='172.16.12.57',
    user='root',
    password='root',
    charset='utf8'
)

cursor = conn.cursor()
batch_size = 30000


def get_total_count():
    """
    分页查询获取总数量
    :return:
    """
    sql = "select count(*) from wiki_org_info"
    cursor.execute(sql)
    rst = cursor.fetchone()
    print(rst[0])
    if rst is None:
        return 0
    return rst[0]


def get_tweet_by_page(start, pagesize):
    """
    分页查询
    :param start:
    :param pagesize:
    :return:
    """
    sql = "select * from wiki_org_info limit %s offset %s "
    cursor.execute(sql, [pagesize, start])
    rst = cursor.fetchall()
    return rst

def limit_offset_query():
    """
    分页查询
    :return:
    """
    # 数据总量
    total_count = get_total_count()
    if total_count <= 0:
        return
    # 总页数
    total_page = total_count / batch_size
    # 开始时间
    start_time = time.time()
    for i in range(int(total_page) + 1):# 遍历每一页
        # 起始位置
        start = batch_size * i
        # 查询数据
        result_list = get_tweet_by_page(start, batch_size)
        if (len(result_list) > 0):
            print('获取%s到%s数据成功' % (start, start + batch_size))
            entity_file = open('./data/entity_org_test.json', 'a+', encoding='utf-8')


            for row in result_list:

                dic = {
                    "mongo_id": "",
                    "meta_type": "entity",
                    "Entity_name": "",
                    "Entity_type": "organization",
                    "Chinese_name": "",
                    "image_path": "",
                    "vital_node": 0
                }

                dic['mongo_id'] = row[0]
                dic['Entity_name'] = '' if ( row[1] == None ) else row[1]
                dic['Chinese_name'] = '' if ( row[2] == None ) else row[2]
                print( row[7] == 'None' )
                if ( row[7] == 'None' ):
                    dic['image_path'] = ''
                else:
                    ll = eval(row[7])
                    print(ll)
                    dic['image_path'] = ll[0]
                json.dump(dic, entity_file, ensure_ascii=False)
                entity_file.write('\n')
            print('over')
            entity_file.close()
    print("耗时：", time.time() - start_time)


limit_offset_query()





