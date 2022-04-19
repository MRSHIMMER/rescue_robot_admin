# resuce_robot_admin
rescue_robot_admin

两种运行方式

1. flask内置服务器运行
flask run

2. gunicorn服务器运行
gunicorn -w 5 -b :5000 --reload app:app
关闭服务器
pstree -ap|grep gunicorn
kill -9 pid
