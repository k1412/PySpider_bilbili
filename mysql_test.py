#新建一个spiders数据库，并创建一个学生数据的数据表：：

# import pymysql

# db = pymysql.connect(host= 'www.k1412.top',user= 'wy-remote', password= 'dovewyjzrn123',port= 3306)
# cursor = db.cursor()
# cursor.execute("CREATE DATABASE spiders_test DEFAULT CHARACTER SET utf8")
# db.close()
import pymysql

db = pymysql.connect(host= 'www.k1412.top',user= 'wy-remote', password= 'dovewyjzrn123',port= 3306,db= 'spiders_test')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,age INT NOT NULL,PRIMARY KEY (id))'
cursor.execute(sql)
db.close()