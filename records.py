
import pymysql

print("Mysql Results")

conn = pymysql.connect(host = "127.0.0.1"
    , user = "root", passwd = "", db="testing"
    , cursorclass=pymysql.cursors.DictCursor) # parser JSON
cur = conn.cursor()
cur.execute("SELECT * FROM posts")
for item in cur.fetchall():
    print(item)

conn.close()