'''
链接数据库，联系数据库的使用
爬取番剧的类别信息
尝试爬一页个人数据
'''

#练习数据库的使用
import pymysql

db = pymysql.connect(host= 'www.k1412.top',user= 'wy-remote',password= 'dovewyjzrn123',port= 3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:',data)
db.close()