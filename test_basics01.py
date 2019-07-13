#了解html的基本结构、解析方法、以及实现基本的网页爬取~
'''
1.网站的基本结构：（chrome的基本使用方法）

2.需要用到的库：

3.开始实践吧

'''
#conding = utf-8
import urllib,urllib2


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
    url = base_url + urllib.urlencode(params)
    try:
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request)
        #将内容解析为json格式返回
        return response.read()
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