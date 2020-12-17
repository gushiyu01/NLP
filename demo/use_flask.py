from flask import Flask, request, render_template

app = Flask(__name__)


# 第一次请求过来执行，之后再有请求不执行
# before_first_request：注册一个函数，在处理第一个请求之前运行。
#
# before_request：注册一个函数，在每次请求之前运行。
#
# after_request：注册一个函数，如果没有未处理的异常抛出，在每次请求之后运行。
#
# teardown_request：注册一个函数，即使有未处理的异常抛出，也在每次请求之后运行。
@app.before_first_request
def first_req():
    print('before first request')


@app.route('/postHello', methods=['post'])
def hello_world():
    try:
        print(request.get_json().get('id'))
        print(request.get_json()['finishFlag'])
    except Exception:

        print(Exception)

    return 'Hello World!'


@app.route('/getHello/<sex>', methods=['get'])
def hello_world2(sex):
    # print(sex)
    # print(__file__)
    # try:
    #     print(request.args['name'])
    #     print(request.args['age'])
    # except BaseException:
    #     print(Exception.args)
    # html模板需要在templates目录下
    return render_template('hello.html', sex=[1, 3, 4, 5])


# 自定义过滤器
# 过滤器注册代码还可以写在初始化代码 __init__.py
def mylen(arg):  # 实现一个可以求长度的函数
    return len(arg)


def interval(test_str, start, end):  # 返回字符串中指定区间的内容
    return test_str[int(start):int(end)]


# 注册过滤器
env = app.jinja_env
env.filters['mylen'] = mylen
env.filters['interval'] = interval


# 视图函数
@app.route('/myfilter')
def myfilter():
    return render_template('myfilter.html', phone='13523511140')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
