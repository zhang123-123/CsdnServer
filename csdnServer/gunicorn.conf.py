#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from multiprocessing import cpu_count

bind = "0.0.0.0:8001"
daemon = True # �����ػ�����,�����̽���supervisor����
# ���й���������
workers = 2*cpu_count() + 1  # workers�ǹ����߳�����һ�����óɣ�2*������CPU���� + 1�������Ļ������κ�ʱ����һ���worker����IO
# ָ��ÿ�������ߵ��߳���
threads = 2
worker_class = "gevent"
forworded_allow_ips = '*'
keepalive = 6
timeout = 65
graceful_timeout = 10
# ������󲢷���
worker_connections = 65535
# ���ý����ļ�Ŀ¼
pidfile = '/www/DjangoPro/gunicorn.pid'
# ���÷�����־�ʹ�����Ϣ��־·��
errorlog = '/www/DjangoPro/gunicorn.error.log'
accesslog = '/www/DjangoPro/gunicorn.access.log'
# ��־�ȼ� 
# debug    : ��ӡȫ������־(notset��ͬ��debug)
# info     : ��ӡinfo,warning,error,critical�������־
# warning  : ��ӡwarning,error,critical�������־
# error    : ��ӡerror,critical�������־
# critical : ��ӡcritical����
loglevel = 'info'
proc_name = 'DjangoPro'