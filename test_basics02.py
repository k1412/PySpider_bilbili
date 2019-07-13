#了解html的基本结构、解析方法、以及实现基本的网页爬取~
'''
1.网站的基本结构：（chrome的基本使用方法）

2.需要用到的库：

3.开始实践吧

'''
#conding = utf-8
import urllib,urllib2
import requests
import json
import re

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
    #url = base_url + urllib.urlencode(params)
    url = base_url
    try:
        # request = urllib2.Request(url,headers=headers)
        response = requests.get(url,headers=headers,params=params,allow_redirects=False)
        #将内容解析为json格式返回
        # myjson = json.loads(response.json())
        # newjson = json.dumps(myjson,ensure_ascii=False)
        # return newjson
        # response.encoding = "utf-8"
        # myjson = json.loads(response.json(),encoding='utf-8')
        newjson = json.dumps(response.json(),ensure_ascii=False)#使json中的中文可以正确的显示,但返回的是一个str格式的数据
        # myjson = json.loads(newjson,encoding='utf-8')
        result = re.findall('"title": "(.*?)"',newjson,re.S)
        return result
        # return response.text
        # return response.status_code
        # return response.cookies
    except urllib2.URLError as e:
        print('Error',e.args)


# response = urllib.urlopen('https://cuiqingcai.com/947.html')
print '中文'
# print response.read()
# print type(response)
# request = urllib2.Request('https://cuiqingcai.com/947.html')
# response2 = urllib2.urlopen(request)
# print response2.read()


print get_page(1)