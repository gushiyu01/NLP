import MySQLdb


def get_mysql_connection_cursor():
    conn = MySQLdb.connect(
        db='lj6',
        host='10.61.2.172',
        user='root',
        password='lj123456',
        charset='utf8'
    )

    return conn.cursor()

