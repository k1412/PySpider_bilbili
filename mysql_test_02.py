'''
远端数据库的链接和数据读取
重新练习  连续分批从网站爬取数据并存入数据库
'''


import pymysql
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd 
import numpy as np
from pandas.io.json import json_normalize
import json
import requests


#读取练习：

connect_info = 'mysql+pymysql://wy-remote:dovewyjzrn123@www.k1412.top:3306/spiders_test?charset=utf8'
engine = create_engine(connect_info)
data = pd.read_sql_table(table_name= 'test1',con = engine)
print data
data.to_csv('mysql_read_test.csv',encoding='utf-8',index=False)
