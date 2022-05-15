import constants
import mysql.connector
import timeit
from mysql.connector import errorcode

if __name__ == '__main__':
    try:
        cnx = mysql.connector.connect(**constants.config)

        if cnx.is_connected():
            file_path = '../results/mysql/select_tests.txt'
            f = open(file_path, "a")

            cursor = cnx.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            print("You're connected to database: ", record, file=f)
            
            a = 100
            length = 9
            r = 2
            query_numbers = [a * r ** (n - 1) for n in range(1, length + 1)]

            for query_number in query_numbers:
                print("---------------TIME CALCULATION---------------")
                print("---------------TIME CALCULATION---------------", file=f)

                print(f"Query number {query_number}")
                print(f"Query number {query_number}", file=f)

                sql = "SELECT BENCHMARK(%s,\"SELECT * FROM students WHERE sexe=%s AND unite_geographique=%s\")"
                start = timeit.default_timer()
                tuple = (query_number, 2, 'Caen')
                cursor.execute(sql, tuple)
                end = timeit.default_timer()
                records = cursor.fetchall()
                print(f"Time to select All female students who lives in Caen from students table with a number of paralel query equal to {query_number} : {end - start}")
                print(f"Time to select All female students who lives in Caen from students table with a number of paralel query equal to {query_number} : {end - start}", file=f)

            cursor.close()
            cnx.close()
            print("----------------------------------------------")
            print("----------------------------------------------", file=f)
            print("MySQL connection is closed")
            print("MySQL connection is closed", file=f)
            f.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)