from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
api = Api(app)

parser = reqparse.RequestParser()  # 定义全局的解析实体
# 定义参数 data，类型必须是整数
parser.add_argument('data', type=int, help='必须提供参数')


class HelloRestful(Resource):
    def get(self):
        return {'greet': 'Hello Flask RESTful!'}


# 初始化待办列表
todos = {
    'todo_1': "读《程序员的自我修养》",
    'todo_2': "买点吃的",
    'todo_3': "去看星星"
}


class Todo(Resource):
    # 根据 todo_id 获取代办事项
    @staticmethod
    def get(todo_id):

        return {todo_id: todos[todo_id]}

    # 新增一个待办事项
    @staticmethod
    def post(todo_id):

        # 获取解析器中定义的参数 并校验
        parser.parse_args()

        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


api.add_resource(HelloRestful, '/')
api.add_resource(Todo, '/todo/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
