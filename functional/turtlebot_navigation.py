#-*- coding:utf-8   -*-  指定中文编码
import roslibpy
from data.constants import *
import time

client = roslibpy.Ros(host='localhost', port=9090)
client.run()

talker = roslibpy.Topic(client, '/move_base_simple/goal', 'geometry_msgs/PoseStamped')


def send_navigation_command():
  print("进入导航函数1")
  # 需要多次发布topic消息才能奏效，只发一次大概率失败
  temp = 15
  if client.is_connected:
    while (temp > 0):
      temp -= 1
      talker.publish(roslibpy.Message(NAVIGATION_GOAL_A))

  talker.unadvertise()

  # print("函数执行结束")
  # client.terminate()
  client.close()


def send_navigation_command2(coordinate):
  print("进入导航函数2")
  temp = 15
  if client.is_connected:
    while (temp > 0):
      temp -= 1
      talker.publish(roslibpy.Message(coordinate['coordinate']))

  talker.unadvertise()

  # client.terminate()
  client.close()


# def send_navigation_command():
#   print("进入导航函数")

#   while client.is_connected:
#     talker.publish(roslibpy.Message(NAVIGATION_GOAL_A))
#     time.sleep(1)

#   talker.unadvertise()

#   client.terminate()
