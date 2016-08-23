import pymysql


def set_table_status(store_name, table_number, set_status):

    conn = pymysql.connect(host='175.126.112.111', user='root', password='dandy', db='TEST', charset='utf8')
    curs = conn.cursor()

    sql = "update TEST.table_info set %s=%s where store_name='%s'" % (table_number, set_status, store_name)

    curs.execute(sql)
    conn.commit()

    return True

    conn.close()

