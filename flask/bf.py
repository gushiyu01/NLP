from flask_bootstrap import Bootstrap
from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run(debug=True, port=8080)
