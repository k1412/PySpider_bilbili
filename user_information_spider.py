'''
爬取哔哩哔哩个人用户的追番信息

'''


#先将两个ID取出来，判断是否有重复

import pandas as pd 
import numpy as np 


data = pd.read_csv('data_test.csv')
data = data[['media_id','season_id']]

data_media_id = data.sort_values('media_id',inplace = False)
data_media_id = data_media_id.reset_index(drop=True)   #依然要区分返回型功能函数和操作自身型的功能函数

print data


data_media_id = data_media_id.drop_duplicates(subset = 'season_id')
print data_media_id