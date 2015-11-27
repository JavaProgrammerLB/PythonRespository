import pymysql.cursors

def main():
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='information_schema',
                                 port=3400,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = 'SELECT DISTINCT table_name FROM COLUMNS WHERE TABLE_SCHEMA = \'serverdata\''
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)

    finally:
        connection.close()

def handleMap(map):


if __name__ == '__main__':
    main()
