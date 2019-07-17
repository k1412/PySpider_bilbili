'''
爬取哔哩哔哩个人用户的追番信息

已经实现了爬取特定ID用户的追番信息---单个
还需要把他转化为一个一位的布尔值
'''

import pandas as pd 
import numpy as np 
import requests
from pandas.io.json import json_normalize
import json

def get_page(vmid,ps):
    #参数
    base_url = "https://api.bilibili.com/x/space/bangumi/follow/list?"
    headers = {
        'Host':'api.bilibili.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Origin': 'https://space.bilibili.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
    }
    params = {
        'type':'1',
        'follow_status': '0',
        'pn': '1',
        'ps': ps,
        'vmid': vmid,
        }
    url = base_url
    try:
        response = requests.get(url,headers=headers,params=params)
        response.json()
        myjson = json.dumps(response.json(),ensure_ascii=False)
        newjson = json.loads(myjson)
        return newjson
    except ReferenceError as e:
        print('Error',e.args)

def get_size(vmid):
    #参数
    base_url = "https://api.bilibili.com/x/space/bangumi/follow/list?"
    headers = {
        'Host':'api.bilibili.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Origin': 'https://space.bilibili.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
    }
    params = {
        'type':'1',
        'follow_status': '0',
        'pn': '1',
        'ps': '15',
        'vmid': vmid,
        }
    url = base_url
    try:
        response = requests.get(url,headers=headers,params=params)
        size = response.json().get('data').get('total')
        return size
    except ReferenceError as e:
        print('Error',e.args)

def parse_one_page(json):
    if json:
        items = json.get('data').get('list')
        items = json_normalize(items)
        web_data = pd.DataFrame(items)
    return web_data

size = get_size(786151)
web_data = parse_one_page(get_page(786151,size))
web_data = web_data[['season_id']]
web_data.to_csv('data_test_100.csv',encoding= 'utf-8')
web_data = web_data.to_numpy()
web_data = web_data.T 
web_data = web_data[0]
web_data_size = web_data.size

print web_data
print web_data_size


'''
还需要完成的工作：
1. 如何构造用户VMID???
2. 判断并跳过无效的爬取？？？？
3. 选取读取成功的爬取。。。

"total":0 时，所爬取的用户没有追番信息？？？？？
