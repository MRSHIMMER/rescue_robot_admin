# resuce_robot_admin
rescue_robot_admin
本地
flask run

服务器
gunicorn -w 5 -b :5000 --reload app:app
关闭服务器
pstree -ap|grep gunicorn
kill -9 pid
