import requests


PROXY_POOL_URL = 'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=947cd405faaa4dcc9c34dc57029abb83&orderno=YZ201972002405khONp&returnType=2&count=1' #云端的代理池

def get_proxy():
    '''
    从云端的代理池获取有用ip,并进行可用性验证
    '''
    # usable_flag = 0
    # while(usable_flag == 0):
    #     response = requests.get(PROXY_POOL_URL)
    #     if response.status_code == 200:
    #         return response.text
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            a = response.json().get("RESULT")[0].get("ip")
            b =  response.json().get("RESULT")[0].get("port")
            return a+':'+b
    except ReferenceError as e:
        print('Error',e.args)

print get_proxy()