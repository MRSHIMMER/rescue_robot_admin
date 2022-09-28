#-*- coding:utf-8   -*-  指定中文编码
import roslibpy
from data.constants import *
import time

client = roslibpy.Ros(host='localhost', port=9090)
client.run()

talker = roslibpy.Topic(client, '/move_base_simple/goal', 'geometry_msgs/PoseStamped')


def send_navigation_command():
    if client.is_connected:
        talker.publish(roslibpy.Message(NAVIGATION_GOAL_A))
        print('Sending navigation command...')
        time.sleep(1)
    else:
        print("client未连接!")

    # talker.unadvertise()
    # client.terminate()


def send_navigation_command2(coordinate):
    if client.is_connected:
        talker.publish(roslibpy.Message(coordinate['coordinate']))
        print('Sending navigation2 command...')
        time.sleep(1)
    else:
        print("client未连接!")

    # talker.unadvertise()
    # client.terminate()
