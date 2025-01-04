from dataclasses import dataclass
import pandas as pd
import mysql.connector

dataBase = mysql.connector.connect(
    host="sql5.freemysqlhosting.net",
    user="sql5744928",
    passwd="wCBdQqsKCG",
    database="sql5744928"
)

# preparing a cursor object
cursor = dataBase.cursor()

needed_columns = [
    'Year', 'User', 'School', 'Grade', 'Subject', 'Course',
    'StartDate', 'EndDate', 'Unit', 'Category', 'Text'
]

courses = pd.read_csv(
    "Seven Hills Clean.csv",
    encoding="Windows-1252",
    low_memory=False,
    usecols=needed_columns
)

# Rename columns to match dataclass fields
courses.rename(columns={
    'User': 'AuthorizedViewers',
    'Text': 'Description'
}, inplace=True)

#print(courses.head(10))

@dataclass
class Course:
    Year: str
    AuthorizedViewers: str
    School: str
    Grade: str
    Subject: str
    Course: str
    StartDate: int
    EndDate: int
    Unit: int
    Category: str
    Description: str

    @classmethod
    def fromRow(cls, row):
        data = row.to_dict()
        return cls(**data)

courseObjects = [Course.fromRow(row) for idx, row in courses.head(1000).iterrows()]

for i, obj in enumerate(courseObjects):
    if obj.Course == courseObjects[i-1].Course:
        continue
    print(obj.Course + "\t\t" + courseObjects[i-1].Course)
    cursor.execute('''
    INSERT INTO CourseInfo (courseName,subjectID,year,grade,divisionID) VALUES (%s, %s, %s, %s, %s)
    ''', (obj.Course, 1, 2023, obj.Grade, 1))

dataBase.commit()

# cursor.execute('SELECT * FROM CourseInfo')
# results = cursor.fetchall()
# for row in results:
#     print(row)

dataBase.close()