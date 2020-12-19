from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request
from changestep import do_it

app = Flask(__name__) # 创建一个 Flask 应用
bootstrap = Bootstrap(app) # 为应用初始化 bootstrap


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/a')
def index2():
    return render_template('index2.html')


@app.route('/b')
def index3():
    return render_template('index3.html')


@app.route('/changeSteps', methods=['get'])
def hello_world2():
    steps_ = request.args['steps']
    username_ = request.args['username']
    password_ = request.args['password']
    it = do_it(steps_, username_, password_)
    return it


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
