import pymysql


def get_table_status(storename):
    conn = pymysql.connect(host='175.126.112.111', user='root', password='dandy', db='TEST', charset='utf8')
    curs = conn.cursor()

    sql = "select * from TEST.table_info where store_name='"+storename+"'"
    curs.execute(sql)
    results = curs.fetchall()

    for store in results:
        store_name = store[1]
        table_num = store[3]

    table_status = []

    for i in range(0, table_num):
        table_status.append(store[4+i])

    context = {'store_name': store_name, 'table_num': table_num,
               'table_status': table_status}

    return context

    conn.close()


def get_store_names():
    conn = pymysql.connect(host='175.126.112.111', user='root', password='dandy', db='TEST', charset='utf8')
    curs = conn.cursor()

    sql = "select * from TEST.table_info"
    curs.execute(sql)
    results = curs.fetchall()

    store_names = []

    for store in results:
        store_names.append(store[1])

    return store_names

    conn.close()
