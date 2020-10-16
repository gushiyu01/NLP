import json
import redis

redisOperator = redis.Redis(host='172.16.12.58', port=6379, password="ictbda_aq")

type1 = type(redisOperator.get('1'))
print(type1)


# 建议使用以下连接池的方式
# 设置decode_responses=True，写入的KV对中的V为string类型，不加则写入的为字节类型。
pool = redis.ConnectionPool(host='47.104.168.202', port=6379, db=0, decode_responses=True)
rs = redis.Redis(connection_pool=pool)

rs.set('myname', '谷世宇')
print(rs.get('1'))
