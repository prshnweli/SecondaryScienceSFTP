#imports
import pandas as pd
import pyodbc
import numpy as np
import csv

#Function to create files
#scCMD: school additional sql command
def creator(csvFile):
    # connection
    conn = pyodbc.connect('Driver={SQL Server};'
    'Server=MHU-DBWH;'
    'Database=Aeries;'
    'Trusted_Connection=yes;')
    # start connection

    cursor = conn.cursor()

    file = open('HMHstudentUsers.sql', 'r')
    sqlFile = file.read()
    file.close()

    cursor.execute(sqlFile)
    data = cursor.fetchall()

    with open(csvFile, 'w', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerow([column[0] for column in cursor.description])
        for line in data:
            a.writerow(line)

    cursor.close()
    conn.close()

    # edit csv
    # df = pd.read_csv(csvFile, encoding = "ISO-8859-1")
creator("HMHstudentUsers.csv")
