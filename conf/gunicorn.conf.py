proc_name = 'test_admin'
bind = '172.16.101.186:8000'
workers = 3
user = 'user'
chdir = '/home/user/Projects/test_admin/test_admin/'
loglevel = 'debug'
errorlog = '/home/user/Projects/test_admin/logs/gunicorn.error.log'
accesslog = '/home/user/Projects/test_admin/logs/gunicorn.access.log'