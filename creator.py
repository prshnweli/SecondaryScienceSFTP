#imports
import pandas as pd
import pyodbc
import numpy as np
import csv
import config

#Function to create files
def creator(sqlFile, csvFile):
    # connection
    conn = pyodbc.connect('Driver={SQL Server};'
    'Server='+config.Server+';'
    'Database='+config.Database+';'
    'UID='+config.UID+';'
    'PWD='+config.PWD+';'
    )
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
creator('sql/HMHstudentUsers.sql', "students/studentUsers.csv")
creator('sql/HMHclassassignmentStudents.sql', "students/classassignmentStudents.csv")

def editor(csvinput, csvoutput):
    file_name = csvinput
    file_name_output = csvoutput

    df = pd.read_csv(file_name, engine='python')
    df.drop_duplicates(subset=None, inplace=True)

# Write the results to a different file
    df.to_csv(file_name_output, index=False)
editor("students/studentUsers.csv", 'students/updatedUsers.csv')
editor("students/classassignmentStudents.csv", 'students/updatedClassAssignment.csv')

def merger(filea, fileb, filec):
    a = pd.read_csv(filea)
    b = pd.read_csv(fileb)
    c = pd.concat([a,b])
    #print(c)
    c.to_csv(filec, index=False)

merger('teachers/CLASSASSIGNMENT.csv', 'students/updatedClassAssignment.csv', 'hmh/CLASSASSIGNMENT.csv')
merger('teachers/USERS.csv', 'students/updatedUsers.csv', 'hmh/USERS.csv')

# def murphyedit():
#     df = pd.read_csv('hmh/CLASSASSIGNMENT.csv', engine='python')
#     df.loc[df["CLASSLOCALID"]=="1120_21", "CLASSLOCALID"] = 1119_21
#     df.to_csv("test.csv", index = False)
