import constants
import mysql.connector
import timeit
import pandas as pd
from mysql.connector import errorcode

def insert_benchmark(batch_sizes: list, cursor):
    for size in batch_sizes:
        print("---------------TIME CALCULATION---------------")
        print("---------------TIME CALCULATION---------------", file=f)

        print(f"Batch size {size}")
        print(f"Batch size {size}", file=f)

        cursor.execute("DROP TABLE IF EXISTS students")
        cursor.execute(constants.table)

        total = 0
        batch_count = 0
        count = 0
        rows = []
        studentsData = pd.read_csv("fr-esr-atlas_regional-effectifs-d-etudiants-inscrits.csv", sep=';')
        studentsData = studentsData.fillna(0)

        start = timeit.default_timer()

        for i, row in studentsData.iterrows():
            if count >= size:
                total += count
                batch_count += 1
                sql = "INSERT INTO students VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.executemany(sql, rows)
                cnx.commit()
                rows = []
                count = 0

            rows.append(tuple(row))
            count += 1

        if len(rows) > 0:
            total += count
            batch_count += 1
            sql = "INSERT INTO students VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.executemany(sql, rows)
            cnx.commit()
            rows = []
        end = timeit.default_timer()
        
        print(f"Time to insert {total} row into students table with a batch size equal to {size} : {end - start}")
        print(f"Time to insert {total} row into students table with a batch size equal to {size} : {end - start}", file=f)
    
               

if __name__ == '__main__':
    try:
        file_path = '../results/mysql/insert_by_batch_tests.txt'
        f = open(file_path, "a")
        cnx = mysql.connector.connect(**constants.config)

        if cnx.is_connected():
            cursor = cnx.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            print("You're connected to database: ", record, file=f)

            a = 100
            length = 9
            r = 2
            batch_sizes = [a * r ** (n - 1) for n in range(1, length + 1)]

            insert_benchmark(batch_sizes=batch_sizes, cursor=cursor)

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
        