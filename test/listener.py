from __future__ import print_function
import roslibpy

# flag = True

# client = roslibpy.Ros(host='localhost', port=9090)
# client.run()

# listener = roslibpy.Topic(client, '/chatter', 'std_msgs/String')
# # listener.subscribe(lambda message: print('Heard talking: ' + message['data']))
# listener.subscribe(lambda message: testPrint(message))

# def testPrint(message):
#   global flag
#   print('Heard talking: ' + message['data'])
#   if client.is_connected:
#     print("client已经连接")
#     client.close()
#     print("client已经关闭")
#     flag = False

# while flag:
#   pass

# print("监听结束")

# from __future__ import print_function
# import roslibpy

# client = roslibpy.Ros(host='localhost', port=9090)
# client.run()

# listener = roslibpy.Topic(client, '/chatter', 'std_msgs/String')
# # listener.subscribe(lambda message: print('Heard talking: ' + message['data']))
# listener.subscribe(lambda message: testPrint(message))

# def testPrint(message):
#   print('Heard talking: ' + message['data'])

# try:
#   while True:
#     pass
# except KeyboardInterrupt:
#   client.terminate()

#   print("监听结束")
