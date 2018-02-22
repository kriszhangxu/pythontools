#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib
import json
import os

#导入的vertica_python和pykafka包需要pip install安装
from pykafka import KafkaClient  
#配置信息 host 多个用,分割
kfhostlist = "" 
kftopicname = ""
offsetfile = "./log/offset.txt"
pationnum = "2"

#将数据偏移量offset写入文件
def GetOffestInfo(offsetfile,pationnum = False):
    try:
        path_os = os.path.abspath( offsetfile ) 
        f1 = open(path_os, 'r' )
        offset = json.loads(f1.readline())  # 从a_offset_start开始读数据
        f1.close()
    except Exception,e:
        offset = {}
        if not partition or isinstance(pationnum,int) or 0>pationnum:
            pationnum = 1
        for i in range(0,pationnum):
            if i not in offset.has_key():
                offset[i] = 0
       
    return offset

def getDataByKafka():

    ret = {}
    
    #填写kafka地址和端口,一般是9092端口
    client = KafkaClient(hosts=kfhostlist) 
    
    #选择一个topic
    topic = client.topics[kftopicname]  
    
    #等待5秒无新数据,退出
    consumer = topic.get_simple_consumer(consumer_timeout_ms=2000, auto_commit_enable=1)  
    
    offsetlog = GetOffestInfo( offsetfile, pationnum )
    
    for message in consumer:  # 循环0
        c[str(message.partition_id)] = message.offset
        if offsetlog[str(message.partition_id)] < message.offset and message is not None:
            try:
                kcontent = urllib.unquote(message.value).decode('utf8')
                data = json.loads(kcontent)
                print data
            except Exception,e:
                print "错误---partition:"+str(message.partition_id)+",偏移量:"+str(message.offset)
                continue
    
    c1 = c
    f = open(offsetfile, 'w+' )
    f.truncate()
    f.write(json.dumps(c1))
    f.close()

if __name__ == "__main__":
    getDataByKafka()
