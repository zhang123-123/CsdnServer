#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from multiprocessing import cpu_count

bind = "0.0.0.0:8001"
daemon = True # 设置守护进程,将进程交给supervisor管理
# 并行工作进程数
workers = 2*cpu_count() + 1  # workers是工作线程数，一般设置成：2*服务器CPU个数 + 1，这样的话，在任何时候都有一半的worker在做IO
# 指定每个工作者的线程数
threads = 2
worker_class = "gevent"
forworded_allow_ips = '*'
keepalive = 6
timeout = 65
graceful_timeout = 10
# 设置最大并发量
worker_connections = 65535
# 设置进程文件目录
pidfile = '/www/DjangoPro/gunicorn.pid'
# 设置访问日志和错误信息日志路径
errorlog = '/www/DjangoPro/gunicorn.error.log'
accesslog = '/www/DjangoPro/gunicorn.access.log'
# 日志等级 
# debug    : 打印全部的日志(notset等同于debug)
# info     : 打印info,warning,error,critical级别的日志
# warning  : 打印warning,error,critical级别的日志
# error    : 打印error,critical级别的日志
# critical : 打印critical级别
loglevel = 'info'
proc_name = 'DjangoPro'