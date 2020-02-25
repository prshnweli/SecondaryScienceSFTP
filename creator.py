#imports
import pandas as pd
import pyodbc
import numpy as np
import csv

#Function to create files
def creator(sqlFile, csvFile):
    # connection
    conn = pyodbc.connect('Driver={SQL Server};'
    'Server=MHU-DBWH;'
    'Database=Aeries;'
    'Trusted_Connection=yes;')
    # start connection

    cursor = conn.cursor()

    file = open(sqlFile, 'r')
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
creator('HMHstudentUsers.sql', "HMHstudentUsers.csv")
creator('HMHclassassignmentStudents.sql', "HMHclassassignmentStudents.csv")

def editor(csvinput, csvoutput):
    file_name = csvinput
    file_name_output = csvoutput

    df = pd.read_csv(file_name, engine='python')
    df.drop_duplicates(subset=None, inplace=True)

# Write the results to a different file
    df.to_csv(file_name_output, index=False)
editor("HMHstudentUsers.csv", "my_file_without_dupes.csv")
editor("CLASS.csv", "CLASS_WITHOUT_DUPES.csv")

def merger():
    a = pd.read_csv('test1.csv')
    b = pd.read_csv('test2.csv')
    df = pd.concat([a,b])
    print(df)
    df.to_csv('test3.csv', index=False)
merger()
