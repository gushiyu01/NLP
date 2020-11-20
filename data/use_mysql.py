# -*- coding: utf-8 -*-
import MySQLdb
import json

conn = MySQLdb.connect(
    db='politician_kb',
    host='172.16.12.57',
    user='root',
    password='root',
    charset='utf8'
)


cursor = conn.cursor()
# 准备查询语句 (如果数据量大，需要借助于分页查询)
sql = 'SELECT wikiData_id, entity_name, chinese_name, image FROM `USA_EN_INFO_1116`'
# 查询数据
cursor.execute(sql)
rows = cursor.fetchall()

entity_file = open('./entity.json', 'w', encoding='utf-8')


for row in rows:

    dic = {
        "mongo_id": "",
        "meta_type": "entity",
        "Entity_name": "",
        "Entity_type": "human",
        "Chinese_name": "",
        "image_path": "",
        "vital_node": 0
    }

    dic['mongo_id'] = row[0]
    dic['Entity_name'] = '' if ( row[1] == None ) else row[1]
    dic['Chinese_name'] = '' if ( row[2] == None ) else row[2]
    dic['image_path'] = '' if ( row[3] == None ) else row[3]
    json.dump(dic, entity_file, ensure_ascii=False)
    entity_file.write('\n')
print('over')
entity_file.close()





