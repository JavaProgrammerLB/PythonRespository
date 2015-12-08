import pymysql.cursors
import Columns

def main():
    list1 = getColumnsByTableSchema('serverdata')
    list2 = getColumnsByTableSchema('semsserverdata')
    print(list1)


def getColumnsByTableSchema(s):
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
            # Read all record
            sql = "SELECT * FROM `columns` WHERE `table_schema`=%s"
            cursor.execute(sql, (s,))
            result = cursor.fetchall()
            # print(result)
            # print('resulte的type',type(result))
            # print('result的长度{}'.format(len(result)))
            l = handleList(result)
            print(l)
    finally:
        connection.close()

def handleList(aList):
    l = list()
    for i in range(len(aList)):
        d = aList[i]
        tableCatlog = d['TABLE_CATALOG']
        tableSchema = d['TABLE_SCHEMA']
        tableName = d['TABLE_NAME']
        columnName = d['COLUMN_NAME']
        ordinalPosition = d['ORDINAL_POSITION']
        columnDefault = d['COLUMN_DEFAULT']
        isNullable = d['IS_NULLABLE']
        dataType = d['DATA_TYPE']
        characterMaximumLength = d['CHARACTER_MAXIMUM_LENGTH']
        characterOcterLength = d['CHARACTER_OCTET_LENGTH']
        numericPrecision = d['NUMERIC_PRECISION']
        numericScale = d['NUMERIC_SCALE']
        characterSetName = d['CHARACTER_SET_NAME']
        collationName = d['COLLATION_NAME']
        columnType = d['COLUMN_TYPE']
        columnKey = d['COLUMN_KEY']
        extra = d['EXTRA']
        privileges = d['PRIVILEGES']
        columnComment = d['COLUMN_COMMENT']

        c = Columns(tableCatlog,tableSchema,tableName,columnName,ordinalPosition,columnDefault,isNullable,dataType,characterMaximumLength,characterOcterLength,numericPrecision,numericScale,characterSetName,collationName,columnType,columnKey,extra,privileges,columnComment)
        l.append(c)
    else:
        return l

if __name__ == '__main__':
    main()
