# -*- coding: utf-8 -*-
##了解html的基本结构、解析方法、以及实现基本的网页爬取~
#html版本
'''
1. 改用pandas.io.json的json_normalize工具来格式化网站爬取的json数据
2. 使用pandas 中 Conncat工具来拼接前后两个番剧表

'''

import urllib,urllib2
import requests
import json
import re
import pandas as pd 
import numpy as np 
from pandas.io.json import json_normalize


def get_page(page):
    #参数
    base_url = "https://bangumi.bilibili.com/media/web_api/search/result?"
    headers = {
        'Host':'bangumi.bilibili.com',
        'Referer':'https://www.bilibili.com/anime/index/',
        'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'Origin': 'https://www.bilibili.com',
    }
    params = {
        'season_version':'-1',
        'area': '-1',
        'is_finish': '-1',
        'copyright': '-1',
        'season_status': '-1',
        'season_month':'-1',
        'pub_date': '-1',
        'style_id': '-1',
        'order': '3',
        'st': '1',
        'sort': '0',
        'page': page,
        'season_type':'1',
        'pagesize':'20'
        }
    url = base_url
    try:
        response = requests.get(url,headers=headers,params=params,allow_redirects=False)
        response.json()
        myjson = json.dumps(response.json(),ensure_ascii=False)
        newjson = json.loads(myjson)
        return newjson
    except urllib2.URLError as e:
        print('Error',e.args)


def parse_one_page(json):
    if json:
        items = json.get('result').get('data')
        items = json_normalize(items)
        web_data = pd.DataFrame(items)
    #print web_data
    return web_data

def main():
    for i in range(1,14):   
        if i == 1:
            global data
            data =  parse_one_page(get_page(i)) 
        else:
            data = pd.concat([data,parse_one_page(get_page(i))],ignore_index=True)
    pass #对data数据进行筛选，以及列的重命名，然后写入数据库
    print data

if __name__ == "__main__":
    print '开始运行'
    main()