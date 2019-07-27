from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/dzt")
def hello_test():
    return 'hello 大猪蹄子'


if __name__ == '__main__':
    app.run()
