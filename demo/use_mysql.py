import MySQLdb

conn = MySQLdb.connect(
    db='mybatis',
    host='47.104.168.202',
    user='root',
    password='root',
    charset='utf8'
)


cursor = conn.cursor()
# 准备查询语句 (如果数据量大，需要借助于分页查询)
sql = 'SELECT `id`, `department_name` FROM `department`'
# 查询数据
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    for col in row:
        print(col)

for (i, row) in enumerate(rows):
    print(i)
    print(row)

