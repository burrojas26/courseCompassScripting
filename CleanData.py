from dataclasses import dataclass
import pandas as pd
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

needed_columns = [
    'Year', 'User', 'School', 'Grade', 'Subject', 'Course',
    'StartDate', 'EndDate', 'Unit', 'Category', 'Text'
]

courses = pd.read_csv(
    "Seven Hills Export.csv",
    encoding="Windows-1252",
    low_memory=False,
    usecols=needed_columns
)

# Rename columns to match dataclass fields
courses.rename(columns={
    'User': 'AuthorizedViewers',
    'Text': 'Description'
}, inplace=True)

print(courses.head(10))

@dataclass
class Course:
    Year: str
    AuthorizedViewers: str
    School: str
    Grade: int
    Subject: str
    Course: str
    StartDate: int
    EndDate: int
    Unit: int
    Category: str
    Description: str
    ID: int

    @classmethod
    def fromRow(cls, row, rowNum):
        data = row.to_dict()
        data['ID'] = rowNum
        return cls(**data)

courseObjects = [Course.fromRow(row, idx) for idx, row in courses.iterrows()]

for obj in courseObjects:
    cursor.execute('''
    INSERT INTO courses (Year,AuthorizedViewers,School,Grade,Subject,Course,StartDate,EndDate,Unit,Category,Description) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (obj.Year, obj.AuthorizedViewers, obj.School, obj.Grade, obj.Subject, obj.Course, obj.StartDate, obj.EndDate, obj.Unit, obj.Category, obj.Description))

conn.commit()

cursor.execute('SELECT * FROM courses')
results = cursor.fetchall()
for row in results:
    print(row)

conn.close()


