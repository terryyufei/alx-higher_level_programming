#!/usr/bin/python3

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    my_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3], port=3306)
    my_cursor = my_db.cursor()

    my_cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")

    my_data = my_cursor.fetchall()

    for data in my_data:
        print(data)

    # Close all cursors
    my_cursor.close()

    # Close all databases
    my_db.close()
