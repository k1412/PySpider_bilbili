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
import anime_index

def get_page(vmid,ps,page=1):
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
        'pn': page,
        'ps': ps,
        'vmid': vmid,
        }
    url = base_url
    try:
        response = requests.get(url,headers=headers,params=params)
        response.json()
        return response.json()
    except ReferenceError as e:
        print('Error',e.args)

def get_size_code(vmid):
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
        code = response.json().get('code')
        if code == 0:
            size = response.json().get('data').get('total')
            return size,code
        else : return 0,code
    except ReferenceError as e:
        print('Error',e.args)

def parse_one_page(json):
    if json:
        items = json.get('data').get('list')
        items = json_normalize(items)
        web_data = pd.DataFrame(items)
        web_data = web_data[['season_id']]
        web_data.to_csv('data_test_100.csv',encoding= 'utf-8')
        web_data = web_data.to_numpy()
        web_data = web_data.T 
        web_data = web_data[0]
    return web_data

def user_information_spider():
    #for vmid in range(1,400000000):
    generate_pd_flag = 1
    for vmid in range(1,10):
        total,code = get_size_code(vmid)
        # useful_vmid
        size = total
        #如果存在：
        if total!=0 and code == 0:
            single_data = np.zeros(2903, dtype=bool)
            #处理单个页面代码
            #保留两份文件，一份的pd id+列表 ，一份是nunpy数组 只有列表数据
            page = 1
            while(total>0):
                web_source_data = get_page(vmid,50,page)
                if page == 1:
                    global web_data
                    web_data = parse_one_page(web_source_data)
                else :
                    web_data = np.append(web_data,parse_one_page(web_source_data))
                page+=1
                total-=50
            #对单个有意义数据的处理：
            for iteam in web_data :
                if anime_index.has_anime_index(iteam):
                    id_index = anime_index.anime_index(iteam)
                    single_data[id_index] = True
            if generate_pd_flag == 1:
                global anime_list
                anime_list = pd.DataFrame(single_data).T
                generate_pd_flag = 0
            else:
                anime_list_new = pd.DataFrame(single_data).T
                anime_list = pd.concat([anime_list,anime_list_new],ignore_index=True)
            np.savetxt('boolData.csv',single_data,delimiter = ',')
    print anime_list

user_information_spider()
'''
还需要完成的工作：
1. 如何构造用户VMID???
2. 判断并跳过无效的爬取？？？？
3. 选取读取成功的爬取。。。

"total":0 时，所爬取的用户没有追番信息？？？？？

爬取到的信息如何保存？？
p. numpy数组？？？
1. 构造稀疏数组
2. 上传

'''