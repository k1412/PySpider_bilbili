'''
还需要完成的工作：
使用代理池，爬取一定数量的网页后，更换代理IP

判断爬取失败的标志？？？相应时间怎么算？？

爬取一定次数后，将数据保存到数据库
捷键代理池中代理检测的一些方法
'''
import pymysql
import pandas as pd 
import numpy as np 
import requests
from pandas.io.json import json_normalize
import json
import anime_index
from sqlalchemy import create_engine
import sqlalchemy

#数据库连接初始化
connect_info = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format("wy-remote", "dovewyjzrn123", "www.k1412.top", "3306", "spiders_test")
engine = create_engine(connect_info)

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
        #web_data = web_data.to_numpy()
        web_data = web_data.T 
        web_data = web_data[0]
    return web_data

def user_information_spider():
    #for vmid in range(1,400000000):
    generate_pd_flag = 1
    useful_num = 0
    for vmid in range(1,100):
        total,code = get_size_code(vmid)
        # useful_vmid
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
            useful_num+=1
            if useful_num == 10:
                break   
    print anime_list,useful_num
    # #原本计划将结果转换为数组然后传入数据库看来是不可以啊
    # anime_list.to_sql(
    #     name = 'test8',
    #     con = engine,
    #     if_exists = 'append',
    #     index= False
    # )

user_information_spider()
