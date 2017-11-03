#!/usr/bin/python
import redis
import os
import sys

count_file = '/tmp/redis_qps.txt'
r = redis.StrictRedis(host='10.14.12.24', port=6379, password='123456')

info = r.info()
def total_commands_processed():
    now_count = info['total_commands_processed']

    if not os.path.exists(count_file):
        with open(count_file, 'w') as f:
            f.write(str(now_count))
        old_count = now_count
    else:
        with open(count_file,'r') as f:
            old_count = f.read()

    with open(count_file,'w') as f:
        f.write(str(now_count))

    print ( int(now_count) - int(old_count) ) / 60


if str(sys.argv[1]) == 'total_commands_processed':
    total_commands_processed
elif str(sys.argv[1]) == 'master_link_status':
    if str(info['master_link_status']) == "up":
        print 0
    else:
        print 1