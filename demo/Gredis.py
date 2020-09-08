import json
import redis

redisOperator = redis.Redis(host='172.16.12.58', port=6379, password="ictbda_aq")

type1 = type(redisOperator.get())
print(type1)
