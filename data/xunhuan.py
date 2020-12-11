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
    sql = "SELECT a.twitter_username,b.tw_id FROM ((SELECT twitter_username FROM wiki_org_id ) a LEFT  JOIN t_twitter_info b ON a.twitter_username = b.sname) WHERE twitter_username IS NOT NULL AND tw_id IS NOT NULL"
    cursor.execute(sql)
    rst = cursor.fetchall()
    if rst is None:
        return []

    result = {}
    for item in rst:
        result[item[0]] = str(item[1])
    return result


print(get_total_wiki_id().get('bostonchildrens'))
