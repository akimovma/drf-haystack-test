proc_name = 'test_admin'
bind = '127.0.0.1:8001'
workers = 3
user = 'user'
chdir = '/home/user/Projects/test_admin/test_admin/'
loglevel = 'debug'
errorlog = '/home/user/Projects/test_admin/logs/gunicorn.error.log'
accesslog = '/home/user/Projects/test_admin/logs/gunicorn.access.log'