# coding=utf-8
import MySQLdb
import json
import time
import uuid


conn = MySQLdb.connect(
    db='politician_kb',
    host='172.16.12.57',
    user='root',
    password='root',
    charset='utf8'
)

cursor = conn.cursor()
batch_size = 1000


def get_total_wiki_id():
    """
    分页查询全部wiki_id
    :return:
    """
    sql = "select wikiData_id from USA_EN_INFO_1116"
    cursor.execute(sql)
    rst = cursor.fetchall()
    if rst is None:
        return []

    result = []
    for item in rst:
        result.append(item[0])
    return result


def get_total_count():
    """
    分页查询获取总数量
    :return:
    """
    sql = "select count(*) from wiki_org_id"
    cursor.execute(sql)
    rst = cursor.fetchone()
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
    sql = "select * from wiki_org_id limit %s offset %s "
    cursor.execute(sql, [pagesize, start])
    rst = cursor.fetchall()
    return rst


def get_dict():
    dic = {
        "Head_id": "",
        "Tail": "",
        "id": "",
        "relation_id": "",
        "type": "",
        "dataset_tag": [0],
        "ts": -1,
        "e_type": 1,
        "余额": "",
        "金额": "",
        "交易类型": "",
        "交易时间": "",
        "交易结果": "",
        "借贷标志": "",
        "Entity_type": "",
        "image_path": "",
        "评论时间": "",
        "点赞时间": ""
    }

    return dic


def get_twitter_id_by_twitter_name():
    """
    查询全部twitter_name的twitter_id
    :return:
    """
    sql = "SELECT a.twitter_username,b.tw_id FROM ((SELECT twitter_username FROM wiki_org_id ) a LEFT  JOIN t_twitter_info b ON a.twitter_username = b.sname) WHERE twitter_username IS NOT NULL AND tw_id IS NOT NULL"
    cursor.execute(sql)
    rst = cursor.fetchall()
    if rst is None:
        return []

    result = {}
    for item in rst:
        result[item[0]] = str(item[1])
    return result


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
    all_wiki_ids = get_total_wiki_id()
    tw_ids = get_twitter_id_by_twitter_name()
    for i in range(int(total_page) + 1):# 遍历每一页
        # 起始位置
        start = batch_size * i
        # 查询数据
        result_list = get_tweet_by_page(start, batch_size)
        if (len(result_list) > 0):
            print('获取%s到%s数据成功' % (start, start + batch_size))
            entity_file = open('./data/entity_entity_org_test.json', 'a+', encoding='utf-8')
            no_deatil = open('./data/entity_entity_org_no_detail.json', 'a+', encoding='utf-8')
            no_tw_id = open('./data/entity_entity_org_no_tw_id.json', 'a+', encoding='utf-8')

            for row in result_list:
                # P112	founded by	创办者 row[] 24
                if row[24] is not None:
                    for item in eval(row[24]):
                        if item in all_wiki_ids:
                            dic = get_dict()
                            dic['Head_id'] = row[0]
                            dic['Tail'] = item
                            dic['id'] = ''.join(str(uuid.uuid4()).split('-'))
                            dic['relation_id'] = 'P112'
                            dic['type'] = 'founded by'
                            json.dump(dic, entity_file, ensure_ascii=False)
                            entity_file.write('\n')
                        else:
                            no_deatil.write(item + ':not in list founded by')
                            no_deatil.write('\n')
                # P1830	owner of	产权所有人   row[] 25
                if row[25] is not None:
                    for item in eval(row[25]):
                        if item in all_wiki_ids:
                            dic = get_dict()
                            dic['Head_id'] = row[0]
                            dic['Tail'] = item
                            dic['id'] = ''.join(str(uuid.uuid4()).split('-'))
                            dic['relation_id'] = 'P1830'
                            dic['type'] = 'owner of'
                            json.dump(dic, entity_file, ensure_ascii=False)
                            entity_file.write('\n')
                        else:
                            no_deatil.write(item + ':not in list owner of')
                            no_deatil.write('\n')
                # P488	chairperson	主席 row[] 26
                if row[26] is not None:
                    if row[26] in all_wiki_ids:
                        dic = get_dict()
                        dic['Head_id'] = row[0]
                        dic['Tail'] = row[26]
                        dic['id'] = ''.join(str(uuid.uuid4()).split('-'))
                        dic['relation_id'] = 'P488'
                        dic['type'] = 'chairperson'
                        json.dump(dic, entity_file, ensure_ascii=False)
                        entity_file.write('\n')
                    else:
                        no_deatil.write(item + ':not in list chairperson')
                        no_deatil.write('\n')
                # P749	parent organization	上级部门 row[] 27
                if row[27] is not None:
                    for item in eval(row[27]):
                        if item in all_wiki_ids:
                            dic = get_dict()
                            dic['Head_id'] = row[0]
                            dic['Tail'] = item
                            dic['id'] = ''.join(str(uuid.uuid4()).split('-'))
                            dic['relation_id'] = 'P749'
                            dic['type'] = 'parent organization'
                            json.dump(dic, entity_file, ensure_ascii=False)
                            entity_file.write('\n')
                        else:
                            no_deatil.write(item + ':not in list parent organization')
                            no_deatil.write('\n')
                # P355	subsidiary	下级部门   row[] 28
                if row[28] is not None:
                    for item in eval(row[28]):
                        if item in all_wiki_ids:
                            dic = get_dict()
                            dic['Head_id'] = row[0]
                            dic['Tail'] = item
                            dic['id'] = ''.join(str(uuid.uuid4()).split('-'))
                            dic['relation_id'] = 'P355'
                            dic['type'] = 'subsidiary'
                            json.dump(dic, entity_file, ensure_ascii=False)
                            entity_file.write('\n')
                        else:
                            no_deatil.write(item + ':not in list subsidiary')
                            no_deatil.write('\n')
                # P169	chief executive officer	首席执行官 29
                if row[29] is not None:
                    if row[29] in all_wiki_ids:
                        dic = get_dict()
                        dic['Head_id'] = row[0]
                        dic['Tail'] = row[29]
                        dic['id'] = ''.join(str(uuid.uuid4()).split('-'))
                        dic['relation_id'] = 'P169'
                        dic['type'] = 'chief executive officer'
                        json.dump(dic, entity_file, ensure_ascii=False)
                        entity_file.write('\n')
                    else:
                        no_deatil.write(item + ':not in list chief executive officer')
                        no_deatil.write('\n')
                # P2002	Twitter username	twitter账号		row[] 31
                if row[31] is not None:
                    if tw_ids.get(row[31]) is not None:
                        dic = get_dict()
                        dic['Head_id'] = row[0]
                        dic['Tail'] = row[31]
                        dic['id'] = ''.join(str(uuid.uuid4()).split('-'))
                        dic['relation_id'] = 'P2002'
                        dic['type'] = 'Twitter username'
                        json.dump(dic, entity_file, ensure_ascii=False)
                        entity_file.write('\n')
                    else:
                        no_tw_id.write(row[31] + ':no twitter id')
                        no_tw_id.write('\n')
            print('over')
            entity_file.close()
            no_deatil.close()
            no_tw_id.close()
    print("耗时：", time.time() - start_time)


limit_offset_query()

