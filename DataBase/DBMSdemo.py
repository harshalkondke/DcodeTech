try:
    import pymysql

    database = pymysql.connect(host="localhost", user="root", passwd="Pass@123")

    cursor = database.cursor()
    cursor.execute("create database college")

    for databases in cursor:
        print(databases)
except pymysql.err.ProgrammingError:
    print("Boom... Already created.")

finally:
    print("macha raha hai bhai")