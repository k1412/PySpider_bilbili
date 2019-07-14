# -*- coding: utf-8 -*-
##了解html的基本结构、解析方法、以及实现基本的网页爬取~
#html版本
'''
1.网站的基本结构：（chrome的基本使用方法）

2.需要用到的库：

3.开始实践吧

'''

import urllib,urllib2
import requests
import json
import re
import pandas as pd 
import numpy as np 

base_url = "https://bangumi.bilibili.com/media/web_api/search/result?"

headers = {
     'Host':'bangumi.bilibili.com',
     'Referer':'https://www.bilibili.com/anime/index/',
     'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
     'Origin': 'https://www.bilibili.com',
}

def get_page(page):
    #参数
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

# def parse_one_page(html):
#     # pattern_title = re.compile('"title":"(.*?)"',re.S)
#     # result = re.findall(pattern_title,html)
#     # return result
def parse_one_page(json):
    if json:
        items = json.get('result').get('data')
        web_data = pd.DataFrame(items)
        web_data2 = web_data[['title','media_id','season_id','order']]
        web_data3 = web_data[['order']]
        # index = 0
        # for item in items:
        #     web_data3 = pd.DataFrame(item['order'])
            # ret[1] = item['season_id']
            # ret[2] = item['media_id']
    return web_data2

print '中文'
print parse_one_page(get_page(1))