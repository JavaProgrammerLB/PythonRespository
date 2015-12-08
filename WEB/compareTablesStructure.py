import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='information_schema',
                             port=3400,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    #with connection.cursor() as cursor:
        # Create a new record
        #sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        #cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    #connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `users` WHERE `name`=%s"
        cursor.execute(sql, ('admin',))
        result = cursor.fetchone()
        print(result)
        print('resulte的type',type(result))
        print('result的长度{}'.format(len(result)))
finally:
    connection.close()
