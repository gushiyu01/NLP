# 学生
class Students(db.Model):
    # 定义表名
    __tablename__ = 'students'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))
    stu_number = db.Column(db.String(32), unique=True)

    # repr()方法显示一个可读字符串,实例返回的内容
    def __repr__(self):
        return '<User: %s %s %s>' % (self.name, self.id, self.stu_number)

    def __init__(self, name, stu_number):
        self.name = name
        self.stu_number = stu_number


# 章节
class ChapterList(db.Model):
    # 定义表名
    __tablename__ = 'chapter_list'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(16))
    params1 = db.Column(db.String(32))
    params2 = db.Column(db.String(32))

    # repr()方法显示一个可读字符串,实例返回的内容
    def __repr__(self):
        return '<User: %s %s %s>' % (self.name, self.id, self.stu_number)

    def __init__(self, name, stu_number):
        self.name = name
        self.stu_number = stu_number




