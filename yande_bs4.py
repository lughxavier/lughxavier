#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
from bs4 import BeautifulSoup
import requests , urllib.request,time

for page in range(1,25):
    path = 'https://yande.re/post?page={}&tags=misaki_kurehito'.format(page) #页码

    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    date = requests.get(path,headers = header)#请求
    soup = BeautifulSoup(date.text, 'lxml')#解析
    time.sleep(3)#间隔3s一次请求
    downfile = 'F://QQdown/misaki/'

    L = []
    imgs = soup.select('a.directlink.largeimg')#大图
    for i in imgs:
        pic = i['href']#只要链接
        L.append(pic)
    
    for d in L:
        urllib.request.urlretrieve(d, downfile + d[-10:])#名字保留链接后10位
        print('Done')    
#  '''
#  导入库
#  写好伪装
#  请求
#  对请求数据解析
#  对解析的数据筛选（路径或元素唯一属性），多个数据可以用字典（字典不能切片）
# '''
