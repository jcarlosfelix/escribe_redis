# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:57:41 2020

@author: jcarl
"""


import redis
import os
import time


r = redis.StrictRedis(host=os.environ['REDIS_HOST'], port=6379, db=0)

redis_ready = False

while not redis_ready:
    try:
        redis_ready = r.ping()
    except:
        print("waiting for redis")
        time.sleep(3)
        
print("setup:redis alive")


i = 0
while True:
    r.rpush('cola_de_mensajes', i)  #empuja un valor por la derecha right push
    print(i)
    i+=1
    time.sleep(3)