from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # 导入 SQLAlachamy
from sqlalchemy import *
from .allclass import Students
"""
sqlalchemy模块内置的查询条件
and_(): 并且
or_(): 或者
not_(): 非, 条件只能一个
"""
# 创建 Flask 应用
app = Flask(__name__)
# 配置数据库的地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@172.16.12.57:3306/test'
# 跟踪数据库的修改 --> 不建议开启 未来的版本中会移除
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = False
# 指定配置，用来省略提交操作
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)  # 初始化应用


def create_table():
    # 删除表
    db.drop_all()
    # 创建表
    db.create_all()

    stu1 = Students(name='小明', stu_number='1918101')
    stu2 = Students(name='小红', stu_number='1918102')
    stu3 = Students(name='小华', stu_number='1918103')
    db.session.add_all([stu1, stu2, stu3])
    db.session.commit()


# 建表函数
# create_table()


@app.route('/')
def index():
    # 通过sql查询
    items = db.session.execute('select * from students order by id desc')
    items = list(items)
    print(items)
    return 'Hello flask!'


@app.route('/select')
def index2():
    # items = Students.query.all()

    # 根据id查询数据
    s = Students.query.get(1)
    print(s.id)
    # 筛选查询
    s2 = Students.query.filter(Students.id > 2).all()
    print(s2)

    # 数据库分页查询, paginate(参数1, 参数2, 参数3), 参数1代表查询的页码, 页码值从1开始; 参数2代表每一页查询的总数据条数;
    # 参数3是布尔类型,用来设定当查询超出范围时, 以何种方式返回结果, 默认为True, 以404错误信息返回, 如果为False此时以空列表形式返回.
    s3 = Students.query.filter(Students.id > 1).paginate(2, 3, False)
    print(s3.items)

    # 统计总量，多重筛选
    s4 = Students.query.filter(and_(Students.id > 1, Students.name.startswith("小"))).count()
    print(s4)

    # 根据id更新数据
    select = Students.query.filter(Students.id == 1).update({'name': '小谷啊'})
    print(select)

    # 执行sql
    # items = db.session.execute('select * from students order by id desc')
    # items = list(items)
    # print(items)

    # 根据id删除数据
    # Students.query.filter(Students.id == 2).delete()

    # 添加数据
    # stu = Students(name="花花", stu_number="5221314")
    # db.session.add(stu)

    return 'Hello flask!'


if __name__ == '__main__':
    app.run(debug=True)
