import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE courses")

#Creating the course database
cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Year TEXT,
                    AuthorizedViewers TEXT,
                    School TEXT,
                    Grade INTEGER,
                    Subject TEXT,
                    Course TEXT,
                    StartDate INTEGER,
                    EndDate INTEGER,
                    Unit INTEGER,
                    Category TEXT,
                    Description TEXT
                )''')

# Inserting the first course from the spreadsheet as a test
# cursor.execute('''
#     INSERT INTO courses (Year,AuthorizedViewers,School,Grade,Subject,Course,StartDate,EndDate,Unit,Category,Description) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
# ''', (20232024,"Cagle, Scott; Garten, Christopher; miller, susan; Worlein, Elizabeth","Lotspeich Lower School",4,"Social Studies","Social Studies 4*",20230808,20230828,"The Human Body","Essential Questions","<ul><li>Why is it important that a person have a skeleton?</li><li>What are the four major organs and their purpose?</li></ul>"))

conn.commit()

cursor.execute('SELECT * FROM courses')
results = cursor.fetchall()
for row in results:
    print(row)

conn.close()