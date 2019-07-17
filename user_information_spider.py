'''
爬取哔哩哔哩个人用户的追番信息

'''


#先将两个ID取出来，判断是否有重复

import pandas as pd 
import numpy as np 
import requests
from pandas.io.json import json_normalize


# data = pd.read_csv('data_test.csv')
#data = data[['media_id','season_id']]

# data_media_id = data.sort_values('media_id',inplace = False)
# data_media_id = data_media_id.reset_index(drop=True)   #依然要区分返回型功能函数和操作自身型的功能函数

# print data


# data_media_id = data_media_id.drop_duplicates(subset = 'season_id')
# print data_media_id

#numpy型数组在处理数据方面的优势？？

# n_data = data.as_matrix(['season_id'])
# n_data = n_data.T
# n_data = np.sort(n_data)
# n_data = n_data[0]
# n_data_size = n_data.size
# print n_data
# print n_data[0]
# print n_data_size

