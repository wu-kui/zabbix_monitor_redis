#!/usr/bin/python
# coding: utf-8
import redis
import hashlib
import time

log_file='test.log'

def md5():
    date = time.time()
    m=hashlib.md5()
    m.update(str(date))
    return m.hexdigest()


# 获取当下时间
def now():
    # 时间格式
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    return time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ))

#  记录日志的函数
def write_logs(body):
    with open(log_file, 'a') as f:
        datetime = now()
        logs = '[ ' + datetime + ' ]: ' + str(body)  + '\n'
        f.write(logs)


if __name__ == "__main__":
    try:

        while True:

            r = redis.StrictRedis(host='172.16.10.40', port=6381, password='12345')
            key = md5()

            begin_time = time.time()
            r.set('wukui', key)
            a = r.get('wukui')
            end_time = time.time()

            user_time = end_time - begin_time
            write_logs(str(user_time)[0:5])
            time.sleep(1)
    except:
        pass

