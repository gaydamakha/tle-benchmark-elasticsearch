import constants

import mysql.connector
import pandas as pd
from mysql.connector import errorcode

if __name__ == '__main__':
    try:
        studentsData = pd.read_csv("fr-esr-atlas_regional-effectifs-d-etudiants-inscrits.csv", sep=';')
        studentsData = studentsData.fillna(0)
        print(studentsData.shape[0])
        cnx = mysql.connector.connect(**constants.config)

        if cnx.is_connected():
            cursor = cnx.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

            print("Creating students table....")
            cursor.execute("DROP TABLE IF EXISTS students;")
            cursor.execute(constants.table)
            print("Students table created")

            print("---------------INSERT DATA---------------")
            print("Inserting data into students table....")
            # batch_size = 100
            for i,row in studentsData.iterrows():
                sql = "INSERT INTO students VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, tuple(row))
                print(i," Record inserted")
                cnx.commit()
            print("Data inserted into students table")

            cursor.close()
            cnx.close()
            print("MySQL connection is closed")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        