#!/usr/bin/python
import redis
import os

count_file = '/var/log/zabbix/redis_qps.txt'
r = redis.StrictRedis(host='10.14.12.24', port=6379, password='123456')

info = r.info()
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

#print 'old_count' + '  ' + str(old_count)
#print 'now_count' + '  ' + str(now_count)

print int(now_count) - int(old_count)