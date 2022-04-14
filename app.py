from crypt import methods
from flask import Flask
from sqlalchemy import true

# flask run --host=0.0.0.0    接收外网请求

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"


@app.route("/api/get")
def tesGet():
  return "get"


@app.route("/api/post", methods=['POST', 'GET'])
def testPost():
  return "post"


# if __name__ == '__main__':
#   app.run(host='0.0.0.0', port=8002, debug=true)
