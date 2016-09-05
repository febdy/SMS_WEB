import pymysql


def get_table_status(store_name):
    conn = pymysql.connect(host='175.126.112.111', user='root', password='dandy', db='TEST', charset='utf8')
    curs = conn.cursor()

    sql = "select * from TEST.table_info where store_name='"+store_name+"'"
    curs.execute(sql)
    results = curs.fetchall()

    for store in results:
        table_num = store[2]

    table_status = []

    for i in range(0, table_num):
        table_status.append(store[3+i])

    context = {'store_name': store_name, 'table_num': table_num,
               'table_status': table_status}

    return context

    conn.close()


def get_store_names():
    conn = pymysql.connect(host='175.126.112.111', user='root', password='dandy', db='TEST', charset='utf8')
    curs = conn.cursor()

    sql = "select * from TEST.test"
    curs.execute(sql)
    results = curs.fetchall()

    store_names = []

    for store in results:
        store_names.append(store[1])

    return store_names

    conn.close()


def get_store_info():
    conn = pymysql.connect(host='175.126.112.111', user='root', password='dandy', db='TEST', charset='utf8')
    curs = conn.cursor()

    sql = "select * from TEST.test"
    curs.execute(sql)
    results = curs.fetchall()

    store_info = []
    store_json = {}

    for store in results:
        store_json['store_name'] = store[1]
        store_json['latitude'] = store[2]
        store_json['longitude'] = store[3]
        store_info.append(store_json)
        store_json = {}

    return store_info

    conn.close()
