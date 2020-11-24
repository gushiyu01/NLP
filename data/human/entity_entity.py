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
batch_size = 10000


def get_total_wiki_id():
    """
    分页查询全部wiki_id
    :return:
    """
    sql = "select wikiData_id from USA_EN_ID_1116"
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
    sql = "select count(*) from USA_EN_ID_1116"
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
    sql = "select * from USA_EN_ID_1116 limit %s offset %s "
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
    for i in range(int(total_page) + 1):# 遍历每一页
        # 起始位置
        start = batch_size * i
        # 查询数据
        result_list = get_tweet_by_page(start, batch_size)
        if (len(result_list) > 0):
            print('获取%s到%s数据成功' % (start, start + batch_size))
            entity_file = open('./entity_entity_test.json', 'a+', encoding='utf-8')
            no_deatil = open('./entity_entity_no_detail.json', 'a+', encoding='utf-8')

            for row in result_list:
                # residence P551    residence   居住地 row[6]
                if row[6] != None :
                    dic = get_dict()
                    dic['Head_id'] = row[0]
                    dic['Tail'] = row[6]
                    dic['id'] = ''.join(str(uuid.uuid4()).split('-'))
                    dic['relation_id'] = 'P551'
                    dic['type'] = 'residence'
                    json.dump(dic, entity_file, ensure_ascii=False)
                    entity_file.write('\n')
                # current_official_position P39 current official position   现任官职    row[9]
                if row[9] != None :
                    dic = get_dict()
                    dic['Head_id'] = row[0]
                    dic['Tail'] = row[9]
                    dic['id'] = ''.join(str(uuid.uuid4()).split('-'))
                    dic['relation_id'] = 'P39'
                    dic['type'] = 'current official position'
                    json.dump(dic, entity_file, ensure_ascii=False)
                    entity_file.write('\n')
                # religion  P140    religion    宗教信仰    row[17]
                if row[17] != None :
                    dic = get_dict()
                    dic['Head_id'] = row[0]
                    dic['Tail'] = row[17]
                    dic['id'] = ''.join(str(uuid.uuid4()).split('-'))
                    dic['relation_id'] = 'P140'
                    dic['type'] = 'religion'
                    json.dump(dic, entity_file, ensure_ascii=False)
                    entity_file.write('\n')
                # father    P22 father  父亲  row[18]
                if row[18] != None :
                    if row[18] in all_wiki_ids:
                        dic = get_dict()
                        dic['Head_id'] = row[0]
                        dic['Tail'] = row[18]
                        dic['id'] = ''.join(str(uuid.uuid4()).split('-'))
                        dic['relation_id'] = 'P22'
                        dic['type'] = 'father'
                        json.dump(dic, entity_file, ensure_ascii=False)
                        entity_file.write('\n')
                    else:
                        no_deatil.write(row[18] + ':not in list father')
                        no_deatil.write('\n')
                # mother    P25 mother  母亲  row[19]
                if row[19] != None :
                    if row[19] in all_wiki_ids:
                        dic = get_dict()
                        dic['Head_id'] = row[0]
                        dic['Tail'] = row[19]
                        dic['id'] = ''.join(str(uuid.uuid4()).split('-'))
                        dic['relation_id'] = 'P25'
                        dic['type'] = 'mother'
                        json.dump(dic, entity_file, ensure_ascii=False)
                        entity_file.write('\n')
                    else:
                        no_deatil.write(row[19] + ':not in list mother')
                        no_deatil.write('\n')
                # spouse 20
                # children  P40 child   子女  row[21]
                if row[21] != None :
                    for item in eval(row[21]):
                        if item in all_wiki_ids:
                            dic = get_dict()
                            dic['Head_id'] = row[0]
                            dic['Tail'] = item
                            dic['id'] = ''.join(str(uuid.uuid4()).split('-'))
                            dic['relation_id'] = 'P40'
                            dic['type'] = 'child'
                            json.dump(dic, entity_file, ensure_ascii=False)
                            entity_file.write('\n')
                        else:
                            no_deatil.write(item + ':not in list child')
                            no_deatil.write('\n')
                # sibling   P3373   sibling 兄弟姐妹    row[22]
                if row[22] != None :
                    for item in eval(row[22]):
                        if item in all_wiki_ids:
                            dic = get_dict()
                            dic['Head_id'] = row[0]
                            dic['Tail'] = item
                            dic['id'] = ''.join(str(uuid.uuid4()).split('-'))
                            dic['relation_id'] = 'P3373'
                            dic['type'] = 'sibling'
                            json.dump(dic, entity_file, ensure_ascii=False)
                            entity_file.write('\n')
                        else:
                            no_deatil.write(item + ':not in list sibling')
                            no_deatil.write('\n')
                # academic_degree   P512    academic degree 学位  row[25]
                if row[25] != None :
                    dic = get_dict()
                    dic['Head_id'] = row[0]
                    dic['Tail'] = row[25]
                    dic['id'] = ''.join(str(uuid.uuid4()).split('-'))
                    dic['relation_id'] = 'P512'
                    dic['type'] = 'academic degree'
                    json.dump(dic, entity_file, ensure_ascii=False)
                    entity_file.write('\n')
                # member_of P463    member of   所属组织    row[26]
                if row[26] != None :
                    dic = get_dict()
                    dic['Head_id'] = row[0]
                    dic['Tail'] = row[26]
                    dic['id'] = ''.join(str(uuid.uuid4()).split('-'))
                    dic['relation_id'] = 'P463'
                    dic['type'] = 'member of'
                    json.dump(dic, entity_file, ensure_ascii=False)
                    entity_file.write('\n')
                # employer  P108    employer    雇主  row[27]
                if row[27] != None :
                    dic = get_dict()
                    dic['Head_id'] = row[0]
                    dic['Tail'] = row[27]
                    dic['id'] = ''.join(str(uuid.uuid4()).split('-'))
                    dic['relation_id'] = 'P108'
                    dic['type'] = 'employer'
                    json.dump(dic, entity_file, ensure_ascii=False)
                    entity_file.write('\n')
            print('over')
            entity_file.close()
    print("耗时：", time.time() - start_time)


limit_offset_query()


