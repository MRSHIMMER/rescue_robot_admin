# -*- coding: UTF-8 -*-
from flask import Flask
from flask import request
from sqlalchemy import true
from functional.turtlebot_navigation import *

# flask run --host=0.0.0.0    接收外网请求

app = Flask(__name__)


@app.route("/")
def index():
  return "<p>Flask app index page!</p>"


@app.route("/api")
def hello_world():
  return "<p>Hello, World!</p>"


@app.route("/api/get")
def tesGet():
  return "get请求跨域成功"


@app.route("/api/post", methods=['POST', 'GET'])
def testPost():
  return "post请求跨域成功!"


@app.route("/api/navigation")
def navigation():
  send_navigation_command()
  return "导航成功"


@app.route("/api/navigation2", methods=['POST', 'GET'])
def navigation2():
  send_navigation_command2(request.get_json())
  return "navigation2请求跨域成功"


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=true)
