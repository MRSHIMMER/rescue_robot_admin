from flask import Flask

# flask run --host=0.0.0.0    接收外网请求

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"


@app.route("/get")
def test():
  return "get"


if __name__ == '__main__':
  app.run()
