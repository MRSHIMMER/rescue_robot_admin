import time
import roslibpy

client = roslibpy.Ros(host='localhost', port=9090)
client.run()

talker = roslibpy.Topic(client, '/chatter', 'std_msgs/String')


def send_patrol_command():
  if client.is_connected:
    talker.publish(roslibpy.Message({'data': 'patrol'}))
    print('Sending message...')
    time.sleep(1)
  else:
    print("client未连接!")

  talker.unadvertise()
  client.close()