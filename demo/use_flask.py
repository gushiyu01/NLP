from flask import Flask, request

app = Flask(__name__)


@app.route('/postHello', methods=['post'])
def hello_world():
    print(request.get_json().get('id'))
    print(request.get_json()['finishFlag'])
    return 'Hello World!'


@app.route('/getHello', methods=['get'])
def hello_world2():
    print(request.args['name'])
    print(request.args['age'])
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, port=8080)

