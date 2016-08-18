import pymysql

conn = pymysql.connect(host='175.126.112.111', user='root', password='dandy', db='TEST', charset='utf8')
curs = conn.cursor()

sql = "select * from TEST.table_info where store_name='숭실대입구'"

curs.execute(sql)
results = curs.fetchall()

for store in results:
    store_name = store[1]
    table_num = store[3]

table_status = []

for i in range(0, table_num):
    table_status.append(store[4+i])

conn.close()
