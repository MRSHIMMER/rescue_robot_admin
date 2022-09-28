import time
import roslibpy

# from rospy_message_converter import message_converter
from std_msgs.msg import String

client = roslibpy.Ros(host='localhost', port=9090)
client.run()

spark_command_talker = roslibpy.Topic(client, '/command2spark', 'std_msgs/String')
admin_command_talker = roslibpy.Topic(client, '/command2admin', 'std_msgs/String')
add_item_command_talker = roslibpy.Topic(client, '/web/sparkenv', 'std_msgs/String')


def send_command_to_spark(req):
    if client.is_connected:
        spark_command_talker.publish(roslibpy.Message({"data": str(req)}))
        print('Sending message to robot...')
        time.sleep(1)
    else:
        print("client未连接!")


def send_command_to_admin(req):
    if client.is_connected:
        admin_command_talker.publish(roslibpy.Message({"data": str(req)}))
        print('Sending message to admin...')
        time.sleep(1)
    else:
        print("client未连接!")


def add_test_item_to_admin(req):
    if client.is_connected:
        add_item_command_talker.publish(roslibpy.Message({"data": str(req)}))
        print('Add test item to admin...')
        time.sleep(1)
    else:
        print("client未连接!")
