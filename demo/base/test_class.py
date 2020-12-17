'''
类方法（可调类变量、可被实例调用、可被类调用）
1、类方法通过@classmethod装饰器实现，只能访问类变量，不能访问实例变量；
2、通过cls参数传递当前类对象，不需要实例化。
'''


class Car(object):
    name = 'BMW'

    def __init__(self, name):
        self.name = name

    @classmethod
    def run(cls, speed):
        print(cls.name, speed, '行驶')


# 访问方式1
c = Car("宝马")
c.run("100迈")
# 访问方式2
Car.run("100迈")


class Test(object):
    name = 'Test'

    def __init__(self, name):
        self.name = name

    def run(self, param):
        print(self.name, param)


t = Test('test')
t.run('hello')
