#!/usr/bin/python3

"""
Module that connects python script to a database
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # connect the db using command-line arguments
    my_db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3]
    )

    # create the cusror && execute the query
    my_cursor = my_db.cursor()
    my_cursor.execute(
        """SELECT * FROM states WHERE name LIKE
        BINARY 'N%'ORDER BY states.id ASC
        """
        )

    # fetch the data queried
    my_data = my_cursor.fetchall()

    # iterate to print a tuple
    for data in my_data:
        print(data)

    # Close all cursors
    my_cursor.close()

    # Close all databases
    my_db.close()
